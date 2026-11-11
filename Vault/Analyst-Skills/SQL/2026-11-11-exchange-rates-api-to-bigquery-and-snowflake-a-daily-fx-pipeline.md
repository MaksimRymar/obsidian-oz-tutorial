---
title: 'Exchange Rates API to BigQuery and Snowflake: A Daily FX Pipeline'
date: '2026-11-11'
source: https://dev.to/allratestodaycom/exchange-rates-api-to-bigquery-and-snowflake-a-daily-fx-pipeline-3hle
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-10-22-how-to-get-the-full-wayback-machine-history-of-any-website-no-code-or-python]]'
status: unread
---

> **TL;DR:** Most companies that sell in more than one currency end up with the same task: get daily exchange rates into the warehouse and convert fact tables to one reporting currency. This tutorial builds that pipeline with an exch…

## What’s new and why it matters
Most companies that sell in more than one currency end up with the same task: get daily exchange rates into the warehouse and convert fact tables to one reporting currency. This tutorial builds that pipeline with an exchange rates API, for BigQuery and Snowflake. It covers a daily load job, a staging table and MERGE, a dim_fx_rates table, a dbt model that converts orders with an as-of join, and weekend and holiday handling that an auditor can follow. Decide which rate you are storing There are two kinds of rate, and a warehouse usually needs both. Official rates. The table a central bank or ta…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/allratestodaycom/exchange-rates-api-to-bigquery-and-snowflake-a-daily-fx-pipeline-3hle

## Related notes
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-10-22-how-to-get-the-full-wayback-machine-history-of-any-website-no-code-or-python]]
