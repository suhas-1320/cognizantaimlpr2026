import logging
import os

def configure_logger():
    """Configure the logger for the healthcare application."""

    logger = logging.getLogger("healthcare.logger")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    if logger.handlers:
        return logger

    log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    log_path = os.path.join(log_dir, "healthcare.log")

    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

logger = configure_logger()
logger.info("Healthcare system started")