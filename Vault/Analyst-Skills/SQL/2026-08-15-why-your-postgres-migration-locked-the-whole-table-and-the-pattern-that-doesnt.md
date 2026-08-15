---
title: Why Your Postgres Migration Locked the Whole Table (and the Pattern That Doesn't)
date: '2026-08-15'
source: https://dev.to/libme/why-your-postgres-migration-locked-the-whole-table-and-the-pattern-that-doesnt-38k4
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-13-zero-downtime-schema-changes-expandcontract-backfills-online-ddl]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
status: unread
---

> **TL;DR:** The ALTER TABLE itself is usually not slow — the outage comes from Postgres queueing every other query behind the lock it is waiting for. The fix is two habits: set lock_timeout on every migration session so a blocked DD…

## What’s new and why it matters
The ALTER TABLE itself is usually not slow — the outage comes from Postgres queueing every other query behind the lock it is waiting for. The fix is two habits: set lock_timeout on every migration session so a blocked DDL statement fails fast instead of freezing traffic, and split anything that rewrites or validates a table into a non-blocking two-step ( NOT VALID then VALIDATE , or CREATE INDEX CONCURRENTLY ). Everything else in this post is detail on which operations need which treatment. This is written for Postgres 12 and up, which is where the cheap paths for most of these operations land…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/libme/why-your-postgres-migration-locked-the-whole-table-and-the-pattern-that-doesnt-38k4

## Related notes
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-13-zero-downtime-schema-changes-expandcontract-backfills-online-ddl]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
