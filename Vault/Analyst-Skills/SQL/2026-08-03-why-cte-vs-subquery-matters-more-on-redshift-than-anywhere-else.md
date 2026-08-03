---
title: Why CTE vs Subquery Matters More on Redshift Than Anywhere Else
date: '2026-08-03'
source: https://dev.to/maithreyan11/why-cte-vs-subquery-matters-more-on-redshift-than-anywhere-else-llm
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]'
- '[[2026-04-26-sql-subqueries-vs-ctes-a-complete-guide-for-data-analysts-published]]'
- '[[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]'
- '[[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]'
status: unread
---

> **TL;DR:** On Snowflake or modern Postgres, CTE vs subquery barely matters for performance. On Redshift, it can matter a lot — and I learned this the hard way. The assumption I carried over I carried an assumption over from Snowfla…

## What’s new and why it matters
On Snowflake or modern Postgres, CTE vs subquery barely matters for performance. On Redshift, it can matter a lot — and I learned this the hard way. The assumption I carried over I carried an assumption over from Snowflake: that the optimizer would treat a CTE and an equivalent subquery the same way. Redshift doesn't play by those rules. Redshift's query planner is derived from an older Postgres lineage, and it historically doesn't inline CTEs the way newer engines do — it can materialize them as a separate step before the outer query even runs. Why this matters on an MPP engine This matters a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/maithreyan11/why-cte-vs-subquery-matters-more-on-redshift-than-anywhere-else-llm

## Related notes
- [[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]
- [[2026-04-26-sql-subqueries-vs-ctes-a-complete-guide-for-data-analysts-published]]
- [[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]
- [[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]
