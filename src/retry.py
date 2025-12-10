import time
import random

def retry(operation, max_retries=3):
    attempt = 0

    while attempt < max_retries:
        try:
            print(f"Attempt {attempt + 1}")
            operation()
            return
        except Exception as e:
            print(f"Failed: {e}")
            sleep_time = 2 ** attempt
            print(f"Retrying in {sleep_time}s...")
            time.sleep(sleep_time)
            attempt += 1

    print("❌ All retries exhausted")
