

import os
import pandas as pd
import time

from metrics import Timer, record_metric
from exceptions import FileMissingError, log_error


RAW_FILE = "data/raw/raw_transactions.csv"
OUTPUT_FILE = "data/ledger/processed_transactions.csv"


def reconcile():
    if not os.path.exists(RAW_FILE):
        msg = "raw_transactions.csv missing"
        log_error(msg)
        raise FileMissingError(msg)

    with Timer("step_time", step="load_csv"):
        df = pd.read_csv(RAW_FILE)

    with Timer("step_time", step="clean"):
        df = df.dropna()

    with Timer("step_time", step="write_output"):
        os.makedirs("data/ledger", exist_ok=True)
        df.to_csv(OUTPUT_FILE, index=False)


if __name__ == "__main__":
    with Timer("execution_time", job="reconcile"):
        reconcile()
