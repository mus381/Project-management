# Daily Settlement Data Flow

1. Ingest raw transactions from payment switches.
2. Validate transaction structure and types.
3. Reconcile:
   - Deduplicate by txn_id
   - Filter bad records
   - Identify settled transactions
   - Compute merchant summaries
4. Output daily settlement report files.
5. Push exceptions to data/exceptions for review.

This mirrors how fintech orgs (Stripe, Flutterwave, MPesa) structure daily settlement flows.
