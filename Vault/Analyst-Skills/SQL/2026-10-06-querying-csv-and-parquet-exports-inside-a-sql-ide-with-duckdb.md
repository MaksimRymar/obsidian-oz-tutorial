---
title: Querying CSV and Parquet exports inside a SQL IDE with DuckDB
date: '2026-10-06'
source: https://dev.to/cccadet/querying-csv-and-parquet-exports-inside-a-sql-ide-with-duckdb-4n7b
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-09-zalo-chat-backup-export-messages-and-contacts-to-json-or-csv]]'
- '[[2026-06-19-how-to-embed-a-sql-dashboard-into-your-saas-app-without-building-everything-from-scratch]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-07-20-building-a-right-click-query-this-file-workflow-in-vs-code-with-duckdb]]'
- '[[2026-08-08-how-to-set-up-a-sql-database-for-beginners]]'
- '[[2026-09-29-what-i-added-to-omni-sql-after-v025-local-analytics-s3-and-more]]'
status: unread
---

> **TL;DR:** Someone sends you a CSV export and asks you to investigate it. You need to check duplicates, group records, or compare it with another export. For a one-off analysis, loading it into a database or writing a separate scri…

## What’s new and why it matters
Someone sends you a CSV export and asks you to investigate it. You need to check duplicates, group records, or compare it with another export. For a one-off analysis, loading it into a database or writing a separate script can take longer than the query itself. I'm building omni-sql , an open-source SQL IDE with embedded DuckDB. You can import CSV or Parquet and query it with SQL inside the IDE. A spreadsheet someone sends you fits this workflow when exported as CSV. Joining a file with a database query result Sometimes the file only contains part of what you need. You can also import a databa…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/cccadet/querying-csv-and-parquet-exports-inside-a-sql-ide-with-duckdb-4n7b

## Related notes
- [[2026-08-09-zalo-chat-backup-export-messages-and-contacts-to-json-or-csv]]
- [[2026-06-19-how-to-embed-a-sql-dashboard-into-your-saas-app-without-building-everything-from-scratch]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-07-20-building-a-right-click-query-this-file-workflow-in-vs-code-with-duckdb]]
- [[2026-08-08-how-to-set-up-a-sql-database-for-beginners]]
- [[2026-09-29-what-i-added-to-omni-sql-after-v025-local-analytics-s3-and-more]]
