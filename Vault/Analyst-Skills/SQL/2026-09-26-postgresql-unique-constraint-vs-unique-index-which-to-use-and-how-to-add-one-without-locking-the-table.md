---
title: 'PostgreSQL Unique Constraint vs Unique Index: Which to Use, and How to Add
  One Without Locking the Table'
date: '2026-09-26'
source: https://dev.to/tbson87/postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-j6f
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Use a unique constraint when the rule covers every row and plain columns, because only a constraint can…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Use a unique constraint when the rule covers every row and plain columns, because only a constraint can be DEFERRABLE or named in ON CONFLICT ON CONSTRAINT , though not both at once. Use a unique index when the rule needs a WHERE clause or an expression such as lower(email) . On a large table, add either one by building the index with CREATE UNIQUE INDEX CONCURRENTLY first, because a plain ALTER TABLE ... ADD CONSTRAINT ... UNIQUE holds back reads and writes until it has checked…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-j6f

## Related notes
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]
