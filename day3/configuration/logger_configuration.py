import logging

def configure_logger():
    """Configure the logger for the healthcare application."""

    # Create a logger instance
    logger = logging.getLogger("healthcare.logger")
    logger.setLevel(logging.DEBUG)

    # Avoid adding multiple handlers
    if logger.handlers:
        return logger

    # Create file handler
    file_handler = logging.FileHandler("healthcare.log")
    file_handler.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Set formatter and add handler
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

logger = configure_logger()
logger.info("Healthcare system started")
logger.error("Patient record not found")