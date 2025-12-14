import time
from src.structured_logging import log_event

def retry(fn, max_retries=3, backoff=1):
    for attempt in range(1, max_retries + 1):
        try:
            return fn()
        except Exception as e:
            log_event(
                "retry_failure",
                attempt=attempt,
                error=str(e)
            )
            if attempt == max_retries:
                raise
            time.sleep(backoff * attempt)
