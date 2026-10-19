---
title: SQL Window Functions, Joins, CTEs and Subqueries Explained with a Hospital
  Dataset
date: '2026-10-19'
source: https://dev.to/asma_salah_2e2a6926b57a2e/sql-window-functions-joins-ctes-and-subqueries-explained-with-a-hospital-dataset-58j
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-10-18-a-practical-guide-to-sql-joins-subqueries-ctes-and-window-functions]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-10-17-joins-in-sql]]'
status: unread
---

> **TL;DR:** What this article covers Window functions ( ROW_NUMBER , RANK , LAG , NTILE , running totals and frames) Joins ( INNER , LEFT , RIGHT , FULL OUTER , CROSS , SELF ) Common table expressions (basic, multiple, recursive) Su…

## What’s new and why it matters
What this article covers Window functions ( ROW_NUMBER , RANK , LAG , NTILE , running totals and frames) Joins ( INNER , LEFT , RIGHT , FULL OUTER , CROSS , SELF ) Common table expressions (basic, multiple, recursive) Subqueries (scalar, correlated, IN , EXISTS , ANY , ALL ) The dataset The database lives in a schema called morning and follows a star-style design. One fact table, visits , connects to dimension tables: visits : one row per hospital visit (date, bill, admission type, stay length, triage level, satisfaction score) patients , doctors , department , wards , diagnosis , procedures :…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/asma_salah_2e2a6926b57a2e/sql-window-functions-joins-ctes-and-subqueries-explained-with-a-hospital-dataset-58j

## Related notes
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-10-18-a-practical-guide-to-sql-joins-subqueries-ctes-and-window-functions]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-10-17-joins-in-sql]]
