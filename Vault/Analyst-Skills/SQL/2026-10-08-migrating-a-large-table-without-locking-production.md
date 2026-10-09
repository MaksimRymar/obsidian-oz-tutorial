---
title: Migrating a Large Table Without Locking Production
date: '2026-10-08'
source: https://dev.to/andriiboyko/migrating-a-large-table-without-locking-production-2fk7
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-10-01-adding-a-not-null-column-to-a-large-postgresql-table-constant-default-backfill-or-not-valid]]'
- '[[2026-10-08-your-postgres-id-columns-will-run-out-of-numbers-heres-a-10-second-check-and-the-trap-that-hides-it]]'
- '[[2026-08-15-why-your-postgres-migration-locked-the-whole-table-and-the-pattern-that-doesnt]]'
status: unread
---

> **TL;DR:** GoCardless once took around 15 seconds of unexpected API downtime from a planned migration. The tables being changed were empty. The statement was fast. It didn't matter, because the migration needed a lock on a heavily…

## What’s new and why it matters
GoCardless once took around 15 seconds of unexpected API downtime from a planned migration. The tables being changed were empty. The statement was fast. It didn't matter, because the migration needed a lock on a heavily used parent table, a long-running read was already holding a conflicting lock, and every API query that arrived after that queued up behind the migration until clients timed out. They wrote it up in Zero-downtime Postgres migrations: the hard parts . That story is the best correction I know to the way this topic usually gets framed. "Tables too big to lock" suggests the danger…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/andriiboyko/migrating-a-large-table-without-locking-production-2fk7

## Related notes
- [[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-10-01-adding-a-not-null-column-to-a-large-postgresql-table-constant-default-backfill-or-not-valid]]
- [[2026-10-08-your-postgres-id-columns-will-run-out-of-numbers-heres-a-10-second-check-and-the-trap-that-hides-it]]
- [[2026-08-15-why-your-postgres-migration-locked-the-whole-table-and-the-pattern-that-doesnt]]
