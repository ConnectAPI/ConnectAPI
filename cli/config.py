from time import sleep
import secrets
from dataclasses import dataclass, MISSING


@dataclass
class UserConfig:
    http_port: int = 80
    https_port: int = 443
    dashboard_port: int = 6489
    domain: str = "localhost"


@dataclass
class SecretConfiguration:
    secret_key: str
    super_user_secret: str
    root_db_password: str
    gateway_db_password: str
    dashboard_db_password: str
    user_config: UserConfig


def generate_conf() -> SecretConfiguration:
    sleep(1)  # prevent output collision
    args = {}
    print("")
    for name, field in UserConfig.__dataclass_fields__.items():
        if field.default != MISSING:
            default = field.default
            value = input(f"Enter {name}[{default}]: ")
            if not value:
                value = default
        else:
            value = None
            while not value:
                value = input(f"Enter {name}[required!]: ")
        args[name] = value
        print("")
    user_config = UserConfig(**args)
    return SecretConfiguration(
        secret_key=secrets.token_urlsafe(20),
        super_user_secret=secrets.token_urlsafe(20),
        root_db_password=secrets.token_urlsafe(20),
        gateway_db_password="gatewaypass",
        dashboard_db_password="dashpassword",
        user_config=user_config,
    )
