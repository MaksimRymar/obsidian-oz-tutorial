---
title: SQL, GroupBy and Aggregates
date: '2026-11-26'
source: https://dev.to/awji/sql-groupby-and-aggregates-3e9h
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-10-12-where-vs-having-in-sql-a-simple-way-to-understand-the-difference]]'
- '[[2026-08-28-sql-execution-order-internals-why-where-fails-on-aliases-but-order-by-succeeds]]'
- '[[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]'
- '[[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]'
- '[[2026-05-13-sql-execution-order-write-queries-that-think-like-the-database]]'
status: unread
---

> **TL;DR:** How Grouping happens under the hood Let's take this example: SELECT user_id , SUM ( amount ) as balance from transactions where was_successful = 1 GROUP BY user_id The grouping happens first , and the aggregate calculati…

## What’s new and why it matters
How Grouping happens under the hood Let's take this example: SELECT user_id , SUM ( amount ) as balance from transactions where was_successful = 1 GROUP BY user_id The grouping happens first , and the aggregate calculation happens second . Here is how the SQL engine processes this conceptually step-by-step: 1. Filter rows ( FROM and WHERE ) The engine grabs the transactions table and discards any row where was_successful is not 1 (or true ). At this stage, you just have a filtered list of individual transaction rows. 2. Form the buckets ( GROUP BY ) Next, the engine organizes the remaining row…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/awji/sql-groupby-and-aggregates-3e9h

## Related notes
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-10-12-where-vs-having-in-sql-a-simple-way-to-understand-the-difference]]
- [[2026-08-28-sql-execution-order-internals-why-where-fails-on-aliases-but-order-by-succeeds]]
- [[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]
- [[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]
- [[2026-05-13-sql-execution-order-write-queries-that-think-like-the-database]]
