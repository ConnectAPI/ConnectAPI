from logging import log
import secrets
import os
import time

import docker
from docker.errors import NotFound
from loguru import logger
from pymongo import MongoClient


from presistence import get_root


def create_secret(n: int) -> str:
    return secrets.token_urlsafe(n)


MARKETPLACE_URL = os.getenv("MARKETPLACE_URL")
DOCKER_NETWORK_NAME = "connectapi"
DOCKER_ACCOUNT = "connectapihub"

MONGODB_HOSTNAME = "mongo"
MONGO_FILES_DIR = str(get_root() / "mongo")

GATEWAY_HOSTNAME = "gateway"
DASHBOARD_HOSTNAME = "dashboard"


def setup_docker_network():
    logger.info(f"Setting up docker network <{DOCKER_NETWORK_NAME}>")
    client = docker.from_env()

    networks = client.networks.list(names=[DOCKER_NETWORK_NAME])
    if not networks:
        client.networks.create(DOCKER_NETWORK_NAME, "bridge")
    else:
        logger.warning("network all ready existing.")


def setup_mongodb(debug, conf):
    client = docker.from_env()

    logger.info("pulling mongodb image")
    client.images.pull("mongo:latest")

    try:
        client.containers.get("connectapi_mongodb")
    except NotFound:
        pass
    else:
        logger.debug("mongodb allready running")
        return

    # Run mongodb
    logger.info("Starting MongoDB")
    if not os.path.isdir(MONGO_FILES_DIR):
        os.mkdir(MONGO_FILES_DIR)
        logger.debug(f"Created {MONGO_FILES_DIR} dir")

    mongo_container = client.containers.run(
        "mongo:latest",
        name="connectapi_mongodb",
        hostname=MONGODB_HOSTNAME,
        ports={27017: 27017},
        environment={
            "MONGO_INITDB_ROOT_USERNAME": "root",
            "MONGO_INITDB_ROOT_PASSWORD": conf.root_db_password,
        },
        volumes=[f"{MONGO_FILES_DIR}:/data/db:rw"],
        network=DOCKER_NETWORK_NAME,
        detach=True,
        auto_remove=not debug,
    )

    logger.info("Setting up db and services auth")
    client = MongoClient(f"mongodb://root:{conf.root_db_password}@127.0.0.1:27017")
    
    client.gateway.command(
        'createUser', 'gateway', 
        pwd=conf.gateway_db_password,
        roles=[{'role': 'dbOwner', 'db': 'gateway'}]
    )

    client.dashboard.command(
        'createUser', 'dashboard', 
        pwd=conf.dashboard_db_password,
        roles=[{'role': 'dbOwner', 'db': 'dashboard'}]
    )


def start_containers(debug, conf):
    logger.debug(f"marketplace url: {MARKETPLACE_URL}")
    client = docker.from_env()

    # Run gateway
    logger.info("Pulling gateway image")
    client.images.pull(f"{DOCKER_ACCOUNT}/gateway")
    logger.info("Starting gateway")
    gateway_container = client.containers.run(
        f"{DOCKER_ACCOUNT}/gateway:latest",
        name="connectapi_gateway",
        hostname=GATEWAY_HOSTNAME,
        ports={80: 1687},
        environment={
            "SECRET_KEY": conf.secret_key,
            "SUPER_USER_SECRET": conf.super_user_secret,
            "MONGO_URL": f"mongodb://gateway:{conf.gateway_db_password}@{MONGODB_HOSTNAME}:27017/gateway",
            "REDIS_PORT": 6379,
            "REDIS_HOST": "redis",
            "ENV": "PRODUCTION",
            "DOCKER_NETWORK_NAME": DOCKER_NETWORK_NAME,
        },
        volumes={'/var/run/docker.sock': {'bind': '/var/run/docker.sock', 'mode': 'rw'}},
        detach=True,
        auto_remove=not debug,
        network=DOCKER_NETWORK_NAME,
    )
    logger.info(f"Started {gateway_container.short_id}")

    # Run dashboard
    logger.info("Pulling dashboard image")
    client.images.pull(f"{DOCKER_ACCOUNT}/dashboard")
    logger.info("Starting dashboard...")
    dashboard_container = client.containers.run(
        f"{DOCKER_ACCOUNT}/dashboard:latest",
        name="connectapi_dashboard",
        hostname=DASHBOARD_HOSTNAME,
        ports={80: 9934},
        environment={
            "SECRET_KEY": conf.secret_key,
            "SUPER_USER_SECRET": conf.super_user_secret,
            "MONGO_URL": f"mongodb://dashboard:{conf.dashboard_db_password}@{MONGODB_HOSTNAME}/dashboard",
            "MARKETPLACE_URL": MARKETPLACE_URL,
            "GATEWAY_URL": "http://gateway",
            "PORT": 80,
        },
        volumes={'/var/run/docker.sock': {'bind': '/var/run/docker.sock', 'mode': 'rw'}},
        detach=True,
        auto_remove=not debug,
        network=DOCKER_NETWORK_NAME,
    )
    logger.info(f"Started {dashboard_container.short_id}")


def stop_containers(debug):
    logger.debug(f"docker network name: {DOCKER_NETWORK_NAME}")

    prune = os.getenv("PRUNE", False) in (True, 1, "yes", "Yes", "y", "Y", "ok")
    logger.debug("Prune is on")

    logger.info("Stopping containers...")
    client = docker.from_env()

    containers = client.containers.list()
    my_containers = filter(lambda c: c.name.startswith("connectapi"), containers)

    for container in my_containers:
        logger.info(f"Stopping container {container.name} {container.short_id}")
        container.stop()
        logger.info("Stopped")
    
    if prune and os.path.isdir(f"{MONGO_FILES_DIR}"):
        logger.info("prunning all stored data")
        code = os.system(f"sudo rm -r {str(get_root())}")
        logger.debug(f"Prune exit code '{code}'")
    
    # TODO: delete docker network
    logger.debug("TODO: delete docker network")