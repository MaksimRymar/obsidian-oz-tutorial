---
title: 'Foreign Key Cascade Deletes: Un-Indexed FKs, Slow Cascades, and Lock Contention
  in PostgreSQL'
date: '2026-10-29'
source: https://dev.to/usman_khan_io/foreign-key-cascade-deletes-un-indexed-fks-slow-cascades-and-lock-contention-in-postgresql-3n45
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#presentations'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-10-24-why-do-database-indexes-slow-down-inserts-the-b-tree-page-split-dilemma]]'
- '[[2026-06-30-postgresql-mvcc-vacuum-bloat-wraparound-autovacuum-tuning-in-production]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-08-09-3-database-query-patterns-that-kill-performance-and-how-to-fix-them]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
status: unread
---

> **TL;DR:** Running a DELETE on a parent entity with ON DELETE CASCADE feels like clean relational cleanup. But if any child or grandchild table in the dependency chain lacks an index on its foreign key column, PostgreSQL falls back…

## What’s new and why it matters
Running a DELETE on a parent entity with ON DELETE CASCADE feels like clean relational cleanup. But if any child or grandchild table in the dependency chain lacks an index on its foreign key column, PostgreSQL falls back to full sequential scans on every cascade step, turning a quick delete into a long-running transaction that holds row locks and starves concurrent writes. Here is an architectural deep dive into what actually happens during an un-indexed cascade, and how to build an asynchronous soft-delete purge pipeline. In multi-tenant relational design, enforcing referential integrity with…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/usman_khan_io/foreign-key-cascade-deletes-un-indexed-fks-slow-cascades-and-lock-contention-in-postgresql-3n45

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-10-24-why-do-database-indexes-slow-down-inserts-the-b-tree-page-split-dilemma]]
- [[2026-06-30-postgresql-mvcc-vacuum-bloat-wraparound-autovacuum-tuning-in-production]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-08-09-3-database-query-patterns-that-kill-performance-and-how-to-fix-them]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
