---
title: 'SQL Pattern Series #1: The Presence Pattern'
date: '2026-05-30'
source: https://dev.to/baldwin_apps/sql-pattern-series-1-the-presence-pattern-a5f
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-05-29-the-hard-truth-about-choosing-a-database-and-why-most-projects-get-it-wrong]]'
- '[[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-04-19-subqueries-vs-ctes-choosing-the-right-tool-in-sql]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-10-building-an-ai-tool-that-generates-sql-queries-from-natural-language]]'
status: unread
---

> **TL;DR:** Thinking in terms of existence instead of lists SQL Pattern Series #1 of 21 A collection of practical SQL patterns that help developers recognize common solutions to recurring database problems. What You'll Learn In this…

## What’s new and why it matters
Thinking in terms of existence instead of lists SQL Pattern Series #1 of 21 A collection of practical SQL patterns that help developers recognize common solutions to recurring database problems. What You'll Learn In this article you'll learn: When EXISTS and IN solve the same problem The difference between set membership and existence Why the underlying mental model matters When I typically reach for EXISTS Most SQL developers write a query like this at some point: SELECT c . CustomerID , c . CustomerName FROM Customers c WHERE c . CustomerID IN ( SELECT o . CustomerID FROM Orders o ); And it…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/baldwin_apps/sql-pattern-series-1-the-presence-pattern-a5f

## Related notes
- [[2026-05-29-the-hard-truth-about-choosing-a-database-and-why-most-projects-get-it-wrong]]
- [[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-04-19-subqueries-vs-ctes-choosing-the-right-tool-in-sql]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-10-building-an-ai-tool-that-generates-sql-queries-from-natural-language]]
