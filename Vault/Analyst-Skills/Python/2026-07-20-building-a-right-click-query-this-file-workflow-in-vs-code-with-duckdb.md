---
title: Building a right-click 'query this file' workflow in VS Code with DuckDB
date: '2026-07-20'
source: https://dev.to/arunkumarbhat88/building-a-right-click-query-this-file-workflow-in-vs-code-with-duckdb-12ja
domain: Python
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]'
- '[[2026-03-03-sql-joins-and-window-functions-with-case-example]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
status: unread
---

> **TL;DR:** Every data engineer has probably faced this workflow: someone shares a Parquet or CSV file, you need to answer one question, and you end up opening a notebook and writing boilerplate just to inspect it. DuckDB already ma…

## What’s new and why it matters
Every data engineer has probably faced this workflow: someone shares a Parquet or CSV file, you need to answer one question, and you end up opening a notebook and writing boilerplate just to inspect it. DuckDB already makes querying files easy, but I wanted that workflow directly inside VS Code. So I built File SQL , a VS Code extension that turns local and S3 files into queryable SQL tables. How it works Right-click a supported file in the VS Code Explorer and select Open with File SQL . The file is registered as a DuckDB table, and the query editor opens next to it. Write SQL, press Ctrl+Ent…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/arunkumarbhat88/building-a-right-click-query-this-file-workflow-in-vs-code-with-duckdb-12ja

## Related notes
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]
- [[2026-03-03-sql-joins-and-window-functions-with-case-example]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
