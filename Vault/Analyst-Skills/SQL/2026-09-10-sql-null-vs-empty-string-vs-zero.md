---
title: SQL NULL vs empty string vs zero
date: '2026-09-10'
source: https://dev.to/nexus_vibes/sql-null-vs-empty-string-vs-zero-3jlo
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-09-06-when-sql-has-nothing-to-say-understanding-nulls]]'
- '[[2026-07-27-sql-select-null-a-complete-guide-to-handling-missing-data-in-sql]]'
- '[[2026-07-02-dont-use-not-in]]'
- '[[2026-04-21-two-sql-null-traps-missing-join-rows-and-unique-constraints-that-do-nothing]]'
- '[[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
status: unread
---

> **TL;DR:** NULL Is Not Zero, Not an Empty String, and Not False This single idea explains most NULL-related surprises: NULL represents an unknown or missing value — not zero, not an empty string, not boolean false. It's a placehold…

## What’s new and why it matters
NULL Is Not Zero, Not an Empty String, and Not False This single idea explains most NULL-related surprises: NULL represents an unknown or missing value — not zero, not an empty string, not boolean false. It's a placeholder meaning "there is no value here to compare," and that has real consequences for how comparisons behave. SELECT * FROM Employees WHERE salary = NULL ; -- returns ZERO rows, always, for every row in the table SELECT * FROM Employees WHERE salary IS NULL ; -- correctly returns Dave SELECT * FROM Employees WHERE salary IS NOT NULL ; -- everyone except Dave salary = NULL doesn't…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/nexus_vibes/sql-null-vs-empty-string-vs-zero-3jlo

## Related notes
- [[2026-09-06-when-sql-has-nothing-to-say-understanding-nulls]]
- [[2026-07-27-sql-select-null-a-complete-guide-to-handling-missing-data-in-sql]]
- [[2026-07-02-dont-use-not-in]]
- [[2026-04-21-two-sql-null-traps-missing-join-rows-and-unique-constraints-that-do-nothing]]
- [[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
