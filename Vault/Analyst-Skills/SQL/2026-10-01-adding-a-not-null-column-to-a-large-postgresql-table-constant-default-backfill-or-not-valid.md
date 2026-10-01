---
title: 'Adding a NOT NULL Column to a Large PostgreSQL Table: Constant Default, Backfill
  or NOT VALID'
date: '2026-10-01'
source: https://dev.to/tbson87/adding-a-not-null-column-to-a-large-postgresql-table-constant-default-backfill-or-not-valid-1ha3
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]'
- '[[2026-09-27-postgresql-generated-column-vs-trigger-which-to-use-for-a-derived-column]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: On PostgreSQL 11 and later, ADD COLUMN ... NOT NULL DEFAULT 'new' is a catalogue change that took 10 ms…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: On PostgreSQL 11 and later, ADD COLUMN ... NOT NULL DEFAULT 'new' is a catalogue change that took 10 ms on 5,000,000 rows, but a volatile default such as gen_random_uuid() rewrote the whole table in 10.4 seconds. When the value has to be computed per row, add the column as nullable, backfill it in batches, and prove it NOT NULL with a constraint added NOT VALID and validated separately, so the full scan never holds a lock that blocks reads. Set lock_timeout on every one of these…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/tbson87/adding-a-not-null-column-to-a-large-postgresql-table-constant-default-backfill-or-not-valid-1ha3

## Related notes
- [[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]
- [[2026-09-27-postgresql-generated-column-vs-trigger-which-to-use-for-a-derived-column]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
