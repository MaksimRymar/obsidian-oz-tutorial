---
title: '# Subqueries & CTEs: Two Ways to Query Inside a Query'
date: '2026-09-29'
source: https://dev.to/patrickomondi/-subqueries-ctes-two-ways-to-query-inside-a-query-4k2k
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-10-subqueries-ctes-breaking-complex-queries-into-steps]]'
- '[[2026-09-09-subqueries-and-ctes]]'
- '[[2026-04-21-subqueries-and-ctes-in-sql]]'
- '[[2026-04-22-understanding-subqueries-vs-ctes-in-sql-with-examples]]'
- '[[2026-09-07-subqueries-ctes-in-sql-what-they-are-and-when-to-use-each]]'
- '[[2026-08-07-sql-subqueries-vs-ctes-types-differences-performance-and-when-to-use-each]]'
status: unread
---

> **TL;DR:** Sometimes one query needs the result of another query to work. SQL gives you two main tools for that: subqueries and CTEs (Common Table Expressions). They can often solve the same problem, but they read differently, and…

## What’s new and why it matters
Sometimes one query needs the result of another query to work. SQL gives you two main tools for that: subqueries and CTEs (Common Table Expressions). They can often solve the same problem, but they read differently, and knowing when to reach for each makes your SQL a lot easier to write and debug. What Are Subqueries? A subquery is a query nested inside another query, wrapped in parentheses. It runs first, and its result is used by the outer query, whether that's a single value, a list of values, or an entire table-like result. Subqueries can live almost anywhere: in the SELECT list, the FROM…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/patrickomondi/-subqueries-ctes-two-ways-to-query-inside-a-query-4k2k

## Related notes
- [[2026-09-10-subqueries-ctes-breaking-complex-queries-into-steps]]
- [[2026-09-09-subqueries-and-ctes]]
- [[2026-04-21-subqueries-and-ctes-in-sql]]
- [[2026-04-22-understanding-subqueries-vs-ctes-in-sql-with-examples]]
- [[2026-09-07-subqueries-ctes-in-sql-what-they-are-and-when-to-use-each]]
- [[2026-08-07-sql-subqueries-vs-ctes-types-differences-performance-and-when-to-use-each]]
