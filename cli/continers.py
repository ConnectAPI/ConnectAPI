import secrets
import os

import docker
from loguru import logger


def create_secret(n: int) -> str:
    return secrets.token_urlsafe(n)


MARKETPLACE_URL = os.getenv("MARKETPLACE_URL")
DOCKER_NETWORK_NAME = "connectapi"


def start_containers(debug, conf):
    logger.debug(f"marketplace url: {MARKETPLACE_URL}")
    logger.debug(f"docker network name: {DOCKER_NETWORK_NAME}")

    client = docker.from_env()

    networks = client.networks.list(names=[DOCKER_NETWORK_NAME])
    if not networks:
        client.networks.create(DOCKER_NETWORK_NAME, "bridge")
    else:
        logger.warning("network all ready existing.")

    # Run gateway
    logger.info("Starting gateway")
    gateway_container = client.containers.run(
        "connectapi_gateway:latest",
        name="connectapi_gateway",
        hostname="gateway",
        ports={80: 1687},
        environment={
            "SECRET_KEY": conf.secret_key,
            "SUPER_USER_SECRET": conf.super_user_secret,
            "MONGO_URL": f"mongodb://gatewayname:{conf.gateway_db_password}@5.183.9.78:27017/gateway",
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
    logger.info("Starting dashboard...")
    dashboard_container = client.containers.run(
        "connectapi_dashboard:latest",
        name="connectapi_dashboard",
        hostname="dashboard",
        ports={80: 9934},
        environment={
            "SECRET_KEY": conf.secret_key,
            "SUPER_USER_SECRET": conf.super_user_secret,
            "MONGO_URL": f"mongodb://dashusername:{conf.dashboard_db_password}@5.183.9.78:27017/Dashboard",
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

    logger.info("Stopping containers...")
    client = docker.from_env()

    containers = client.containers.list()
    my_containers = filter(lambda c: c.name.startswith("connectapi"), containers)

    for container in my_containers:
        logger.info(f"Stopping container {container.name} {container.short_id}")
        container.stop()
        logger.info("Stopped")

    # TODO: delete docker network
