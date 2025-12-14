from pathlib import Path
import csv
import json
from jsonschema import Draft7Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "transactions_schema.json"
RAW = ROOT / "data" / "raw" / "raw_transactions.csv"
BAD = ROOT / "data" / "exceptions"
BAD.mkdir(parents=True, exist_ok=True)

def load_schema():
    return json.loads(SCHEMA.read_text())

def validate_row_dict(row_dict, validator):
    return list(validator.iter_errors(row_dict))

def run_validation():
    schema = load_schema()
    validator = Draft7Validator(schema, format_checker=FormatChecker())

    bad_rows = []
    keys = None

    with RAW.open() as f:
        reader = csv.DictReader(f)
        keys = reader.fieldnames

        for row in reader:
            # Convert numeric strings to actual types if needed
            # Keeping it simple for now: pure string input allowed
            errors = validate_row_dict(row, validator)
            if errors:
                row["_errors"] = [e.message for e in errors]
                bad_rows.append(row)

    if bad_rows:
        out = BAD / "schema_violations.csv"
        with out.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys + ["_errors"])
            writer.writeheader()
            writer.writerows(bad_rows)

        raise ValueError(f"{len(bad_rows)} schema violations -> {out}")

    print("Schema validation passed!")
