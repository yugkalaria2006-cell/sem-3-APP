import logging

logging.basicConfig(level=logging.INFO,format="%(asctime)s | %(levelname)s | %(message)s")

logging.info("Program Started")
logging.warning("Data is missing")
logging.error("Database Conection Error")
