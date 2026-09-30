---
title: ORDER BY Without a Tiebreaker Is a Flaky Test Generator
date: '2026-09-30'
source: https://dev.to/_66d02d0cc1ece7d1137c5f/order-by-without-a-tiebreaker-is-a-flaky-test-generator-2l51
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-05-how-query-optimizers-work-statistics-cardinality-join-order]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]'
status: unread
---

> **TL;DR:** I had a test that asserted orders.first().id == 9917 . It passed locally for months. Then it failed in CI, twice in a row, then passed again on a rerun. Nobody had touched the query. The query was this: SELECT id , creat…

## What’s new and why it matters
I had a test that asserted orders.first().id == 9917 . It passed locally for months. Then it failed in CI, twice in a row, then passed again on a rerun. Nobody had touched the query. The query was this: SELECT id , created_at , total_cents FROM orders WHERE customer_id = $ 1 ORDER BY created_at DESC LIMIT 1 ; The test seeded three orders for one customer inside a single transaction. All three got created_at = now() . now() is transaction_timestamp() — it does not advance during a transaction. So three rows shared the exact same timestamp to the microsecond. ORDER BY created_at DESC gives one v…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/_66d02d0cc1ece7d1137c5f/order-by-without-a-tiebreaker-is-a-flaky-test-generator-2l51

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-05-how-query-optimizers-work-statistics-cardinality-join-order]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]
