---
title: 'PostgreSQL 19 REPACK: Choosing the Right FILLFACTOR'
date: '2026-08-07'
source: https://dev.to/franckpachot/postgresql-19-repack-choosing-the-right-fillfactor-3848
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
status: unread
---

> **TL;DR:** I see users excited by REPACK in PostgreSQL 19 (currently in beta), because it looks like a simple command that reduces table bloat. But it's not that simple. Choosing the "right" FILLFACTOR is fundamentally a heuristic…

## What’s new and why it matters
I see users excited by REPACK in PostgreSQL 19 (currently in beta), because it looks like a simple command that reduces table bloat. But it's not that simple. Choosing the "right" FILLFACTOR is fundamentally a heuristic problem. For INSERTs, you can estimate future growth based on the expected lifecycle of newly inserted rows. For REPACK, you're repacking existing rows whose future update patterns are largely unknown. Excess free space is a waste of space, not only on disk, but also in memory, twice: Linux filesystem cache and PostgreSQL shared buffers. However, for rows that are still likely…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/franckpachot/postgresql-19-repack-choosing-the-right-fillfactor-3848

## Related notes
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
