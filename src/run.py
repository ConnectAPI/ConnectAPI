import os
import sys

from loguru import logger

from continers import start_containers, stop_containers


DEBUG = os.getenv("DEBUG", False) in (True, 1, "yes", "Yes", "y", "ok")


def setup_db():
    logger.info("setting up db...")
    # TODO: setup db


def install_and_start_system():
    setup_db()
    start_containers(debug=DEBUG)


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
    command = "install"
    if len(sys.argv) > 1:
        command = sys.argv[1]
    logger.info(f"Starting command <{command}>")
    if DEBUG:
        logger.info("Starting debug mode")
        logger.level("DEBUG")
    run_command(command)


if __name__ == "__main__":
    main()
