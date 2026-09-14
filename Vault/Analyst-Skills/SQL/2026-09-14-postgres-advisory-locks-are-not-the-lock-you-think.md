---
title: Postgres Advisory Locks Are Not the Lock You Think
date: '2026-09-14'
source: https://dev.to/_66d02d0cc1ece7d1137c5f/postgres-advisory-locks-are-not-the-lock-you-think-3ig3
domain: SQL
relevance: 🔴
tags:
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-09-06-your-audit-log-is-probably-lying-to-you-postgres-18-fixes-it-in-one-statement]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
status: unread
---

> **TL;DR:** At 03:40 my nightly reconcile job ran twice. Two workers, same pg_advisory_lock(42) , both proceeded, and the refunds went out twice. The lock was real. The code was correct. It still did nothing, because each worker hel…

## What’s new and why it matters
At 03:40 my nightly reconcile job ran twice. Two workers, same pg_advisory_lock(42) , both proceeded, and the refunds went out twice. The lock was real. The code was correct. It still did nothing, because each worker held a different Postgres backend behind PgBouncer in transaction mode. pg_advisory_lock looks like a distributed lock. It is not one. It is a mutex owned by a database session. What the lock actually is A session-level advisory lock lives in the backend process that ran the statement. pg_advisory_lock(key) blocks until it gets the lock. pg_try_advisory_lock(key) returns true or f…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/_66d02d0cc1ece7d1137c5f/postgres-advisory-locks-are-not-the-lock-you-think-3ig3

## Related notes
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-09-06-your-audit-log-is-probably-lying-to-you-postgres-18-fixes-it-in-one-statement]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
