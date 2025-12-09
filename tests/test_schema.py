# tests/test_schema.py
import json
from pathlib import Path
from jsonschema import validate

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"

def test_schema_valid():
    schema = json.loads((SCHEMAS / "transactions_schema.json").read_text())
    golden = json.loads((SCHEMAS / "golden_transaction.json").read_text())

    validate(golden, schema)
