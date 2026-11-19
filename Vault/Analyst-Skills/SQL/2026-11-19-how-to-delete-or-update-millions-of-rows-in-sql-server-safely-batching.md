---
title: How to Delete or Update Millions of Rows in SQL Server Safely (Batching)
date: '2026-11-19'
source: https://dev.to/lingamsuyambu/how-to-delete-or-update-millions-of-rows-in-sql-server-safely-batching-1jd6
domain: SQL
relevance: 🔴
tags:
- '#career'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-11-17-sql-server-isolation-levels-explained-with-nolock-and-rcsi]]'
- '[[2026-11-12-sql-server-index-tuning-for-beginners-a-practical-guide]]'
- '[[2026-11-11-how-to-reduce-azure-sql-costs-a-practical-checklist-2026]]'
- '[[2026-10-29-sargable-queries-in-sql-server-why-functions-in-where-slow-you-down]]'
- '[[2026-11-09-how-to-monitor-sql-server-agent-job-failures-alerts-queries-and-best-practices]]'
- '[[2026-11-13-how-to-find-slow-queries-in-sql-server-dmvs-and-query-store]]'
status: unread
---

> **TL;DR:** Originally published at SQL & Cloud Lab . This post was drafted with AI assistance. Delete or update millions of rows in SQL Server without blocking users or filling the log: batching scripts, lock escalation and log tip…

## What’s new and why it matters
Originally published at SQL & Cloud Lab . This post was drafted with AI assistance. Delete or update millions of rows in SQL Server without blocking users or filling the log: batching scripts, lock escalation and log tips. Sooner or later you need to delete five years of audit logs or update a column on 30 million rows. Run it as one statement and you can lock the table for an hour, fill the transaction log, block every user and, if you cancel, wait just as long again for the rollback. The fix is simple: do the work in small batches. Why one big statement hurts One huge transaction: every row…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/lingamsuyambu/how-to-delete-or-update-millions-of-rows-in-sql-server-safely-batching-1jd6

## Related notes
- [[2026-11-17-sql-server-isolation-levels-explained-with-nolock-and-rcsi]]
- [[2026-11-12-sql-server-index-tuning-for-beginners-a-practical-guide]]
- [[2026-11-11-how-to-reduce-azure-sql-costs-a-practical-checklist-2026]]
- [[2026-10-29-sargable-queries-in-sql-server-why-functions-in-where-slow-you-down]]
- [[2026-11-09-how-to-monitor-sql-server-agent-job-failures-alerts-queries-and-best-practices]]
- [[2026-11-13-how-to-find-slow-queries-in-sql-server-dmvs-and-query-store]]
