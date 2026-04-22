---
title: 'Two SQL NULL Traps: Missing JOIN Rows and UNIQUE Constraints That Do Nothing'
date: '2026-04-21'
source: https://dev.to/recca0120/two-sql-null-traps-missing-join-rows-and-unique-constraints-that-do-nothing-23n5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-26-create-tables]]'
- '[[2026-02-24-countcolumn-vs-count-in-sql-with-inner-left-right-full-join-explained]]'
- '[[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]'
- '[[2026-04-16-sql-joins-explained]]'
status: unread
---

> **TL;DR:** Originally published at recca0120.github.io JOIN two tables on a nullable column and the rows disappear. Insert two NULLs into a UNIQUE column and neither insert fails. Both problems share the same root: SQL defines NULL…

## What’s new and why it matters
Originally published at recca0120.github.io JOIN two tables on a nullable column and the rows disappear. Insert two NULLs into a UNIQUE column and neither insert fails. Both problems share the same root: SQL defines NULL as unknown, and unknown is never equal to anything — including another unknown. What NULL Actually Means In SQL, NULL means "unknown value" — not zero, not empty string, not false. SELECT NULL = NULL ; -- Result: NULL, not TRUE SELECT NULL IS NULL ; -- Result: TRUE NULL = NULL returns NULL , not TRUE . This single rule is why JOINs and UNIQUE constraints behave unexpectedly wi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/recca0120/two-sql-null-traps-missing-join-rows-and-unique-constraints-that-do-nothing-23n5

## Related notes
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-26-create-tables]]
- [[2026-02-24-countcolumn-vs-count-in-sql-with-inner-left-right-full-join-explained]]
- [[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]
- [[2026-04-16-sql-joins-explained]]
