---
title: T-SQL patterns that break when you migrate SQL Server to PostgreSQL (and where
  they hide in Java/C#)
date: '2026-06-08'
source: https://dev.to/tacioalves/t-sql-patterns-that-break-when-you-migrate-sql-server-to-postgresql-and-where-they-hide-in-javac-jf1
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-04-23-4-open-source-tools-to-build-production-ready-ai-voice-agents]]'
- '[[2026-05-11-five-sql-patterns-ai-agents-get-wrong-and-how-to-fix-them]]'
- '[[2026-05-13-we-built-an-enterprise-integration-stack-for-net-from-scratch-eav-dsl-runtime]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-05-18-from-python-script-to-python-application-the-mindset-shift-beginners-miss]]'
- '[[2026-03-26-finding-the-missing-indexes-your-queries-are-begging-for]]'
status: unread
---

> **TL;DR:** Database migrations look "done" until Monday morning. The stored procedures are converted. The schema is on PostgreSQL. Then the order API fails — because nobody inventoried nativeQuery = true in Spring or FromSqlRaw in…

## What’s new and why it matters
Database migrations look "done" until Monday morning. The stored procedures are converted. The schema is on PostgreSQL. Then the order API fails — because nobody inventoried nativeQuery = true in Spring or FromSqlRaw in EF Core. Here are five patterns that survive the DBA's .sql bundle but break in production: 1. SELECT TOP PostgreSQL uses LIMIT . Easy to miss inside a 40-character @Query string. 2. GETDATE() / SYSDATETIME() Becomes NOW() or CURRENT_TIMESTAMP — but only if you find every occurrence in application code. 3. ISNULL() PostgreSQL prefers COALESCE . Sounds trivial until it's buried…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tacioalves/t-sql-patterns-that-break-when-you-migrate-sql-server-to-postgresql-and-where-they-hide-in-javac-jf1

## Related notes
- [[2026-04-23-4-open-source-tools-to-build-production-ready-ai-voice-agents]]
- [[2026-05-11-five-sql-patterns-ai-agents-get-wrong-and-how-to-fix-them]]
- [[2026-05-13-we-built-an-enterprise-integration-stack-for-net-from-scratch-eav-dsl-runtime]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-05-18-from-python-script-to-python-application-the-mindset-shift-beginners-miss]]
- [[2026-03-26-finding-the-missing-indexes-your-queries-are-begging-for]]
