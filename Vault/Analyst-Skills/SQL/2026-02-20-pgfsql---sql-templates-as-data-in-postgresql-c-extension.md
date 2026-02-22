---
title: pg_fsql - SQL templates as data in PostgreSQL (C extension)
date: '2026-02-20'
source: https://dev.to/yurc/pgfsql-sql-templates-as-data-in-postgresql-c-extension-34be
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-02-22-how-to-generate-business-leads-using-google-maps-ids-and-python]]'
- '[[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]'
- '[[2026-02-21-sql-masterclass]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-02-22-md-files-connector-stop-losing-track-of-your-markdown-docs]]'
- '[[2026-02-22-i-built-a-free-self-hosted-snmp-toolkit-now-with-real-time-websocket-push]]'
status: unread
---

> **TL;DR:** I built a PostgreSQL extension that stores SQL queries as composable templates in a regular table. Templates form a dot-path hierarchy — children resolve first and inject into the parent. The idea Queries are data , not…

## What’s new and why it matters
I built a PostgreSQL extension that stores SQL queries as composable templates in a regular table. Templates form a dot-path hierarchy — children resolve first and inject into the parent. The idea Queries are data , not code. You can SELECT, UPDATE, version them. Swap a subtree and the whole query changes. Add a child — it auto-injects into the parent. Quick example INSERT INTO fsql . templates ( path , cmd , body ) VALUES ( 'report' , 'exec' , 'SELECT jsonb_build_object( '' data '' , array_agg(row_to_json(t))) FROM (SELECT {d[cols]} FROM {d[src]} WHERE city = {d[city]!r}) t' ), ( 'report.cols…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yurc/pgfsql-sql-templates-as-data-in-postgresql-c-extension-34be

## Related notes
- [[2026-02-22-how-to-generate-business-leads-using-google-maps-ids-and-python]]
- [[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]
- [[2026-02-21-sql-masterclass]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-02-22-md-files-connector-stop-losing-track-of-your-markdown-docs]]
- [[2026-02-22-i-built-a-free-self-hosted-snmp-toolkit-now-with-real-time-websocket-push]]
