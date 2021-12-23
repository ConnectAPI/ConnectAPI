import os
import secrets

import docker

DOCKER_NETWORK_NAME = "core"


def create_secret(n: int) -> str:
    return secrets.token_urlsafe(n)

MARKETPLACE_URL = os.environ.get("MARKETPLACE_URL")
SECRET_KEY = create_secret(20)
SUPER_USER_SECRET = create_secret(20)
GATEWAY_DB_PASSWORD = create_secret(20)
DASHBOARD_DB_PASSWORD = create_secret(20)

print("SECRET_KEY",         SECRET_KEY)
print("SUPER_USER_SECRET",  SUPER_USER_SECRET)
print("GATEWAY_DB_PASSWORD",         GATEWAY_DB_PASSWORD)
print("SECRET_KEY",         DASHBOARD_DB_PASSWORD)


def deploy_containers():
    client = docker.from_env()

    client.networks.create(DOCKER_NETWORK_NAME, "bridge")

    # Run gateway
    client.containers.run(
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
        },
        volumes={'/var/run/docker.sock': {'bind': '/var/run/docker.sock', 'mode': 'rw'}},
        detach=True,
        network="core",
    )

    # Run dashboard
    client.containers.run(
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
        network="core",
    )


def main():
    deploy_containers()


if __name__ == "__main__":
    main()
