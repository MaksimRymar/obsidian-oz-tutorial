---
title: 'How Database Reads Work: Pages, Buffer Pools, and Disk'
date: '2026-06-12'
source: https://dev.to/doogal/how-database-reads-work-pages-buffer-pools-and-disk-1heg
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-05-28-before-sql-we-had-to-tell-computers-everything-then-one-idea-changed-that-forever]]'
- '[[2026-05-09-how-i-built-a-real-time-postgresql-wal-reader-in-go]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-06-10-your-database-is-fast-your-queries-are-slow]]'
status: unread
---

> **TL;DR:** Quick Answer: When you query a database, it rarely reads a single row directly from disk. Instead, it relies on RAM. Databases load fixed-size blocks of data called "pages" (typically 8KB) into a memory cache known as th…

## What’s new and why it matters
Quick Answer: When you query a database, it rarely reads a single row directly from disk. Instead, it relies on RAM. Databases load fixed-size blocks of data called "pages" (typically 8KB) into a memory cache known as the buffer pool. This minimizes slow disk reads and dramatically speeds up follow-on queries. Let's say you need to fetch a specific order from your database. You write a standard query that looks something like this: SELECT * FROM orders WHERE user_id = 6 ; I see a lot of developers naively think the database engine behaves like a simple file reader: it spins up the physical dis…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/doogal/how-database-reads-work-pages-buffer-pools-and-disk-1heg

## Related notes
- [[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-05-28-before-sql-we-had-to-tell-computers-everything-then-one-idea-changed-that-forever]]
- [[2026-05-09-how-i-built-a-real-time-postgresql-wal-reader-in-go]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-06-10-your-database-is-fast-your-queries-are-slow]]
