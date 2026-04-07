---
title: 'PostgreSQL: Transactions, Locks, and Why Serializable Fails'
date: '2026-04-07'
source: https://dev.to/radilov/postgresql-transactions-locks-and-why-serializable-fails-8lm
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-26-create-tables]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-03-08-data-engineers-what-if-your-bigquery-function-could-return-multiple-tables]]'
status: unread
---

> **TL;DR:** If you've ever had queries that suddenly hang, transactions that behave unexpectedly, or an UPDATE from two sessions that produces strange results — this article will help you understand what's happening inside PostgreSQ…

## What’s new and why it matters
If you've ever had queries that suddenly hang, transactions that behave unexpectedly, or an UPDATE from two sessions that produces strange results — this article will help you understand what's happening inside PostgreSQL. We'll cover isolation levels, locks, VACUUM, and demonstrate everything with live SQL examples. A few years ago I gave internal talks on PostgreSQL for my team. Then I spent a long time working with other technologies, and when I recently came back to PostgreSQL, the first thing I did was revisit my own notes to refresh the fundamentals. I figured if it was useful to me, it…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/radilov/postgresql-transactions-locks-and-why-serializable-fails-8lm

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-26-create-tables]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-03-08-data-engineers-what-if-your-bigquery-function-could-return-multiple-tables]]
