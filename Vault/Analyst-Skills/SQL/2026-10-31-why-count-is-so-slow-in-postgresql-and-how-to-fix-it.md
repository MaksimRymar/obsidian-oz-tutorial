---
title: Why COUNT(*) Is So Slow in PostgreSQL (And How to Fix It)
date: '2026-10-31'
source: https://dev.to/ihssmaheel/why-count-is-so-slow-in-postgresql-and-how-to-fix-it-38d4
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-10-03-replacing-deep-offset-pagination-in-d1-rows-read-and-inserts-between-pages]]'
- '[[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]'
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-10-22-why-offset-pagination-is-killing-your-postgresql-queries-and-how-to-implement-keyset-pagination-in-nodejs]]'
- '[[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]'
status: unread
---

> **TL;DR:** You have a users table with 20 million rows. You just want to know how many users exist. Simple, right? SELECT COUNT ( * ) FROM users ; But PostgreSQL takes several seconds to return a single number. Why does counting ro…

## What’s new and why it matters
You have a users table with 20 million rows. You just want to know how many users exist. Simple, right? SELECT COUNT ( * ) FROM users ; But PostgreSQL takes several seconds to return a single number. Why does counting rows take so long? The answer is hidden in how PostgreSQL handles transactions. The Problem: PostgreSQL Can't Just Read a Counter Imagine your database contains 20 million users. While you're counting: One transaction inserts 100 users. Another transaction deletes 50 users. A third transaction hasn't committed its changes yet. So, how many users actually exist? It depends on whic…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ihssmaheel/why-count-is-so-slow-in-postgresql-and-how-to-fix-it-38d4

## Related notes
- [[2026-10-03-replacing-deep-offset-pagination-in-d1-rows-read-and-inserts-between-pages]]
- [[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-10-22-why-offset-pagination-is-killing-your-postgresql-queries-and-how-to-implement-keyset-pagination-in-nodejs]]
- [[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]
