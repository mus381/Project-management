import json, os, logging, time
LOG_PATH = "logs/structured.log"
os.makedirs("logs", exist_ok=True)
logger = logging.getLogger("structured")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.FileHandler(LOG_PATH)
    handler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(handler)

def log_event(event_type, **payload):
    payload.update({
        "ts": time.time(),
        "event": event_type
    })
    logger.info(json.dumps(payload))
