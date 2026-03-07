---
title: C# strings silently kill your SQL Server indexes in Dapper
date: '2026-03-06'
source: https://consultwithgriff.com/dapper-nvarchar-implicit-conversion-performance-trap
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-02-22-the-4000-character-bug-when-sql-server-silently-truncates-your-data]]'
- '[[2026-02-28-the-sql-server-feature-that-cut-our-query-time-by-87-and-we-didnt-write-a-single-line-of-code]]'
- '[[2026-02-28-rag-explained-for-sql-developers-think-of-it-as-select-but-for-meaning]]'
- '[[2026-03-05-100-bounce-rate-0-revenue-an-ai-founders-honest-autopsy]]'
- '[[2026-03-04-bulletproof-data-pipelines-adding-schema-validation-to-nike-scrapers]]'
- '[[2026-02-21-why-your-sql-window-functions-betray-you-in-cloud-ssms-vs-snowflake]]'
status: unread
---

> **TL;DR:** C# strings silently kill your SQL Server indexes in Dapper

## What’s new and why it matters
C# strings silently kill your SQL Server indexes in Dapper

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://consultwithgriff.com/dapper-nvarchar-implicit-conversion-performance-trap

## Related notes
- [[2026-02-22-the-4000-character-bug-when-sql-server-silently-truncates-your-data]]
- [[2026-02-28-the-sql-server-feature-that-cut-our-query-time-by-87-and-we-didnt-write-a-single-line-of-code]]
- [[2026-02-28-rag-explained-for-sql-developers-think-of-it-as-select-but-for-meaning]]
- [[2026-03-05-100-bounce-rate-0-revenue-an-ai-founders-honest-autopsy]]
- [[2026-03-04-bulletproof-data-pipelines-adding-schema-validation-to-nike-scrapers]]
- [[2026-02-21-why-your-sql-window-functions-betray-you-in-cloud-ssms-vs-snowflake]]
