---
title: 'DuckLake vs Iceberg: which table format for a small team'
date: '2026-11-20'
source: https://dev.to/mohammed_arshadansari_f2/ducklake-vs-iceberg-which-table-format-for-a-small-team-2ibc
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]'
- '[[2026-11-13-a-full-table-scan-isnt-always-a-mistake]]'
- '[[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-10-15-see-every-google-ad-a-competitor-runs-from-just-their-domain-curl-python-n8n]]'
status: unread
---

> **TL;DR:** DuckLake vs Iceberg is usually argued on design. Iceberg keeps table metadata as files next to the data. DuckLake keeps it as rows in a SQL database. Both camps have a diagram that proves they are right. I wanted a numbe…

## What’s new and why it matters
DuckLake vs Iceberg is usually argued on design. Iceberg keeps table metadata as files next to the data. DuckLake keeps it as rows in a SQL database. Both camps have a diagram that proves they are right. I wanted a number instead. So I ran the same workload on both: 50 small commits, a delete, a column rename, time travel, then cleanup. I counted every file each one left on disk and timed every commit. Below is what each format cost, and which one I would pick for a team of two to ten people. What is DuckLake? DuckLake is an open table format from the people behind DuckDB. The data is Parquet,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/mohammed_arshadansari_f2/ducklake-vs-iceberg-which-table-format-for-a-small-team-2ibc

## Related notes
- [[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]
- [[2026-11-13-a-full-table-scan-isnt-always-a-mistake]]
- [[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-10-15-see-every-google-ad-a-competitor-runs-from-just-their-domain-curl-python-n8n]]
