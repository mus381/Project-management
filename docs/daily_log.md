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
