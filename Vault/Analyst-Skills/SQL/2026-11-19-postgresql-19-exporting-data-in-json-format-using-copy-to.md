---
title: 'PostgreSQL 19: Exporting Data in JSON Format Using COPY TO'
date: '2026-11-19'
source: https://dev.to/vahidusefzadeh/postgresql-19-exporting-data-in-json-format-using-copy-to-a18
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
- '[[2026-11-18-query-a-csv-file-with-sql-without-setting-up-a-database]]'
- '[[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]'
- '[[2026-03-08-data-engineers-what-if-your-bigquery-function-could-return-multiple-tables]]'
- '[[2026-09-15-how-to-extract-tables-from-word-documents-with-python]]'
- '[[2026-07-09-stop-using-offset-for-pagination-switching-to-cursor-based-filtering-for-massive-datasets]]'
status: unread
---

> **TL;DR:** PostgreSQL provides the COPY command to efficiently transfer data between database tables and files or standard input/output streams. Traditionally, COPY supports formats such as TEXT , CSV , and BINARY . However, export…

## What’s new and why it matters
PostgreSQL provides the COPY command to efficiently transfer data between database tables and files or standard input/output streams. Traditionally, COPY supports formats such as TEXT , CSV , and BINARY . However, exporting relational data directly as JSON has often required additional SQL functions, such as row_to_json() or json_agg() . PostgreSQL 19 introduces a new capability: native JSON format support for COPY TO. With this enhancement, we can export table data or query results directly in JSON format without explicitly converting every row using JSON functions. In this article, I will de…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vahidusefzadeh/postgresql-19-exporting-data-in-json-format-using-copy-to-a18

## Related notes
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
- [[2026-11-18-query-a-csv-file-with-sql-without-setting-up-a-database]]
- [[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]
- [[2026-03-08-data-engineers-what-if-your-bigquery-function-could-return-multiple-tables]]
- [[2026-09-15-how-to-extract-tables-from-word-documents-with-python]]
- [[2026-07-09-stop-using-offset-for-pagination-switching-to-cursor-based-filtering-for-massive-datasets]]
