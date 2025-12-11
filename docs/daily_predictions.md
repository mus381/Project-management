## dec 9 2025
## day 4

# BEFORE running:
# Prediction: This will fail because there was no executable logic.

python3 -m src.ledger

## the logic that was missing at the script
if __name__ == "__main__":
    process_once()





# AFTER running:
# It failed; Nothing  happened yet. Because we didn’t call the function.

# After calling the function
-python3 -m src.ledger
-✅ Ledger created

# After running the command twice to guarantee idempotency
-Ledger already exists. Skipping.

# Lessons learned;
-I now understand:

Why Stripe, PayPal, banks use idempotent keys

Why retries can’t create duplicates

Why ledger systems exist

## Day 5
# dec 10 2025

## Predections
the command ran with alternative success n failures proving this;
## What I just learned

- I now understand:

- Why APIs aren't trusted blindly

- Why Stripe retries webhooks

- Why networks lie

- Why backoff prevents outages


# day 6
# Dec 11 2025

# predictions

i ran command python3 -m src.reconcile
n got this output
python3 -m src.reconcile
✅ Reconciliation successful

proving this you can’t trust what you can’t see.

strongly validated by this;
cat logs/metrics.log
2025-12-11 07:24:14,252 - execution_time=0.0096

# what i just learned

Observability into runtime

Timing introspection

Machine-readable logs

literally what production fintech relies on.
