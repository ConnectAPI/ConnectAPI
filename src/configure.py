import os
import secrets


def create_secret(n: int) -> str:
    return secrets.token_urlsafe(n)


def create_secrets():
    os.environ["SECRET_KEY"] = create_secret(20)
    os.environ["SUPER_USER_SECRET"] = create_secret(20)
    os.environ["GATEWAY_DB_PASSWORD"] = create_secret(20)
    os.environ["DASHBOARD_DB_PASSWORD"] = create_secret(20)
    print("SECRET_KEY", os.environ["SECRET_KEY"])
    print("SUPER_USER_SECRET", os.environ["SUPER_USER_SECRET"])
    print("SECRET_KEY", os.environ["GATEWAY_DB_PASSWORD"])
    print("SECRET_KEY", os.environ["DASHBOARD_DB_PASSWORD"])


def run_docker_compose():
    os.system("docker-compose up")


def main():
    create_secrets()
    run_docker_compose()


if __name__ == "__main__":
    main()
