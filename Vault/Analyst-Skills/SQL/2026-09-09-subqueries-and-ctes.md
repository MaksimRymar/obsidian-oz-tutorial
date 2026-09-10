---
title: SUBQUERIES and CTEs
date: '2026-09-09'
source: https://dev.to/elizabeth_njoroge_7c850b9/subqueries-and-ctes-2e5n
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-09-07-subqueries-ctes-in-sql-what-they-are-and-when-to-use-each]]'
- '[[2026-08-04-write-clearer-sql-when-to-use-ctes-or-subqueries]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-04-26-sql-subqueries-vs-ctes-a-complete-guide-for-data-analysts-published]]'
- '[[2026-04-21-ctes-subqueries-and-query-optimisation-in-sql]]'
- '[[2026-02-25-common-table-expressions]]'
status: unread
---

> **TL;DR:** SUBQUERIES Subquery is a query inside a query and is used when one statement needs a result from another. It is usually inside a clause like 'where' : 'from' or 'select'. CTE A CTE(Common Table Expression) is a temporary…

## What’s new and why it matters
SUBQUERIES Subquery is a query inside a query and is used when one statement needs a result from another. It is usually inside a clause like 'where' : 'from' or 'select'. CTE A CTE(Common Table Expression) is a temporary named result set that one can reference within single query to reuse in the next query. Advantages of CTE CTEs tend to be preferred for readability and structuring complex structure. A thing with CTEs is it is reusable in that you can reuse the definition without rewriting it. Difference between subquery and CTE CTEs support recursion while subqueries do not. Subqueries can be…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/elizabeth_njoroge_7c850b9/subqueries-and-ctes-2e5n

## Related notes
- [[2026-09-07-subqueries-ctes-in-sql-what-they-are-and-when-to-use-each]]
- [[2026-08-04-write-clearer-sql-when-to-use-ctes-or-subqueries]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-04-26-sql-subqueries-vs-ctes-a-complete-guide-for-data-analysts-published]]
- [[2026-04-21-ctes-subqueries-and-query-optimisation-in-sql]]
- [[2026-02-25-common-table-expressions]]
