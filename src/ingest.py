# src/ingest.py
import json
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

RAW_DIR = ROOT / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

SCHEMAS = ROOT / "schemas"
golden = SCHEMAS / "golden_transaction.json"

def load_golden_record():
    with open(golden) as f:
        return json.load(f)

def ingest_raw_transactions():
    """Load raw CSV and return DataFrame."""
    raw_file = RAW_DIR / "raw_transactions.csv"
    if not raw_file.exists():
        raise FileNotFoundError(f"Missing raw file: {raw_file}")

    df = pd.read_csv(raw_file)
    return df

if __name__ == "__main__":
    print("Golden record loaded:", load_golden_record())
    df = ingest_raw_transactions()
    print(df.head())
