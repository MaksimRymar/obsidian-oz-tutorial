---
title: 'Migrating 200 Million Records in .NET: From Row-by-Row to a Crash-Safe Batched
  Pipeline'
date: '2026-07-30'
source: https://dev.to/arash_zand/migrating-200-million-records-in-net-from-row-by-row-to-a-crash-safe-batched-pipeline-3d5b
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#sql'
- '#tool'
related:
- '[[2026-04-22-upsert-in-mysql-postgresql-sqlite-ms-sql-server-a-complete-comparison]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-03-26-design-a-reliable-wallet-transfer-system-with-acid-guarantees-pt---1-atomicity]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
status: unread
---

> **TL;DR:** A real-world walkthrough of how we rewrote a data migration four times before it was production-ready. We had to move email history records out of a legacy SQL Server system (16 regional databases, ~200 million rows tota…

## What’s new and why it matters
A real-world walkthrough of how we rewrote a data migration four times before it was production-ready. We had to move email history records out of a legacy SQL Server system (16 regional databases, ~200 million rows total) into a PostgreSQL privacy service already running in production. The job had to be idempotent, restartable without duplicates, survive network drops, and finish fast enough to matter. We went through five versions. Here's what changed each time and why. The Setup Source (SQL Server — 16 regional DBs): CREATE TABLE [ dbo ].[ PlayerEmailHistory ] ( [ HistoryId ] INT NOT NULL I…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/arash_zand/migrating-200-million-records-in-net-from-row-by-row-to-a-crash-safe-batched-pipeline-3d5b

## Related notes
- [[2026-04-22-upsert-in-mysql-postgresql-sqlite-ms-sql-server-a-complete-comparison]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-03-26-design-a-reliable-wallet-transfer-system-with-acid-guarantees-pt---1-atomicity]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
