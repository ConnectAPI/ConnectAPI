import os
from time import sleep
import secrets
import json

from loguru import logger
from pydantic import BaseModel, conint

from presistence import get_root


CONFIG_DIR_PATH = get_root() / "configuration"
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.json"


class UserConfig(BaseModel):
    http_port: conint(gt=0, lt=65000) = 80
    dashboard_port: conint(gt=0, lt=65000) = 6489
    domain: str = "localhost"


class SecretConfiguration(BaseModel):
    secret_key: str
    super_user_secret: str
    root_db_password: str
    gateway_db_password: str
    dashboard_db_password: str
    user_config: UserConfig
    loaded: bool = False


def _save_config(conf: dict):
    if not os.path.isdir(str(CONFIG_DIR_PATH)):
        logger.debug("Creating config dir")
        os.mkdir(str(CONFIG_DIR_PATH))
    
    with open(str(CONFIG_FILE_PATH), 'w') as config_file:
        config_file.write(json.dumps(conf))
    logger.info("Saved config")


def _load_config() -> dict:
    if not (os.path.isdir(str(CONFIG_DIR_PATH)) and os.path.isfile(str(CONFIG_FILE_PATH))):
        logger.info("Config not found")
        return None
    logger.info("Loading config")
    with open(str(CONFIG_FILE_PATH), 'r') as config_file:
        config_json = config_file.read()
        return json.loads(config_json)


def generate_conf() -> SecretConfiguration:
    loaded_config = _load_config()
    if loaded_config is not None:
        return SecretConfiguration(**loaded_config, loaded=True)

    sleep(1)  # prevent output collision
    args = {}
    print("")
    for name, field in UserConfig.__fields__.items():
        value = None
        while value is None:
            value = input(f"Enter {name}[{field.default if not field.required else 'required'}]: ")
            if not value:
                value = None
            if not value and field.default:
                value = field.default
        args[field.name] = value
        print("")
    
    user_config = UserConfig(**args)
    config = SecretConfiguration(
        secret_key=secrets.token_urlsafe(20),
        super_user_secret=secrets.token_urlsafe(20),
        root_db_password=secrets.token_urlsafe(20),
        gateway_db_password=secrets.token_urlsafe(20),
        dashboard_db_password=secrets.token_urlsafe(20),
        user_config=user_config,
    )
    _save_config(config.dict(exclude={"loaded",}))
    return config
