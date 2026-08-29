---
title: How to Set Up DuckDB (Run SQL on a CSV With No Import Step)
date: '2026-08-29'
source: https://dev.to/michaelnocito/how-to-set-up-duckdb-run-sql-on-a-csv-with-no-import-step-16nk
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tableau'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-08-21-which-sql-database-should-you-install]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
status: unread
---

> **TL;DR:** By Michael Nocito , data analyst · Published August 8, 2026 By the end of this page you will be running SQL directly against a CSV file on your machine, with no import step, no CREATE TABLE , and no schema written by han…

## What’s new and why it matters
By Michael Nocito , data analyst · Published August 8, 2026 By the end of this page you will be running SQL directly against a CSV file on your machine, with no import step, no CREATE TABLE , and no schema written by hand. DuckDB reads the file where it lies, works out the column types itself, and gives you a normal SQL result. It takes one command to install and about a minute to prove. Here is what to actually do today. Run python -m pip install duckdb , then write a query with your CSV's filename in quotes where the table name would normally go. That is the entire idea, and everything else…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/michaelnocito/how-to-set-up-duckdb-run-sql-on-a-csv-with-no-import-step-16nk

## Related notes
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-12-sql-foundations-start-to-finish]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-08-21-which-sql-database-should-you-install]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
