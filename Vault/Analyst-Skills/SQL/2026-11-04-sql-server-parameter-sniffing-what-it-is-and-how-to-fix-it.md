---
title: 'SQL Server Parameter Sniffing: What It Is and How to Fix It'
date: '2026-11-04'
source: https://dev.to/lingamsuyambu/sql-server-parameter-sniffing-what-it-is-and-how-to-fix-it-574j
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-10-10-sql-indexes-explained-for-people-who-just-got-yelled-at-by-a-slow-dashboard]]'
- '[[2026-09-23-oracle-indexes-when-they-help-when-they-hurt-and-how-to-tell]]'
- '[[2026-07-13-sql-server-parameter-sniffing-detecting-unstable-execution-plans-and-choosing-the-right-fix]]'
- '[[2026-10-29-sargable-queries-in-sql-server-why-functions-in-where-slow-you-down]]'
status: unread
---

> **TL;DR:** Originally published at SQL & Cloud Lab . "The stored procedure was fast yesterday and slow today, and nothing changed." If you have heard that sentence, you have probably met parameter sniffing . It is one of the most c…

## What’s new and why it matters
Originally published at SQL & Cloud Lab . "The stored procedure was fast yesterday and slow today, and nothing changed." If you have heard that sentence, you have probably met parameter sniffing . It is one of the most common causes of sudden, unexplained slowdowns in SQL Server, and once you understand it, it becomes easy to diagnose. What parameter sniffing is When a parameterised query or stored procedure runs for the first time, SQL Server looks at ("sniffs") the parameter values, builds an execution plan that is optimal for those values, and caches it. Every later call reuses that plan, w…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/lingamsuyambu/sql-server-parameter-sniffing-what-it-is-and-how-to-fix-it-574j

## Related notes
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-10-10-sql-indexes-explained-for-people-who-just-got-yelled-at-by-a-slow-dashboard]]
- [[2026-09-23-oracle-indexes-when-they-help-when-they-hurt-and-how-to-tell]]
- [[2026-07-13-sql-server-parameter-sniffing-detecting-unstable-execution-plans-and-choosing-the-right-fix]]
- [[2026-10-29-sargable-queries-in-sql-server-why-functions-in-where-slow-you-down]]
