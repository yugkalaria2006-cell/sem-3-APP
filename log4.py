import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s: %(message)s",
    filename="log091026.log"
)

logging.info("Program started")
logging.warning("This is a warning")
logging.error("An error occurred")