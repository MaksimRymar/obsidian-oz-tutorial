---
title: 'Performance Engineering: What Is the System Waiting For?'
date: '2026-08-28'
source: https://dev.to/josemariairiarte/performance-engineering-what-is-the-system-waiting-for-483i
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-08-26-sql-taught-me-that-there-is-always-an-easier-way-to-do-things]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-05-04-postgresql-query-rewriting-techniques]]'
status: unread
---

> **TL;DR:** When a request takes five seconds, the obvious question is what to make faster. The more useful question is what, precisely, the system spent those five seconds doing, or waiting to do. The answer may lie in unnecessary…

## What’s new and why it matters
When a request takes five seconds, the obvious question is what to make faster. The more useful question is what, precisely, the system spent those five seconds doing, or waiting to do. The answer may lie in unnecessary database work, excessive data movement, an execution plan, contention, or the costs of concurrency - and different causes require fundamentally different interventions. Performance engineering begins not with optimization, but with establishing causality: understanding what the system is doing before deciding what it should do differently. A request takes five seconds to comple…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/josemariairiarte/performance-engineering-what-is-the-system-waiting-for-483i

## Related notes
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-08-26-sql-taught-me-that-there-is-always-an-easier-way-to-do-things]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-05-18-top-orm-tools-practical-comparison]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-05-04-postgresql-query-rewriting-techniques]]
