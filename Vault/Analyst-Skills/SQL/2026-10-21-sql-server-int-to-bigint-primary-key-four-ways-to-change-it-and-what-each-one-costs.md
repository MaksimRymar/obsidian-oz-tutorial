---
title: 'SQL Server INT to BIGINT Primary Key: Four Ways to Change It and What Each
  One Costs'
date: '2026-10-21'
source: https://dev.to/tbson87/sql-server-int-to-bigint-primary-key-four-ways-to-change-it-and-what-each-one-costs-df6
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-10-08-your-postgres-id-columns-will-run-out-of-numbers-heres-a-10-second-check-and-the-trap-that-hides-it]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: SQL Server refuses ALTER COLUMN on an INT primary key while the key, any foreign key or any index uses t…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: SQL Server refuses ALTER COLUMN on an INT primary key while the key, any foreign key or any index uses the column, so the in-place change is drop, alter, recreate. On two 1,000,000-row tables that took 20.5 seconds and about 1 GB of transaction log. Row compression stops the ALTER COLUMN from rewriting rows, new tables copied across avoid the long lock, and a negative reseed buys time when no window is available yet. To change an INT primary key to BIGINT in SQL Server, you have…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/sql-server-int-to-bigint-primary-key-four-ways-to-change-it-and-what-each-one-costs-df6

## Related notes
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-10-08-your-postgres-id-columns-will-run-out-of-numbers-heres-a-10-second-check-and-the-trap-that-hides-it]]
