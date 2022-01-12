import os
import sys

from loguru import logger

from logger import setup_logger
from continers import setup_docker_network, setup_mongodb, start_containers, stop_containers
from config import generate_conf


DEBUG = os.getenv("DEBUG", False) in (True, 1, "yes", "Yes", "y", "Y", "ok")


def install_and_start_system():
    conf = generate_conf()
    logger.debug(conf.__dict__)

    setup_docker_network()
    setup_mongodb(DEBUG, conf)
    start_containers(debug=DEBUG, conf=conf)
    
    logger.info(f"Running dashboard on http://{conf.user_config.domain}:{conf.user_config.dashboard_port}")


def stop_and_uninstall_system():
    stop_containers(debug=DEBUG)


def run_command(command):
    if command == "install":
        install_and_start_system()
    elif command == "uninstall":
        stop_and_uninstall_system()
    else:
        print("ERROR: command not exist.")


def main():
    setup_logger(DEBUG)

    command = "install"
    if len(sys.argv) > 1:
        command = sys.argv[1]

    logger.info(f"Starting command '{command}'")
    run_command(command)


if __name__ == "__main__":
    main()
