---
title: 'SQL Query Execution Order: Why Your Query Doesn''t Run Top-to-Bottom'
date: '2026-10-11'
source: https://dev.to/neha_christina_1ac8651819/sql-query-execution-order-why-your-query-doesnt-run-top-to-bottom-34pk
domain: SQL
relevance: 🟡
tags:
- '#career'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-06-19-oracle-ora-00934-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-05-13-sql-execution-order-write-queries-that-think-like-the-database]]'
- '[[2026-08-28-sql-execution-order-internals-why-where-fails-on-aliases-but-order-by-succeeds]]'
- '[[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
status: unread
---

> **TL;DR:** If you've ever written a query like this and gotten a baffling error, this post is for you: SELECT customer_id , SUM ( amount ) AS total FROM orders WHERE total > 100 GROUP BY customer_id ; ERROR: column "total" does not…

## What’s new and why it matters
If you've ever written a query like this and gotten a baffling error, this post is for you: SELECT customer_id , SUM ( amount ) AS total FROM orders WHERE total > 100 GROUP BY customer_id ; ERROR: column "total" does not exist Your first reaction is probably "but I just defined total right there in the SELECT." Totally reasonable reaction — and totally wrong assumption about how SQL works under the hood. SQL reads like English, top to bottom: SELECT , FROM , WHERE , GROUP BY , HAVING , ORDER BY . But that's the order you write it in, not the order the database executes it in. Once you internal…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/neha_christina_1ac8651819/sql-query-execution-order-why-your-query-doesnt-run-top-to-bottom-34pk

## Related notes
- [[2026-06-19-oracle-ora-00934-error-causes-and-solutions-complete-guide]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-05-13-sql-execution-order-write-queries-that-think-like-the-database]]
- [[2026-08-28-sql-execution-order-internals-why-where-fails-on-aliases-but-order-by-succeeds]]
- [[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
