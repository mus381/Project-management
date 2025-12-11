import time
import logging

LOG_PATH = "logs/metrics.log"

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def record_metric(name: str, value):
    logging.info(f"{name}={value}")

def time_it(fn):
    def wrapper():
        start = time.time()
        fn()
        end = time.time()
        record_metric("execution_time", round(end - start, 4))
    return wrapper
