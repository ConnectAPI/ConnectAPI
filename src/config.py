import secrets
from dataclasses import dataclass


@dataclass
class SecretConfiguration:
    secret_key: str
    super_user_secret: str
    gateway_db_password: str
    dashboard_db_password: str


def generate_conf() -> SecretConfiguration:
    return SecretConfiguration(
        secret_key=secrets.token_urlsafe(20),
        super_user_secret=secrets.token_urlsafe(20),
        gateway_db_password="gatewaypass",
        dashboard_db_password="dashpassword",
    )
