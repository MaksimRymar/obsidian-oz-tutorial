---
title: Designing an Expiring-Points System on an RDBMS (with Benchmarks)
date: '2026-06-12'
source: https://dev.to/matsubo/designing-an-expiring-points-system-on-an-rdbms-with-benchmarks-5hk1
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-05-01-joins-combining-tables-without-losing-your-mind]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-05-04-sql-date-time-functions-a-practical-guide-for-real-world-queries]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
status: unread
---

> **TL;DR:** This is an English rewrite of an article I originally published in Japanese. I've run the design on PostgreSQL 17 in Docker and folded the measured numbers into this post. TL;DR Designing a points system where each grant…

## What’s new and why it matters
This is an English rewrite of an article I originally published in Japanese. I've run the design on PostgreSQL 17 in Docker and folded the measured numbers into this post. TL;DR Designing a points system where each grant expires on its own date (think airline miles, not "12 months since last activity") is far harder than it looks. I compare three relational designs and land on an object-oriented ledger with three tables: deposit , withdraw , and a deposit_withdraw allocation table. That allocation table is the whole trick: it records which grant each spend drew from , which makes exact cancell…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/matsubo/designing-an-expiring-points-system-on-an-rdbms-with-benchmarks-5hk1

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-05-01-joins-combining-tables-without-losing-your-mind]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-05-04-sql-date-time-functions-a-practical-guide-for-real-world-queries]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
