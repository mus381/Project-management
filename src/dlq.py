from pathlib import Path
import csv, os, json

DLQ_DIR = Path("data/dlq")
DLQ_DIR.mkdir(parents=True, exist_ok=True)

def push_to_dlq(row_dict, reason="unknown"):
    fname = f"dlq_{int(Path().stat().st_mtime)}.csv"
    out = DLQ_DIR / fname
    # append style; if file exists, append header only once
    write_header = not out.exists()
    with open(out, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(row_dict.keys())+["dlq_reason"])
        if write_header:
            writer.writeheader()
        row_dict["dlq_reason"] = reason
        writer.writerow(row_dict)
