---
title: 'When SQL Has Nothing to Say: Handling NULLs'
date: '2026-09-20'
source: https://dev.to/rose_odiwuor/when-sql-has-nothing-to-say-handling-nulls-34jm
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-07-27-sql-select-null-a-complete-guide-to-handling-missing-data-in-sql]]'
- '[[2026-04-10-sql-case-expressions-write-smarter-queries-with-conditional-logic]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-06-19-oracle-ora-00934-error-causes-and-solutions-complete-guide]]'
- '[[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]'
status: unread
---

> **TL;DR:** In Part 1 of the NULL series, we focused on: what NULL represents in a dataset: a value that is missing, unknown, or not applicable how to use is null and is not null to find, update and delete rows with NULL . NULL valu…

## What’s new and why it matters
In Part 1 of the NULL series, we focused on: what NULL represents in a dataset: a value that is missing, unknown, or not applicable how to use is null and is not null to find, update and delete rows with NULL . NULL values can cause unexpected behavior in comparisons and calculations, so it's important to know how to handle them effectively. In Part 2, we'll learn how to: replace NULL with a specified/default value using isnull() and coalesce() replace a value with NULL using nullif() Note: isnull() is database-specific. The examples below use isnull() to demonstrate the function, but PostgreS…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rose_odiwuor/when-sql-has-nothing-to-say-handling-nulls-34jm

## Related notes
- [[2026-07-27-sql-select-null-a-complete-guide-to-handling-missing-data-in-sql]]
- [[2026-04-10-sql-case-expressions-write-smarter-queries-with-conditional-logic]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-06-19-oracle-ora-00934-error-causes-and-solutions-complete-guide]]
- [[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]
