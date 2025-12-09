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

