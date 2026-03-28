---
title: Finding Slow Queries in PostgreSQL (Without Guessing)
date: '2026-03-28'
source: https://dev.to/labeeb-ahmad/finding-slow-queries-in-postgresql-without-guessing-1p5j
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-08-postgresql-query-optimization-10-techniques-that-actually-work]]'
- '[[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-11-why-production-databases-break-normalization-and-why-thats-okay]]'
- '[[2026-03-18-window-functions-for-call-centre-analytics-a-practical-postgresql-guide]]'
status: unread
---

> **TL;DR:** Here’s the quantitative method used by DBAs and tools like pganalyze and AWS Performance Insights. Connect to your database and create the extension: CREATE EXTENSION IF NOT EXISTS pg_stat_statements ; Then tell PostgreS…

## What’s new and why it matters
Here’s the quantitative method used by DBAs and tools like pganalyze and AWS Performance Insights. Connect to your database and create the extension: CREATE EXTENSION IF NOT EXISTS pg_stat_statements ; Then tell PostgreSQL to load it at startup. The easiest way is with ALTER SYSTEM (no need to edit config files): ALTER SYSTEM SET shared_preload_libraries = 'pg_stat_statements' ; Now restart PostgreSQL. If you’re using Docker: docker restart <your-pg-container-name> The extension now tracks every query, grouping similar ones together. Find the Queries That Cost the Most After the restart, run s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/labeeb-ahmad/finding-slow-queries-in-postgresql-without-guessing-1p5j

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-08-postgresql-query-optimization-10-techniques-that-actually-work]]
- [[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-11-why-production-databases-break-normalization-and-why-thats-okay]]
- [[2026-03-18-window-functions-for-call-centre-analytics-a-practical-postgresql-guide]]
