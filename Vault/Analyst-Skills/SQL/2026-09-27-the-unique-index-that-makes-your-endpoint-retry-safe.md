---
title: The Unique Index That Makes Your Endpoint Retry-Safe
date: '2026-09-27'
source: https://dev.to/_66d02d0cc1ece7d1137c5f/the-unique-index-that-makes-your-endpoint-retry-safe-35o9
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
status: unread
---

> **TL;DR:** The payment form double-submitted on a flaky connection. Two POSTs hit /payments with the same idempotency key. One row landed in the table. The client got 200 OK both times. I asked why the second insert did not fail, a…

## What’s new and why it matters
The payment form double-submitted on a flaky connection. Two POSTs hit /payments with the same idempotency key. One row landed in the table. The client got 200 OK both times. I asked why the second insert did not fail, and got three different answers from three engineers. The real answer was in a migration from before any of us joined. CREATE UNIQUE INDEX payments_idempotency_key_idx ON payments ( idempotency_key ); That index, and nothing in the Python, is what made the endpoint safe to retry. The constraint is the retry policy The handler looked like this. def create_payment ( req ): try : c…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/_66d02d0cc1ece7d1137c5f/the-unique-index-that-makes-your-endpoint-retry-safe-35o9

## Related notes
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
