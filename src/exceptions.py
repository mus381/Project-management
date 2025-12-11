import os
import logging

LOG_PATH = "logs/errors.log"

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("fintech_logger")
logger.setLevel(logging.ERROR)

if not logger.handlers:
    handler = logging.FileHandler(LOG_PATH)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def log_error(message: str):
    logger.error(message)
    print(f"[LOGGED] {message}")


class FileMissingError(Exception):
    pass
