---
title: 'Postgres MERGE vs INSERT ON CONFLICT: MERGE Failed 3 of 4 Concurrent Batches'
date: '2026-11-16'
source: https://medium.com/@nazmul_hasan/postgres-merge-vs-insert-on-conflict-merge-failed-3-of-4-concurrent-batches-9b999523e49c?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
related:
- '[[2026-10-23-using-claude-to-plan-a-fast-and-safe-bulk-load-with-postgres-copy]]'
- '[[2026-07-22-postgresql-is-not-just-a-database-it-is-a-tiny-operating-system-for-your-data]]'
- '[[2026-06-29-mongodb-vs-postgresql-the-arguments-everyone-gets-wrong]]'
- '[[2026-10-26-setting-up-logical-replication-between-two-postgres-instances]]'
- '[[2026-11-04-using-claude-to-write-postgres-upserts-4-on-conflict-traps-that-lose-data-without-an-error]]'
- '[[2026-04-23-5-postgresql-time-bugs-youll-write-before-you-know-any-better]]'
status: unread
---

> **TL;DR:** I timed eight bulk upserts from Python on PostgreSQL 18. The statement barely changed the speed. Skipping unchanged rows cut WAL by 4x. Continue reading on Medium »

## What’s new and why it matters
I timed eight bulk upserts from Python on PostgreSQL 18. The statement barely changed the speed. Skipping unchanged rows cut WAL by 4x. Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/@nazmul_hasan/postgres-merge-vs-insert-on-conflict-merge-failed-3-of-4-concurrent-batches-9b999523e49c?source=rss------sql-5

## Related notes
- [[2026-10-23-using-claude-to-plan-a-fast-and-safe-bulk-load-with-postgres-copy]]
- [[2026-07-22-postgresql-is-not-just-a-database-it-is-a-tiny-operating-system-for-your-data]]
- [[2026-06-29-mongodb-vs-postgresql-the-arguments-everyone-gets-wrong]]
- [[2026-10-26-setting-up-logical-replication-between-two-postgres-instances]]
- [[2026-11-04-using-claude-to-write-postgres-upserts-4-on-conflict-traps-that-lose-data-without-an-error]]
- [[2026-04-23-5-postgresql-time-bugs-youll-write-before-you-know-any-better]]
