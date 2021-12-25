import sys

from loguru import logger


def setup_logger(debug: bool):
    logger_level = "INFO"

    if debug:
        logger.info("Starting debug mode")
        logger_level = "DEBUG"
    logger.remove()
    logger.add(sys.stderr, level=logger_level)