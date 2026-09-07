---
title: Why Adding an Index Won't Fix Your Slow COUNT(*) in PostgreSQL
date: '2026-09-07'
source: https://dev.to/bodanthebackend/why-adding-an-index-wont-fix-your-slow-count-in-postgresql-477a
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** COUNT(*) looks like a trivial operation: SELECT COUNT ( * ) FROM orders ; The query asks for a single number, but that doesn't mean PostgreSQL can produce it with a constant-time read from some internal counter. When we…

## What’s new and why it matters
COUNT(*) looks like a trivial operation: SELECT COUNT ( * ) FROM orders ; The query asks for a single number, but that doesn't mean PostgreSQL can produce it with a constant-time read from some internal counter. When we need an exact count, PostgreSQL has to determine how many rows are actually part of the visible result set for that query. On large tables, that work can become a meaningful chunk of total execution time. And the problem doesn't just go away by throwing an index at it. The useful question isn't "do I have an index?" It's: How many rows does PostgreSQL actually need to examine t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/bodanthebackend/why-adding-an-index-wont-fix-your-slow-count-in-postgresql-477a

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
