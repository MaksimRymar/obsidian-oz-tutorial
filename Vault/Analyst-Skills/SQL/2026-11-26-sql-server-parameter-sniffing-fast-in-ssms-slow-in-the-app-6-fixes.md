---
title: 'SQL Server Parameter Sniffing: Fast in SSMS, Slow in the App (6 Fixes)'
date: '2026-11-26'
source: https://dev.to/lingamsuyambu/sql-server-parameter-sniffing-fast-in-ssms-slow-in-the-app-6-fixes-2e9g
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-11-04-sql-server-parameter-sniffing-what-it-is-and-how-to-fix-it]]'
- '[[2026-11-15-sql-server-query-store-a-practical-beginners-guide]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-11-06-how-to-read-a-sql-server-execution-plan-beginners-guide]]'
- '[[2026-11-23-5-mysql-explain-signals-that-tell-you-exactly-why-your-query-is-slow]]'
- '[[2026-11-20-sql-server-columnstore-indexes-fast-reporting-on-large-tables]]'
status: unread
---

> **TL;DR:** Your stored procedure ran in 1 second yesterday. Today it takes 2 minutes. You copy the call into SSMS and it's fast again. Nothing was deployed. Nine times out of ten, that's parameter sniffing . What actually happens W…

## What’s new and why it matters
Your stored procedure ran in 1 second yesterday. Today it takes 2 minutes. You copy the call into SSMS and it's fast again. Nothing was deployed. Nine times out of ten, that's parameter sniffing . What actually happens When SQL Server compiles a stored procedure (or a parameterized query), it "sniffs" the parameter values of that first call and builds an execution plan that's ideal for those values. The plan goes into the plan cache and every later call reuses it. That's normally a good thing: compiling is expensive. It goes wrong when your data is skewed : CREATE OR ALTER PROCEDURE dbo . GetC…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/lingamsuyambu/sql-server-parameter-sniffing-fast-in-ssms-slow-in-the-app-6-fixes-2e9g

## Related notes
- [[2026-11-04-sql-server-parameter-sniffing-what-it-is-and-how-to-fix-it]]
- [[2026-11-15-sql-server-query-store-a-practical-beginners-guide]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-11-06-how-to-read-a-sql-server-execution-plan-beginners-guide]]
- [[2026-11-23-5-mysql-explain-signals-that-tell-you-exactly-why-your-query-is-slow]]
- [[2026-11-20-sql-server-columnstore-indexes-fast-reporting-on-large-tables]]
