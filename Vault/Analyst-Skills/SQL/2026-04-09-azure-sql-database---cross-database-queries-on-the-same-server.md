---
title: Azure SQL Database - Cross-Database Queries on the Same Server
date: '2026-04-09'
source: https://dev.to/andrewelans/azure-sql-database-cross-database-queries-on-the-same-server-2b9j
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-02-28-clustered-vs-non-clustered-index-in-sqlcomplete-guide-with-examples]]'
- '[[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]'
- '[[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]'
- '[[2026-04-09-postgresql-foreign-data-wrappers-cross-database-queries-explained]]'
- '[[2026-03-01-sql-joins]]'
- '[[2026-03-14-demystifying-sql-joins-window-functions]]'
status: unread
---

> **TL;DR:** If you have two databases on the same Azure SQL logical server and try a three-part name query like you would on-prem SQL Server - it won't work. Here's how to set it up using Elastic Query. Prerequisites Elastic Query o…

## What’s new and why it matters
If you have two databases on the same Azure SQL logical server and try a three-part name query like you would on-prem SQL Server - it won't work. Here's how to set it up using Elastic Query. Prerequisites Elastic Query only supports SQL authentication - Entra ID (AAD) and Managed Identity are not supported for cross-database credentials. If your server has Microsoft Entra ID only authentication enabled, you'll need to disable it: Azure Portal → SQL Server → Settings → Microsoft Entra ID → uncheck Support only Microsoft Entra authentication for this server . This is a server-level setting that…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/andrewelans/azure-sql-database-cross-database-queries-on-the-same-server-2b9j

## Related notes
- [[2026-02-28-clustered-vs-non-clustered-index-in-sqlcomplete-guide-with-examples]]
- [[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]
- [[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]
- [[2026-04-09-postgresql-foreign-data-wrappers-cross-database-queries-explained]]
- [[2026-03-01-sql-joins]]
- [[2026-03-14-demystifying-sql-joins-window-functions]]
