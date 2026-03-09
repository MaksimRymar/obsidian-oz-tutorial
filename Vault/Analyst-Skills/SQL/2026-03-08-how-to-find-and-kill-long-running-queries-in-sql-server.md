---
title: How to Find and Kill Long-Running Queries in SQL Server
date: '2026-03-08'
source: https://dev.to/crw/how-to-find-and-kill-long-running-queries-in-sql-server-5269
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-03-02-dbeaver-postgres-aiven-and-other-sql-shenanigans]]'
- '[[2026-02-23-distributed-locking-in-python]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-02-28-clustered-vs-non-clustered-index-in-sqlcomplete-guide-with-examples]]'
status: unread
---

> **TL;DR:** Anyone who works with SQL Server long enough eventually faces the same problem: a query that just keeps running. Maybe it's blocking other sessions, maybe CPU usage spikes, or maybe an application suddenly becomes slow.…

## What’s new and why it matters
Anyone who works with SQL Server long enough eventually faces the same problem: a query that just keeps running. Maybe it's blocking other sessions, maybe CPU usage spikes, or maybe an application suddenly becomes slow. Long-running queries are one of the most common causes of SQL Server performance issues. In this article, we'll walk through how to: Identify long-running queries Detect blocking sessions Investigate the query details Safely terminate problematic queries Let’s get started. Why Long-Running Queries Are a Problem A query running longer than expected can cause several issues: Bloc…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/crw/how-to-find-and-kill-long-running-queries-in-sql-server-5269

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-03-02-dbeaver-postgres-aiven-and-other-sql-shenanigans]]
- [[2026-02-23-distributed-locking-in-python]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-02-28-clustered-vs-non-clustered-index-in-sqlcomplete-guide-with-examples]]
