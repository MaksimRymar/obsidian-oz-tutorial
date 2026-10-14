---
title: 'Subquery vs CTE in SQL: When and How to Use Each'
date: '2026-10-14'
source: https://dev.to/petermuriya/subquery-vs-cte-in-sql-when-and-how-to-use-each-1n0h
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-09-subqueries-and-ctes]]'
- '[[2026-09-10-subqueries-ctes-breaking-complex-queries-into-steps]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]'
- '[[2026-04-22-understanding-subqueries-vs-ctes-in-sql-with-examples]]'
- '[[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]'
status: unread
---

> **TL;DR:** A subquery is a SQL query nested inside another statement, while a Common Table Expression (CTE) is a named temporary result set defined with WITH before the main query. Subqueries suit quick, one-off calculations; CTEs…

## What’s new and why it matters
A subquery is a SQL query nested inside another statement, while a Common Table Expression (CTE) is a named temporary result set defined with WITH before the main query. Subqueries suit quick, one-off calculations; CTEs break complex queries into readable, reusable steps and are the only way to write recursive queries. Think of a subquery as scratch math in the margin, and a CTE as a labeled table on the whiteboard that you can refer back to. What Is a Subquery in SQL? A subquery can appear inside SELECT , INSERT , UPDATE , or DELETE . The PostgreSQL documentation covers three common forms: Sc…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/petermuriya/subquery-vs-cte-in-sql-when-and-how-to-use-each-1n0h

## Related notes
- [[2026-09-09-subqueries-and-ctes]]
- [[2026-09-10-subqueries-ctes-breaking-complex-queries-into-steps]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]
- [[2026-04-22-understanding-subqueries-vs-ctes-in-sql-with-examples]]
- [[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]
