import os
import pandas as pd

LEDGER_PATH = "data/ledger/processed_transactions.csv"
RAW_PATH = "data/raw/raw_transactions.csv"

os.makedirs("data/ledger", exist_ok=True)

def process_once():
    if not os.path.exists(RAW_PATH):
        print("No raw file found.")
        return

    if os.path.exists(LEDGER_PATH):
        print("Ledger already exists. Skipping.")
        return

    df = pd.read_csv(RAW_PATH)
    df.to_csv(LEDGER_PATH, index=False)
    print("✅ Ledger created")

if __name__ == "__main__":
    process_once()
