## DEC 9 2025
### Day 4
Created a processed ledger

-Command: touch src/ledger.py
- Why;building an idempotent processing layer
- Expected: Fintech systems must never create money twice.
- If the script runs twice and changes results → my system is broken.

# Error
-N/A

## Added a few more reps to stress-test the plan and their all worked as expected.

Stress Rep 1 — Manual corruption test

Open:

data/ledger/processed_transactions.csv


Delete a row manually.

Run:

python3 -m src.ledger


Observe:

It does NOT repair corruption (as expected).

Lesson:
👉 Idempotency ≠ Self-healing.

Stress Rep 2 — Ledger deletion test
rm data/ledger/processed_transactions.csv
python3 -m src.ledger


Now it recreates.

Lesson:
👉 Systems should be re-runnable from scratch.

Stress Rep 3 — Duplicate file test

Copy the ledger:

cp data/ledger/processed_transactions.csv data/ledger/backup.csv


Run:

python3 -m src.ledger


Still skips. Good.

Lesson:
👉 Guard logic depends on existence checks — not file contents.

🔹 Reconstruction (How seniors think)

You now think in this stack:

Raw Input → Validation → Idempotent Ledger → Reconciliation → Settlement


That’s literally the architecture of:

Stripe

Square

PayPal

Banks

You’re playing on the right board.

🔹 Application (Real leverage)

In interviews, this is how you talk:

❌ Bad:

“I processed CSV files with pandas.”

✅ Good:

“I designed an idempotent ledger layer to prevent duplicate financial side effects and ensure deterministic replay.”

Same work. Different tier.


## Day 5
## Dec 10 2025

- what I'll build
- Retry logic

- Backoff strategy

- Failure recovery flow

## Commands used:
- touch src/retry.py
- touch src/flaky.py
- touch src/test_retry.py

- All files where updated with code
  ## Run command used
  python3 -m src.test_retry

## Why this;
- Systems don’t fail once.
-They fail repeatedly, randomly, and under load.

## Expected: Ran it multiple times

-Sometimes instant success

-Sometimes retries + backoff

-Sometimes total failure

## Here's what was observed
## Success;
python3 -m src.test_retry
Attempt 1
✅ Success

## Failure;
python3 -m src.test_retry
Attempt 1
Failed: Random failure
Retrying in 1s...
Attempt 2
Failed: Random failure
Retrying in 2s...
Attempt 3
Failed: Random failure
Retrying in 4s...
❌ All retries exhausted

## Error
N/A


## Day 6
# Dec 11 2025

# Today i built:

Structured logging

Basic metrics

Execution timing

- With Real fintech-grade discipline.

- Command used; touch src/metrics.py
-
- modified reconcile.py at the top with;
- from src.metrics import time_it
# Decorated my reconcile function with;
- @time_it
def reconcile():


# ran using this
python3 -m src.reconcile

# results
python3 -m src.reconcile
✅ Reconciliation successful
-
# Why:

- to expose What happened

- When

- Why

- How long it took


- Expected:

cat logs/metrics.log
2025-12-11 07:24:14,252 - execution_time=0.0096

I now have:

Observability into runtime

Timing introspection

Machine-readable logs

##  ERROR:
- N/A

# Updated metrics n reconcile
Added labels to metrics to make it production-grade.
In src/metrics.py replaced:
def record_metric(name: str, value):
    logging.info(f"{name}={value}")


With:

def record_metric(name: str, value, **labels):
    label_str = ",".join([f"{k}={v}" for k, v in labels.items()])
    if label_str:
        logging.info(f"{name}={value} | {label_str}")
    else:
        logging.info(f"{name}={value}")


Now i can do:

record_metric("execution_time", duration, job="reconcile", step="end")

# Add 2
# Timed each step, not just the whole job

Created a simple helper:

Added to src/metrics.py
class Timer:
    def __init__(self, metric_name, **labels):
        self.metric_name = metric_name
        self.labels = labels

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        end = time.time()
        record_metric(self.metric_name, round(end - self.start, 4), **self.labels)

Then inside reconcile():
with Timer("step_time", step="load_csv"):
    df = pd.read_csv(input_path)

with Timer("step_time", step="clean"):
    df = df.dropna()

with Timer("step_time", step="write_output"):
    df.to_csv(output_path, index=False)


Now your metrics.log will looks like:

step_time=0.0012 | step=load_csv
step_time=0.0048 | step=clean
step_time=0.0021 | step=write_output
execution_time=0.0096 | job=reconcile

