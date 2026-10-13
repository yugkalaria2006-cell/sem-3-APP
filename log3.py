
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

try:
    a = 10
    b = 0
    result = a / b
    logging.info("Result: %s", result)

except Exception:
    logging.exception("An error occurred")