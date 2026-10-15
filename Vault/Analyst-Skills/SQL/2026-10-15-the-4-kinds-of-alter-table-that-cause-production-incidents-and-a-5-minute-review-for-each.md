---
title: The 4 kinds of ALTER TABLE that cause production incidents (and a 5-minute
  review for each)
date: '2026-10-15'
source: https://dev.to/sayonilmitra/the-4-kinds-of-alter-table-that-cause-production-incidents-and-a-5-minute-review-for-each-5gog
domain: SQL
relevance: 🔴
tags:
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-15-why-your-postgres-migration-locked-the-whole-table-and-the-pattern-that-doesnt]]'
- '[[2026-10-01-adding-a-not-null-column-to-a-large-postgresql-table-constant-default-backfill-or-not-valid]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
status: unread
---

> **TL;DR:** A migration that runs fine on your laptop's empty database can still fail, or do real damage, in production. Production has data, traffic, and application code that depends on the old schema. You don't need a heavyweight…

## What’s new and why it matters
A migration that runs fine on your laptop's empty database can still fail, or do real damage, in production. Production has data, traffic, and application code that depends on the old schema. You don't need a heavyweight process to catch most of it. You need to look at each statement and ask which of four categories it falls into. Here's a migration that looks routine: ALTER TABLE orders DROP COLUMN legacy_ref ; ALTER TABLE orders RENAME COLUMN cust_id TO customer_id ; ALTER TABLE orders ADD COLUMN region TEXT NOT NULL ; CREATE INDEX idx_orders_customer ON orders ( customer_id ); Every one of…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/sayonilmitra/the-4-kinds-of-alter-table-that-cause-production-incidents-and-a-5-minute-review-for-each-5gog

## Related notes
- [[2026-08-15-why-your-postgres-migration-locked-the-whole-table-and-the-pattern-that-doesnt]]
- [[2026-10-01-adding-a-not-null-column-to-a-large-postgresql-table-constant-default-backfill-or-not-valid]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
