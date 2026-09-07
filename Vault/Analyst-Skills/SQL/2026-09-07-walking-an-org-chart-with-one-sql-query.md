---
title: Walking an Org Chart with One SQL Query
date: '2026-09-07'
source: https://dev.to/rahmanfrr/walking-an-org-chart-with-one-sql-query-14c0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-07-30-how-to-write-a-cohort-retention-query-in-sql-that-actually-runs]]'
- '[[2026-09-04-recursive-ctes-explained-from-first-principles]]'
- '[[2026-04-22-subqueries-vs-ctes-when-why-how]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
status: unread
---

> **TL;DR:** Walking an Org Chart with One SQL Query Some data is naturally arranged like a tree: Employees and managers Folders and files Categories and subcategories Comments and replies A recursive CTE lets SQL walk through that t…

## What’s new and why it matters
Walking an Org Chart with One SQL Query Some data is naturally arranged like a tree: Employees and managers Folders and files Categories and subcategories Comments and replies A recursive CTE lets SQL walk through that tree. The table Imagine an employees table like this: id name manager_id 1 Maya NULL 2 Jon 1 3 Priya 1 4 Leo 2 manager_id points to another employee in the same table. The recursive query WITH RECURSIVE org AS ( -- Start with the top-level employee SELECT id , name , manager_id , 0 AS level , ARRAY [ id ] AS path FROM employees WHERE manager_id IS NULL UNION ALL -- Find employee…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rahmanfrr/walking-an-org-chart-with-one-sql-query-14c0

## Related notes
- [[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-07-30-how-to-write-a-cohort-retention-query-in-sql-that-actually-runs]]
- [[2026-09-04-recursive-ctes-explained-from-first-principles]]
- [[2026-04-22-subqueries-vs-ctes-when-why-how]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
