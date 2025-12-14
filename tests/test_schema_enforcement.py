import pytest
from src.schema_validate import run_validation

def test_schema_validation_passes_when_no_violations():
    """
    If the raw CSV contains only valid rows,
    run_validation() should NOT raise an exception.
    """
    run_validation()  # Should complete silently


def test_schema_validation_raises_on_violations(tmp_path, monkeypatch):
    """
    When we inject a malformed record, run_validation()
    must raise ValueError.
    """
    # --- Create a fake raw CSV with one invalid row ---
    bad_csv = tmp_path / "raw_transactions.csv"
    bad_csv.write_text(
        "transaction_id,merchant_id,amount,currency,type,created_at,status\n"
        "txn_bad,m_404,NOT_A_NUMBER,KES,sale,2025-12-03T09:15:00Z,settled\n"
    )

    # Patch RAW path inside the module
    monkeypatch.setattr(
        "src.schema_validate.RAW",
        bad_csv
    )

    with pytest.raises(ValueError):
        run_validation()
