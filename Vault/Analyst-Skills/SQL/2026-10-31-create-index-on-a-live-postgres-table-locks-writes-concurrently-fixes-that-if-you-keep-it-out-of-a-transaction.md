---
title: CREATE INDEX on a live Postgres table locks writes. CONCURRENTLY fixes that,
  if you keep it out of a transaction
date: '2026-10-31'
source: https://dev.to/labyrinthlab/create-index-on-a-live-postgres-table-locks-writes-concurrently-fixes-that-if-you-keep-it-out-of-4bm6
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-08-28-stop-writing-raw-sql-in-your-migrations-most-of-the-time]]'
- '[[2026-08-15-why-your-postgres-migration-locked-the-whole-table-and-the-pattern-that-doesnt]]'
- '[[2026-09-28-how-i-stream-row-changes-out-of-sqlite-without-touching-the-app-reading-the-wal]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-07-06-create-index-is-a-write-outage-in-disguise]]'
status: unread
---

> **TL;DR:** Here is the failure. You ship a migration that adds an index on a busy table: CREATE INDEX idx_orders_customer_id ON orders ( customer_id ); Postgres builds the index with a SHARE lock. Other sessions can still SELECT .…

## What’s new and why it matters
Here is the failure. You ship a migration that adds an index on a busy table: CREATE INDEX idx_orders_customer_id ON orders ( customer_id ); Postgres builds the index with a SHARE lock. Other sessions can still SELECT . They cannot INSERT , UPDATE , or DELETE until the build finishes. On a large table that can be minutes or hours of blocked writes. The PostgreSQL CREATE INDEX docs say so outright: a standard index build "locks out writes (but not reads) on the table until it's done." The fix is also in those docs: CREATE INDEX CONCURRENTLY idx_orders_customer_id ON orders ( customer_id ); CONC…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/labyrinthlab/create-index-on-a-live-postgres-table-locks-writes-concurrently-fixes-that-if-you-keep-it-out-of-4bm6

## Related notes
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-08-28-stop-writing-raw-sql-in-your-migrations-most-of-the-time]]
- [[2026-08-15-why-your-postgres-migration-locked-the-whole-table-and-the-pattern-that-doesnt]]
- [[2026-09-28-how-i-stream-row-changes-out-of-sqlite-without-touching-the-app-reading-the-wal]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-07-06-create-index-is-a-write-outage-in-disguise]]
