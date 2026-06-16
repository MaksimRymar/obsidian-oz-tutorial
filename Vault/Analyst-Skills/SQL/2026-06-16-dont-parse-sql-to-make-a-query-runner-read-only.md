---
title: Don't parse SQL to make a query runner read-only
date: '2026-06-16'
source: https://dev.to/hitoshi1964/dont-parse-sql-to-make-a-query-runner-read-only-b62
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
- '[[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]'
- '[[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]'
- '[[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-05-13-multi-tenant-sql-reporting-how-to-show-each-customer-only-their-own-data]]'
status: unread
---

> **TL;DR:** Say you're building a tool that lets people run ad-hoc SQL against a database, and you want a read-only by default mode — a safety net so a fat-fingered UPDATE doesn't nuke a table. The tempting first instinct is to look…

## What’s new and why it matters
Say you're building a tool that lets people run ad-hoc SQL against a database, and you want a read-only by default mode — a safety net so a fat-fingered UPDATE doesn't nuke a table. The tempting first instinct is to look at the SQL : FORBIDDEN = ( " insert " , " update " , " delete " , " drop " , " truncate " , " alter " , " create " ) def is_read_only ( sql : str ) -> bool : lowered = sql . strip (). lower () return not any ( lowered . startswith ( word ) for word in FORBIDDEN ) Please don't ship this. It's a sieve: WITH x AS ( DELETE FROM orders RETURNING * ) SELECT * FROM x ; -- starts with…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hitoshi1964/dont-parse-sql-to-make-a-query-runner-read-only-b62

## Related notes
- [[2026-05-18-top-orm-tools-practical-comparison]]
- [[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]
- [[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]
- [[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-05-13-multi-tenant-sql-reporting-how-to-show-each-customer-only-their-own-data]]
