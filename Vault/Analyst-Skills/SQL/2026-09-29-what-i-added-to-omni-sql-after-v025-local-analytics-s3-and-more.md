---
title: 'What I added to omni-sql after v0.2.5: local analytics, S3, and more'
date: '2026-09-29'
source: https://dev.to/cccadet/what-i-added-to-omni-sql-after-v025-local-analytics-s3-and-more-2ef6
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-04-11-master-mysql-views-and-window-functions-advanced-query-optimization-guide]]'
- '[[2026-09-15-sql-subqueries-vs-ctes-which-when-and-why]]'
- '[[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]'
status: unread
---

> **TL;DR:** My first post about omni-sql covered the SQL editor, five database engines, and contextual autocomplete. Since v0.2.5, I've added workflows that let me do more with the data after running a query. The current published r…

## What’s new and why it matters
My first post about omni-sql covered the SQL editor, five database engines, and contextual autocomplete. Since v0.2.5, I've added workflows that let me do more with the data after running a query. The current published release is v0.5.1. Analyze data locally with DuckDB I can send a query from the main editor to Analyze locally , check the SQL before importing it, and load either the complete result or an explicit sample. I can also start with a CSV or Parquet file. Each source becomes a dataset in a local DuckDB workspace, where I can join data from different connections and files with SQL. T…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/cccadet/what-i-added-to-omni-sql-after-v025-local-analytics-s3-and-more-2ef6

## Related notes
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-04-11-master-mysql-views-and-window-functions-advanced-query-optimization-guide]]
- [[2026-09-15-sql-subqueries-vs-ctes-which-when-and-why]]
- [[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]
