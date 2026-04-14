---
title: Why PostgreSQL Ignores Your Index
date: '2026-04-14'
source: https://dev.to/radilov/why-postgresql-ignores-your-index-4ne
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-04-07-postgresql-transactions-locks-and-why-serializable-fails]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
status: unread
---

> **TL;DR:** You created an index, but the query still does a Seq Scan? The cost in EXPLAIN is some mysterious number and you have no idea how to interpret it? Reads with an index are slower than without one? Let's figure out how Pos…

## What’s new and why it matters
You created an index, but the query still does a Seq Scan? The cost in EXPLAIN is some mysterious number and you have no idea how to interpret it? Reads with an index are slower than without one? Let's figure out how PostgreSQL actually works with indexes — using hands-on examples with 4 million rows. This is Part 2 of a series based on my internal PostgreSQL talks. I spent a long time working with other technologies, and when I came back to PostgreSQL, I revisited my own notes to refresh the fundamentals. The fundamental mechanics of indexes haven't changed, but some useful tools have appeare…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/radilov/why-postgresql-ignores-your-index-4ne

## Related notes
- [[2026-04-07-postgresql-transactions-locks-and-why-serializable-fails]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
