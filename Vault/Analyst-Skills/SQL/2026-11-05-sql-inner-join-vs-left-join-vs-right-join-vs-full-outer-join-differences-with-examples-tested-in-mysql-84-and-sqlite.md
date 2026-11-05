---
title: 'SQL INNER JOIN vs LEFT JOIN vs RIGHT JOIN vs FULL OUTER JOIN: Differences
  With Examples (Tested in MySQL 8.4 and SQLite)'
date: '2026-11-05'
source: https://dev.to/mfaysaldev/sql-inner-join-vs-left-join-vs-right-join-vs-full-outer-join-differences-with-examples-tested-in-51pb
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-09-09-sql-joins]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
status: unread
---

> **TL;DR:** INNER JOIN returns only the rows that match in both tables. LEFT JOIN returns every row from the left table, with NULL where the right table has no match. RIGHT JOIN is the mirror image: every row from the right table. F…

## What’s new and why it matters
INNER JOIN returns only the rows that match in both tables. LEFT JOIN returns every row from the left table, with NULL where the right table has no match. RIGHT JOIN is the mirror image: every row from the right table. FULL OUTER JOIN returns every row from both tables, matched where possible. On my four customers and five orders, those joins returned 4, 5, 5 and 6 rows. MySQL doesn't support FULL OUTER JOIN at all, so there you combine a LEFT JOIN and a RIGHT JOIN with UNION ALL . Joins are where a lot of SQL bugs hide. A report silently drops customers who never ordered, a WHERE clause quiet…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/mfaysaldev/sql-inner-join-vs-left-join-vs-right-join-vs-full-outer-join-differences-with-examples-tested-in-51pb

## Related notes
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-09-09-sql-joins]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
