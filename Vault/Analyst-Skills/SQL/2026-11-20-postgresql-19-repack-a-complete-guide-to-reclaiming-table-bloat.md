---
title: 'PostgreSQL 19 REPACK: A Complete Guide to Reclaiming Table Bloat'
date: '2026-11-20'
source: https://dev.to/database-engineering/postgresql-19-repack-table-bloat-locks-and-alternatives-1f6e
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-08-postgres-autovacuum-isnt-keeping-up-diagnosing-bloat-long-transactions-and-wraparound-warnings]]'
- '[[2026-06-30-postgresql-mvcc-vacuum-bloat-wraparound-autovacuum-tuning-in-production]]'
- '[[2026-10-15-vacuum-full-locks-your-table-the-whole-time-postgres-19s-repack-concurrently-doesnt]]'
- '[[2026-09-10-postgresql-mvcc-why-bloat-doesnt-automatically-mean-expensive-reads]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-11-20-sql-server-columnstore-indexes-fast-reporting-on-large-tables]]'
status: unread
---

> **TL;DR:** Darshan Turakhia reported that a high-traffic notifications table accumulated 11.2 million dead rows . In that case, the autovacuum threshold and I/O budget let new dead tuples accumulate faster than vacuum could clear t…

## What’s new and why it matters
Darshan Turakhia reported that a high-traffic notifications table accumulated 11.2 million dead rows . In that case, the autovacuum threshold and I/O budget let new dead tuples accumulate faster than vacuum could clear them. The table plus indexes occupied 41 GB before pg_repack reduced them to 9.8 GB. More generally, ordinary VACUUM makes dead-tuple space reusable inside PostgreSQL but usually does not shrink the relation file. PostgreSQL 19 introduces REPACK as a core SQL command to solve this exact gap. TL;DR PostgreSQL 19 introduces REPACK , a built-in SQL command that reclaims disk space…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/database-engineering/postgresql-19-repack-table-bloat-locks-and-alternatives-1f6e

## Related notes
- [[2026-09-08-postgres-autovacuum-isnt-keeping-up-diagnosing-bloat-long-transactions-and-wraparound-warnings]]
- [[2026-06-30-postgresql-mvcc-vacuum-bloat-wraparound-autovacuum-tuning-in-production]]
- [[2026-10-15-vacuum-full-locks-your-table-the-whole-time-postgres-19s-repack-concurrently-doesnt]]
- [[2026-09-10-postgresql-mvcc-why-bloat-doesnt-automatically-mean-expensive-reads]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-11-20-sql-server-columnstore-indexes-fast-reporting-on-large-tables]]
