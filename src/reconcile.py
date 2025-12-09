import os
import pandas as pd
from src.exceptions import log_error

RAW_PATH = "data/raw/raw_transactions.csv"
OUT_PATH = "data/outputs/cleaned_transactions.csv"

def reconcile():
    try:
        if not os.path.exists(RAW_PATH):
            raise FileNotFoundError("raw_transactions.csv missing")

        df = pd.read_csv(RAW_PATH)

        if df.empty:
            raise ValueError("Raw file is empty")

        df.to_csv(OUT_PATH, index=False)
        print("✅ Reconciliation successful")

    except Exception as e:
        log_error(str(e))

if __name__ == "__main__":
    reconcile()
