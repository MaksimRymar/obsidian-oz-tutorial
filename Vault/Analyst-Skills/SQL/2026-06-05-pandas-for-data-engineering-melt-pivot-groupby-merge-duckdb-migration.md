---
title: 'Pandas for Data Engineering: melt, pivot, groupby, merge & DuckDB Migration'
date: '2026-06-05'
source: https://dev.to/gowthampotureddi/pandas-for-data-engineering-melt-pivot-groupby-merge-duckdb-migration-16d9
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#library'
- '#presentations'
- '#python'
- '#sql'
- '#support-analytics'
- '#tableau'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]'
- '[[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
status: unread
---

> **TL;DR:** pandas melt is the single most useful reshape primitive in a data engineer's toolbox — it is the "untidy wide table → tidy long table" transformation that lets every downstream groupby , merge , and SQL UNPIVOT actually…

## What’s new and why it matters
pandas melt is the single most useful reshape primitive in a data engineer's toolbox — it is the "untidy wide table → tidy long table" transformation that lets every downstream groupby , merge , and SQL UNPIVOT actually work. Five other primitives — pivot_table , stack / unstack , groupby.agg / transform / apply , and merge (with its six join types plus the underrated merge_asof ) — round out the pandas data engineering core, and duckdb pandas is the 2026 escape hatch for when your dataframe stops fitting in RAM. This guide walks the five primitives that show up most in production Python ETL —…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/pandas-for-data-engineering-melt-pivot-groupby-merge-duckdb-migration-16d9

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]
- [[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
