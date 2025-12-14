import os
import pandas as pd
from time import sleep

from metrics import Timer, record_metric
from exceptions import FileMissingError, log_error
from src.structured_logging import log_event
from src.retry import retry
from src.dlq import push_to_dlq

RAW_FILE = "data/raw/raw_transactions.csv"
OUTPUT_FILE = "data/ledger/processed_transactions.csv"


def process_row(row):
    """Wrap risky per-row operation in retry; push to DLQ if all retries fail."""
    def op():
        # Placeholder for per-row risky work, e.g. transformations
        # row["amount"] = some_transformation(row["amount"])
        pass

    try:
        retry(op, max_retries=3)
    except Exception as e:
        push_to_dlq(row.to_dict(), reason=str(e))


def reconcile():
    log_event("load_start", job="reconcile")

    if not os.path.exists(RAW_FILE):
        msg = "raw_transactions.csv missing"
        log_error(msg)
        raise FileMissingError(msg)

    with Timer("step_time", step="load_csv"):
        df = pd.read_csv(RAW_FILE)
        log_event("load_end", job="reconcile", rows=len(df))

    with Timer("step_time", step="clean"):
        df = df.dropna()
        log_event("clean_end", job="reconcile", cleaned_rows=len(df))

    # Process rows individually with retry + DLQ
    with Timer("step_time", step="process_rows"):
        for _, row in df.iterrows():
            process_row(row)

    # Write final CSV with retry
    with Timer("step_time", step="write_output"):
        def write_op():
            os.makedirs("data/ledger", exist_ok=True)
            df.to_csv(OUTPUT_FILE, index=False)

        retry(write_op, max_retries=3)
        log_event("write_end", job="reconcile", output_file=str(OUTPUT_FILE))


if __name__ == "__main__":
    with Timer("execution_time", job="reconcile"):
        reconcile()
