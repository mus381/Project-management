import logging
import time
import os

LOG_PATH = "logs/metrics.log"
os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("metrics_logger")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.FileHandler(LOG_PATH)
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def record_metric(name: str, value, **labels):
    label_str = ",".join([f"{k}={v}" for k, v in labels.items()])
    if label_str:
        logger.info(f"{name}={value} | {label_str}")
    else:
        logger.info(f"{name}={value}")


class Timer:
    def __init__(self, metric_name, **labels):
        self.metric_name = metric_name
        self.labels = labels

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        end = time.time()
        duration = round(end - self.start, 4)
        record_metric(self.metric_name, duration, **self.labels)
