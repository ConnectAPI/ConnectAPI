import sys
import os
import secrets

import docker

from debug import run as run_debug
from file import load_container_ids, save_container_ids


def create_secret(n: int) -> str:
    return secrets.token_urlsafe(n)


MARKETPLACE_URL = os.environ.get("MARKETPLACE_URL")
SECRET_KEY = create_secret(20)
SUPER_USER_SECRET = create_secret(20)
GATEWAY_DB_PASSWORD = "gatewaypass" #create_secret(20)
DASHBOARD_DB_PASSWORD = "dashpassword" #create_secret(20)
DOCKER_NETWORK_NAME = "connectapi"
DEBUG = os.getenv("DEBUG", False) in (True, 1, "yes", "Yes", "y", "ok")


print("SECRET_KEY",         SECRET_KEY)
print("SUPER_USER_SECRET",  SUPER_USER_SECRET)
print("GATEWAY_DB_PASSWORD",         GATEWAY_DB_PASSWORD)
print("DASHBOARD_DB_PASSWORD",         DASHBOARD_DB_PASSWORD)


def setup_db():
    print("TODO: setup db")
    # TODO: setup db


def install_and_start_system():
    client = docker.from_env()

    networks = client.networks.list(names=[DOCKER_NETWORK_NAME])
    if not networks:
        client.networks.create(DOCKER_NETWORK_NAME, "bridge")
    else:
        print("WARNING: network all ready existing.")

    # Run gateway
    gateway_container = client.containers.run(
        "connectapi_gateway:latest",
        name="connectapi_gateway",
        hostname="gateway",
        ports={80: 1687},
        environment={
            "SECRET_KEY": SECRET_KEY,
            "SUPER_USER_SECRET": SUPER_USER_SECRET,
            "MONGO_URL": f"mongodb://gatewayname:{GATEWAY_DB_PASSWORD}@5.183.9.78:27017/gateway",
            "REDIS_PORT": 6379,
            "REDIS_HOST": "redis",
            "ENV": "PRODUCTION",
            "DOCKER_NETWORK_NAME": DOCKER_NETWORK_NAME,
        },
        volumes={'/var/run/docker.sock': {'bind': '/var/run/docker.sock', 'mode': 'rw'}},
        detach=True,
        auto_remove=not DEBUG,
        network=DOCKER_NETWORK_NAME,
    )

    # Run dashboard
    dashboard_container = client.containers.run(
        "connectapi_dashboard:latest",
        name="connectapi_dashboard",
        hostname="dashboard",
        ports={80: 9934},
        environment={
            "SECRET_KEY": SECRET_KEY,
            "mongo_url": f"mongodb://dashusername:{DASHBOARD_DB_PASSWORD}@5.183.9.78:27017/Dashboard",
            "marketplace_url": MARKETPLACE_URL,
            "gateway_url": "http://gateway",
            "port": 80,
        },
        volumes={'/var/run/docker.sock': {'bind': '/var/run/docker.sock', 'mode': 'rw'}},
        detach=True,
        auto_remove=not DEBUG,
        network=DOCKER_NETWORK_NAME,
    )
    print(gateway_container.id, dashboard_container.id)
    save_container_ids([gateway_container.id, dashboard_container.id])


def stop_and_uninstall_system():
    ids = load_container_ids()
    client = docker.from_env()

    for id in ids:
        container = client.containers.get(id)
        container.stop()


def run_command(command):
    if command == "install":
        install_and_start_system()
    elif command == "uninstall":
        stop_and_uninstall_system()
    else:
        print("ERROR: command not exist.")


def main():
    command = "install"
    if len(sys.argv) > 1:
        command = sys.argv[1]
    run_command(command)

    if DEBUG:
        run_debug()


if __name__ == "__main__":
    main()
