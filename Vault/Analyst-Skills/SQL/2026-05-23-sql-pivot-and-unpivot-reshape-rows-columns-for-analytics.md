---
title: 'SQL PIVOT and UNPIVOT: Reshape Rows ↔ Columns for Analytics'
date: '2026-05-23'
source: https://dev.to/gowthampotureddi/sql-pivot-and-unpivot-reshape-rows-columns-for-analytics-1ia4
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tableau'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-05-22-group-by-and-having-in-sql-aggregation-patterns-for-interviews]]'
- '[[2026-05-11-postgresql-sql-data-types-practical-column-type-guide]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-04-10-sql-case-expressions-write-smarter-queries-with-conditional-logic]]'
- '[[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]'
- '[[2026-04-22-sql-database-architecture-use-cases-and-monitoring-a-practitioners-guide]]'
status: unread
---

> **TL;DR:** sql pivot turns long-format rows into wide-format columns: one row per category becomes one column per category, with the aggregate value populating each cell. sql unpivot is the inverse — one column per metric becomes o…

## What’s new and why it matters
sql pivot turns long-format rows into wide-format columns: one row per category becomes one column per category, with the aggregate value populating each cell. sql unpivot is the inverse — one column per metric becomes one row per metric, restoring the long shape that downstream pipelines and BI tools prefer. These two reshape operators answer the bulk of the sql interview questions in the "make this data wide" / "make this data long" cluster, and getting pivot in sql right — especially the dialect divergence between SQL Server's native PIVOT operator and PostgreSQL's SUM(CASE WHEN …) idiom —…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/sql-pivot-and-unpivot-reshape-rows-columns-for-analytics-1ia4

## Related notes
- [[2026-05-22-group-by-and-having-in-sql-aggregation-patterns-for-interviews]]
- [[2026-05-11-postgresql-sql-data-types-practical-column-type-guide]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-04-10-sql-case-expressions-write-smarter-queries-with-conditional-logic]]
- [[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]
- [[2026-04-22-sql-database-architecture-use-cases-and-monitoring-a-practitioners-guide]]
