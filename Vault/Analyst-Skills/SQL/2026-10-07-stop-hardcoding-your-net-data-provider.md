---
title: Stop Hardcoding Your .NET Data Provider
date: '2026-10-07'
source: https://dev.to/pengdows/stop-hardcoding-your-net-data-provider-4jmo
domain: SQL
relevance: 🔴
tags:
- '#best-practice'
- '#feature'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]'
- '[[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-08-08-how-to-set-up-a-sql-database-for-beginners]]'
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
status: unread
---

> **TL;DR:** There is a piece of advice I have been giving for a long time. I first wrote about it around 2010, before .NET Core existed: Do not hardcode your database provider into your application unless the application is delibera…

## What’s new and why it matters
There is a piece of advice I have been giving for a long time. I first wrote about it around 2010, before .NET Core existed: Do not hardcode your database provider into your application unless the application is deliberately a database-specific application. That sounds obvious now. It was less obvious then, when a lot of .NET code looked like this: using var connection = new SqlConnection ( connectionString ); using var command = new SqlCommand ( sql , connection ); There is nothing technically wrong with that code. SqlConnection works. SqlCommand works. If the application is a SQL Server appl…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/pengdows/stop-hardcoding-your-net-data-provider-4jmo

## Related notes
- [[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]
- [[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-08-08-how-to-set-up-a-sql-database-for-beginners]]
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
