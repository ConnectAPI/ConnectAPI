import os
import sys

from loguru import logger

from logger import setup_logger
from continers import start_containers, stop_containers
from config import generate_conf


DEBUG = os.getenv("DEBUG", False) in (True, 1, "yes", "Yes", "y", "ok")


def setup_db():
    logger.info("setting up db...")
    # TODO: setup db


def install_and_start_system():
    conf = generate_conf()
    logger.debug(conf.__dict__)

    setup_db()
    start_containers(debug=DEBUG, conf=conf)


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
