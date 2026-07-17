---
title: Checking Data Quality with SQL — a Configurable Framework for Spotting Bad
  Data Generically
date: '2026-07-16'
source: https://dev.to/marcus1968/checking-data-quality-with-sql-a-configurable-framework-for-spotting-bad-data-generically-2cg9
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-05-24-day-4-creating-tables-data-types-null-and-default-constraints]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
status: unread
---

> **TL;DR:** Bad data gives no warning. An age of 200 years, a duplicate customer number, a country code that doesn't exist — in the source system nobody notices. Only when the ETL run tries to push the rows into the strictly modelle…

## What’s new and why it matters
Bad data gives no warning. An age of 200 years, a duplicate customer number, a country code that doesn't exist — in the source system nobody notices. Only when the ETL run tries to push the rows into the strictly modelled target layer does the load break: on a CHECK , on a UNIQUE index, on a foreign key. Checking data quality with SQL means finding exactly those rows beforehand, classifying them by severity and sorting them out deliberately — without a special tool, with a handful of generic SQL routines. The essentials up front: Three generic check routines — a WHERE clause , a uniqueness che…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/marcus1968/checking-data-quality-with-sql-a-configurable-framework-for-spotting-bad-data-generically-2cg9

## Related notes
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-05-24-day-4-creating-tables-data-types-null-and-default-constraints]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
