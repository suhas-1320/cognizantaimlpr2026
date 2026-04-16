
import sys
import os

# Get absolute path of project root (day3)
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")
)

# Add project root to sys.path if not already present
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


from configuration.logger_configuration import configure_logger
"""
    Entry point for the application. This module initializes the application and runs the main logic.
"""
logger = configure_logger()

def run():
    logger.info("Running the application...")
    logger.info("Application finished successfully.")

#handle entry point for the application
if __name__ == "__main__":
    run()