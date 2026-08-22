---
title: How to Find Duplicate Rows in SQL (and Decide What Counts as One)
date: '2026-08-21'
source: https://dev.to/michaelnocito/how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one-1h9i
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tableau'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
status: unread
---

> **TL;DR:** By Michael Nocito , data analyst · Published August 7, 2026 By the end of this page you can check any table for duplicate rows, list every copy, and mark which one to keep, all with queries you understand. You will also…

## What’s new and why it matters
By Michael Nocito , data analyst · Published August 7, 2026 By the end of this page you can check any table for duplicate rows, list every copy, and mark which one to keep, all with queries you understand. You will also know the step that comes before any query: deciding what "duplicate" means for this table, because two rows can match on everything or on one column, and those are different problems with different fixes. It is about twenty minutes. Here is what to actually do with it. On the next table you are handed, run one comparison before anything else: COUNT(*) against COUNT(DISTINCT key…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/michaelnocito/how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one-1h9i

## Related notes
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-08-12-sql-foundations-start-to-finish]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
