import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "raw_transactions.csv"
SCHEMA = ROOT / "schemas" / "transaction_schema.json"
BAD = ROOT / "data" / "exceptions"
BAD.mkdir(exist_ok=True)

REQUIRED_COLS = [
    "txn_id", "merchant_id", "amount", "currency",
    "type", "created_at", "status"
]

def validate_transactions():
    if not RAW.exists():
        raise FileNotFoundError("raw_transactions.csv missing")

    df = pd.read_csv(RAW)

    # 1. Missing columns
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        df.to_csv(BAD / "missing_columns.csv", index=False)
        raise ValueError(f"Missing required columns: {missing}")

    # 2. Drop completely empty rows
    df = df.dropna(how="all")

    # 3. Bad datatypes: amount must be float
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    bad_amount = df[df["amount"].isna()]
    if not bad_amount.empty:
        bad_amount.to_csv(BAD / "bad_amount.csv", index=False)
        df = df[df["amount"].notna()]

    return df
