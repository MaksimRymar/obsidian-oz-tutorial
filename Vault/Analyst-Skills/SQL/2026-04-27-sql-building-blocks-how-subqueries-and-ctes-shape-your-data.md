---
title: 'SQL Building Blocks: How Subqueries and CTEs Shape Your Data'
date: '2026-04-27'
source: https://dev.to/reinhard_bonnke_3c96981a4/sql-building-blocks-how-subqueries-and-ctes-shape-your-data-4b0j
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-04-22-understanding-subqueries-vs-ctes-in-sql-with-examples]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-04-21-ctes-subqueries-and-query-optimisation-in-sql]]'
- '[[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-04-20-up-down-or-down-up-understanding-subqueries-and-ctes-in-sql-a-comprehensive-guide]]'
status: unread
---

> **TL;DR:** Unless you are new to SQL, at some point you have written a query that begins to resemble a puzzle box query, query within query, difficult to read, more difficult to debug. CTEs fix that. So, What is a CTE? CTE is an ab…

## What’s new and why it matters
Unless you are new to SQL, at some point you have written a query that begins to resemble a puzzle box query, query within query, difficult to read, more difficult to debug. CTEs fix that. So, What is a CTE? CTE is an abbreviation that means Common Table Expression . It is simply a means of assigning value to a query in order to be able to employ it later in the same statement like a table. It is the keyword WITH . What is the point of using one? Readability. Your SQL is top down rather than inwards. Reusability. You need not rewrite the query, you can refer to the same CTE more than once. Eas…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/reinhard_bonnke_3c96981a4/sql-building-blocks-how-subqueries-and-ctes-shape-your-data-4b0j

## Related notes
- [[2026-04-22-understanding-subqueries-vs-ctes-in-sql-with-examples]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-04-21-ctes-subqueries-and-query-optimisation-in-sql]]
- [[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-04-20-up-down-or-down-up-understanding-subqueries-and-ctes-in-sql-a-comprehensive-guide]]
