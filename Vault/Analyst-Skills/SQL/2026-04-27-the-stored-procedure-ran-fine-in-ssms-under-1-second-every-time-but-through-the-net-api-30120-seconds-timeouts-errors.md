---
title: The stored procedure ran fine in SSMS — under 1 second, every time. But through
  the .NET API? 30–120 seconds. Timeouts. Errors.
date: '2026-04-27'
source: https://dev.to/ahmedmohamedhussein/the-stored-procedure-ran-fine-in-ssms-under-1-second-every-time-but-through-the-net-api-51e4
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-24-stop-tuning-blind-query-observability-as-the-foundation-for-database-optimization]]'
- '[[2026-03-08-how-to-find-and-kill-long-running-queries-in-sql-server]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-26-finding-the-missing-indexes-your-queries-are-begging-for]]'
- '[[2026-04-24-postgresql-debugging-a-slow-query-and-optimizing-it]]'
- '[[2026-03-09-the-sql-query-that-ruined-my-weekend-and-what-i-built-to-prevent-it]]'
status: unread
---

> **TL;DR:** A production system started timing out. The stored procedure ran fine in SSMS — under 1 second, every time. But through the .NET API? 30–120 seconds. Timeouts. Errors. No CPU spikes. No blocking. No infrastructure alerts…

## What’s new and why it matters
A production system started timing out. The stored procedure ran fine in SSMS — under 1 second, every time. But through the .NET API? 30–120 seconds. Timeouts. Errors. No CPU spikes. No blocking. No infrastructure alerts. The DBA checked. The infrastructure team checked. Nothing. So what changed? ━━━ The investigation ━━━ The timeline had one clue: the degradation started right after routine DBA maintenance — a statistics update and index rebuild. That narrowed it down. The maintenance invalidated the execution plan cache. SQL Server was forced to recompile the procedure on the next call. But…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ahmedmohamedhussein/the-stored-procedure-ran-fine-in-ssms-under-1-second-every-time-but-through-the-net-api-51e4

## Related notes
- [[2026-03-24-stop-tuning-blind-query-observability-as-the-foundation-for-database-optimization]]
- [[2026-03-08-how-to-find-and-kill-long-running-queries-in-sql-server]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-26-finding-the-missing-indexes-your-queries-are-begging-for]]
- [[2026-04-24-postgresql-debugging-a-slow-query-and-optimizing-it]]
- [[2026-03-09-the-sql-query-that-ruined-my-weekend-and-what-i-built-to-prevent-it]]
