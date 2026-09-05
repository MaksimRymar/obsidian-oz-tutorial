---
title: SQL COMMANDS,AND FUNCTIONS CONCEPTS
date: '2026-09-05'
source: https://dev.to/abineshrajendiran/sql-commandsand-functions-concepts-27ai
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-06-19-oracle-ora-00934-error-causes-and-solutions-complete-guide]]'
- '[[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]'
status: unread
---

> **TL;DR:** 1. SQL Basics & Filtering SELECT ** SELECT — SELECT name FROM users; → picks which columns to return. **Example: SELECT * FROM users; → returns all columns. * DISTINCT * SELECT DISTINCT city FROM users; → removes duplica…

## What’s new and why it matters
1. SQL Basics & Filtering SELECT ** SELECT — SELECT name FROM users; → picks which columns to return. **Example: SELECT * FROM users; → returns all columns. * DISTINCT * SELECT DISTINCT city FROM users; → removes duplicate rows from results. * FROM * SELECT * FROM users; → names the table to query. WHERE SELECT * FROM users WHERE age > 18; → filters rows before grouping/output. EXAMPLE : * AND * WHERE age > 18 AND city='Chennai'; → all conditions must be true. OR — WHERE city='Chennai' OR city='Trichy'; → at least one condition must be true. * NOT * WHERE NOT city='Chennai'; → negates a condit…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/abineshrajendiran/sql-commandsand-functions-concepts-27ai

## Related notes
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-06-19-oracle-ora-00934-error-causes-and-solutions-complete-guide]]
- [[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]
