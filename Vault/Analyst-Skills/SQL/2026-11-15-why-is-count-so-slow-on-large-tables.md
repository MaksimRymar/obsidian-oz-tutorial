---
title: Why Is COUNT(*) So Slow on Large Tables?
date: '2026-11-15'
source: https://dev.to/mia_keller_ffd2584c046ecb/why-is-count-so-slow-on-large-tables-3h5k
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
status: unread
---

> **TL;DR:** COUNT(*) feels like it should be instant. The table already exists, an index already exists, so why does Postgres sometimes scan a large table just to answer how many rows it holds? The short answer is that in Postgres,…

## What’s new and why it matters
COUNT(*) feels like it should be instant. The table already exists, an index already exists, so why does Postgres sometimes scan a large table just to answer how many rows it holds? The short answer is that in Postgres, a count is not a stored number. It depends on what the current transaction can see. Why Postgres checks rows instead of reading a stored count Postgres uses MVCC, which means different transactions can see different versions of the same table at the same time. A row inserted by an uncommitted transaction, or deleted but not yet vacuumed, may be visible to one transaction and in…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mia_keller_ffd2584c046ecb/why-is-count-so-slow-on-large-tables-3h5k

## Related notes
- [[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
