---
title: 'Cost-First or Sample-First: A Debate Over How Agent SQL Loops Handle Unknown
  Table Sizes'
date: '2026-11-05'
source: https://dev.to/dataio_4921/cost-first-or-sample-first-a-debate-over-how-agent-sql-loops-handle-unknown-table-sizes-5286
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tableau'
- '#tool'
related:
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-14-a-read-only-gate-for-model-generated-sql-on-free-compute]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-10-15-the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-attempts]]'
status: unread
---

> **TL;DR:** A drafting agent returns a query that reads fine: three joins, a GROUP BY , a date filter, an ORDER BY on the aggregate. Nothing in the SQL signals danger. The plan underneath it opens with a sequential scan over a table…

## What’s new and why it matters
A drafting agent returns a query that reads fine: three joins, a GROUP BY , a date filter, an ORDER BY on the aggregate. Nothing in the SQL signals danger. The plan underneath it opens with a sequential scan over a table whose row count nobody on the call can state out loud, and the aggregate spills to disk before the first row comes back. That scenario is a constructed reproduction of a common failure mode, not a customer incident and not a logged event from my own past. I use it because the interesting argument is not whether the query was wrong. The argument is what your loop checks before…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dataio_4921/cost-first-or-sample-first-a-debate-over-how-agent-sql-loops-handle-unknown-table-sizes-5286

## Related notes
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-14-a-read-only-gate-for-model-generated-sql-on-free-compute]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-10-15-the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-attempts]]
