---
title: The fundamentals of SQL Subqueries and Common Table Expressions (CTEs)
date: '2026-09-09'
source: https://dev.to/steve_m/the-fundamentals-of-sql-subqueries-and-common-table-expressions-ctes-3bj3
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-04-28-understanding-subquery-and-common-table-expressionsctes]]'
- '[[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]'
- '[[2026-06-30-cte-vs-temporary-tables-in-sql-which-one-should-you-use]]'
- '[[2026-04-26-sql-subqueries-vs-ctes-a-complete-guide-for-data-analysts-published]]'
status: unread
---

> **TL;DR:** As you work on data with SQL you will encounter situations where you are trying to achieve very specific results depending on the conditions of your query. For instance given a study group schema , with members table and…

## What’s new and why it matters
As you work on data with SQL you will encounter situations where you are trying to achieve very specific results depending on the conditions of your query. For instance given a study group schema , with members table and quiz results table, and you are required to figure out the members who scored above the average for all the tests. To solve this you will end up with a series of queries, or a complex query, where you need to filter out the members results , find the average score for the tests and finally filter out only the members who scored above the average found. While this may be achiev…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/steve_m/the-fundamentals-of-sql-subqueries-and-common-table-expressions-ctes-3bj3

## Related notes
- [[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-04-28-understanding-subquery-and-common-table-expressionsctes]]
- [[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]
- [[2026-06-30-cte-vs-temporary-tables-in-sql-which-one-should-you-use]]
- [[2026-04-26-sql-subqueries-vs-ctes-a-complete-guide-for-data-analysts-published]]
