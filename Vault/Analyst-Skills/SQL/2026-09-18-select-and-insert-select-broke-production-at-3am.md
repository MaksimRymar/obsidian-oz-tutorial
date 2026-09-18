---
title: SELECT * and INSERT ... SELECT Broke Production at 3am
date: '2026-09-18'
source: https://dev.to/_66d02d0cc1ece7d1137c5f/select-and-insert-select-broke-production-at-3am-2jfo
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-02-deriving-data-quality-rules-from-the-schema-what-the-metadata-already-knows]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
status: unread
---

> **TL;DR:** The 3am failure At 03:12 the alert was a Postgres error, not a latency graph: ERROR: null value in column "tenant_id" violates not-null constraint The job was a backfill I wrote months earlier. Two statements, no column…

## What’s new and why it matters
The 3am failure At 03:12 the alert was a Postgres error, not a latency graph: ERROR: null value in column "tenant_id" violates not-null constraint The job was a backfill I wrote months earlier. Two statements, no column lists anywhere: INSERT INTO accounts_archive SELECT * FROM accounts WHERE created_at < '2026-01-01' ; When I wrote it, accounts and accounts_archive had the same columns in the same order. I checked with \d , saw them line up, and shipped it. Six months later a teammate added tenant_id uuid NOT NULL DEFAULT gen_random_uuid() and a generated email_domain column to accounts . Nob…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/_66d02d0cc1ece7d1137c5f/select-and-insert-select-broke-production-at-3am-2jfo

## Related notes
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-02-deriving-data-quality-rules-from-the-schema-what-the-metadata-already-knows]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
