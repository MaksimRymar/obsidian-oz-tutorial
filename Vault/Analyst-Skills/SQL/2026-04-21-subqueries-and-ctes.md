---
title: Subqueries and Cte's
date: '2026-04-21'
source: https://dev.to/martin_ndungu_38/subqueries-and-ctes-105b
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-04-20-subqueries-vs-ctes-and-when-to-use-each]]'
- '[[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]'
- '[[2026-02-25-common-table-expressions]]'
- '[[2026-04-19-understanding-subqueries-and-ctes-in-sql]]'
- '[[2026-04-19-subqueries-vs-ctes-choosing-the-right-tool-in-sql]]'
status: unread
---

> **TL;DR:** Introduction SQL is a powerful language used for managing and analyzing data. As queries become more complex, tools like subqueries and Common Table Expressions (CTEs) help simplify logic and improve readability. What is…

## What’s new and why it matters
Introduction SQL is a powerful language used for managing and analyzing data. As queries become more complex, tools like subqueries and Common Table Expressions (CTEs) help simplify logic and improve readability. What is a Subquery? A subquery is a query nested inside another query. It is used to perform operations that depend on the result of another query. Example: SELECT name FROM customers WHERE customer_id IN ( SELECT customer_id FROM sales ); Types of Subqueries Scalar Subquery Returns a single value. Multi-row Subquery Returns multiple rows. Correlated Subquery Depends on the outer quer…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/martin_ndungu_38/subqueries-and-ctes-105b

## Related notes
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-04-20-subqueries-vs-ctes-and-when-to-use-each]]
- [[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]
- [[2026-02-25-common-table-expressions]]
- [[2026-04-19-understanding-subqueries-and-ctes-in-sql]]
- [[2026-04-19-subqueries-vs-ctes-choosing-the-right-tool-in-sql]]
