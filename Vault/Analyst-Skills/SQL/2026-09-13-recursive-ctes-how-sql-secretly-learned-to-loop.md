---
title: 'Recursive CTEs: How SQL Secretly Learned to Loop'
date: '2026-09-13'
source: https://dev.to/rahmanfrr/recursive-ctes-how-sql-secretly-learned-to-loop-457f
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-07-10-sql-recursive-ctes-hierarchies-trees-graph-traversal-bill-of-materials]]'
- '[[2026-08-13-cohort-retention-analysis-in-sql-the-query-that-tells-you-if-your-product-is-actually-sticky]]'
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
- '[[2026-09-04-recursive-ctes-explained-from-first-principles]]'
status: unread
---

> **TL;DR:** Ask a SQL query to find "all employees under this manager," and things get ugly fast if you don't know how many levels deep the org chart goes. A regular join handles one level. Two joins handle two levels. Nobody's writ…

## What’s new and why it matters
Ask a SQL query to find "all employees under this manager," and things get ugly fast if you don't know how many levels deep the org chart goes. A regular join handles one level. Two joins handle two levels. Nobody's writing seven joins for seven levels of middle management. This is exactly the problem recursive CTEs exist to solve — and most people who've written SQL for years have never touched one. The setup: data that references itself Picture a plain employees table where each row points to its own manager: CREATE TABLE employees ( id INT PRIMARY KEY , name TEXT , manager_id INT REFERENCES…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rahmanfrr/recursive-ctes-how-sql-secretly-learned-to-loop-457f

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-07-10-sql-recursive-ctes-hierarchies-trees-graph-traversal-bill-of-materials]]
- [[2026-08-13-cohort-retention-analysis-in-sql-the-query-that-tells-you-if-your-product-is-actually-sticky]]
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
- [[2026-09-04-recursive-ctes-explained-from-first-principles]]
