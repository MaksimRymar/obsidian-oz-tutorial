---
title: SQLazy：Conditional Running Total with Reset
date: '2026-07-27'
source: https://dev.to/esproc_spl/sqlazyconditional-running-total-with-reset-47oo
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-06-20-sql-pattern-series-7-the-running-total-pattern]]'
- '[[2026-07-14-sqlazy-account-based-grouping-with-sequence-number-reset-on-gaps-exceeding-1-hour]]'
- '[[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]'
- '[[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-03-03-sql-joins-and-window-functions-with-case-example]]'
status: unread
---

> **TL;DR:** Problem Description Conditional running total with reset: restart accumulation when logic is 't'. An event table table_t1 records event sequences with three fields: id (sort key), logic (condition flag, values 't' or 'f'…

## What’s new and why it matters
Problem Description Conditional running total with reset: restart accumulation when logic is 't'. An event table table_t1 records event sequences with three fields: id (sort key), logic (condition flag, values 't' or 'f'), and val (numeric value for accumulation). A computed column output needs to be added: when logic equals 't', output is set to 1; otherwise output equals the previous row's output plus the current row's val. This is a conditional running total that resets and restarts accumulation when logic is 't'. Source Data Expected Result id=1 (logic=t): Start of a new segment, output =…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/esproc_spl/sqlazyconditional-running-total-with-reset-47oo

## Related notes
- [[2026-06-20-sql-pattern-series-7-the-running-total-pattern]]
- [[2026-07-14-sqlazy-account-based-grouping-with-sequence-number-reset-on-gaps-exceeding-1-hour]]
- [[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]
- [[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-03-03-sql-joins-and-window-functions-with-case-example]]
