---
title: I built a free desktop SQL client with a live database health dashboard
date: '2026-03-28'
source: https://dev.to/ashish_srivastava_e6b8ecc/i-built-a-free-desktop-sql-client-with-a-live-database-health-dashboard-16om
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-07-i-built-a-mybatis-style-sql-mapper-for-net-because-ef-core-was-eating-all-our-memory]]'
- '[[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]'
- '[[2026-02-25-how-to-send-telegram-bot-messages-from-a-database-using-sql]]'
- '[[2026-03-18-sql-mastery-the-essential-cheat-sheet-for-data-professionals]]'
- '[[2026-03-08-i-built-a-csv-to-json-converter-in-30-lines-of-python---it-replaced-my-50-saas]]'
- '[[2026-03-11-i-built-a-zero-friction-sqlite-playground-for-my-students]]'
status: unread
---

> **TL;DR:** What is DB Explorer? DB Explorer is a free, open desktop database client built in Java. It supports PostgreSQL, MySQL/MariaDB, Oracle, SQL Server, SQLite, and AWS DynamoDB — all from one tool, with no subscription, no te…

## What’s new and why it matters
What is DB Explorer? DB Explorer is a free, open desktop database client built in Java. It supports PostgreSQL, MySQL/MariaDB, Oracle, SQL Server, SQLite, and AWS DynamoDB — all from one tool, with no subscription, no telemetry, and no account required. What's new in v2.1 The big addition is a live Database Health Dashboard . When you enable it for a connection, it opens a dedicated background JDBC connection (separate from your query connection) and polls your database's own system views on a configurable interval (5–30 seconds). What it shows: Active sessions — pulled from pg_stat_activity ,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashish_srivastava_e6b8ecc/i-built-a-free-desktop-sql-client-with-a-live-database-health-dashboard-16om

## Related notes
- [[2026-03-07-i-built-a-mybatis-style-sql-mapper-for-net-because-ef-core-was-eating-all-our-memory]]
- [[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]
- [[2026-02-25-how-to-send-telegram-bot-messages-from-a-database-using-sql]]
- [[2026-03-18-sql-mastery-the-essential-cheat-sheet-for-data-professionals]]
- [[2026-03-08-i-built-a-csv-to-json-converter-in-30-lines-of-python---it-replaced-my-50-saas]]
- [[2026-03-11-i-built-a-zero-friction-sqlite-playground-for-my-students]]
