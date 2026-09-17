---
title: 5 Things AI Cannot Do at PostgreSQL
date: '2026-09-16'
source: https://dev.to/devunionx/5-things-ai-cannot-do-at-postgresql-4kj8
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-08-28-stop-writing-raw-sql-in-your-migrations-most-of-the-time]]'
status: unread
---

> **TL;DR:** AI has become surprisingly good at PostgreSQL. Give it a schema and it can write a query in seconds. Paste an EXPLAIN ANALYZE result into a chat and it may suggest an index or point to an expensive join. That is useful.…

## What’s new and why it matters
AI has become surprisingly good at PostgreSQL. Give it a schema and it can write a query in seconds. Paste an EXPLAIN ANALYZE result into a chat and it may suggest an index or point to an expensive join. That is useful. But there is a difference between writing PostgreSQL code and understanding why the database should work that way . After looking at the practical side of PostgreSQL, five gaps stand out. They are less about syntax and more about context, trade-offs, investigation, responsibility, and situations where there is no obvious answer. 1. AI Cannot Understand Your Business Logic This…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/devunionx/5-things-ai-cannot-do-at-postgresql-4kj8

## Related notes
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-08-28-stop-writing-raw-sql-in-your-migrations-most-of-the-time]]
