---
title: WINDOW FUNCTIONS VS AGGREGATE FUNCTIONS
date: '2026-09-20'
source: https://dev.to/emkoki/window-functions-vs-aggregate-functions-1hoj
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-20-window-functions-vs-aggregate-functions-in-sql-a-beginner-friendly-guide]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-09-07-sql-for-beginners-window-functions-vs-group-by]]'
- '[[2026-05-29-part-14-window-functions-ninja-mode]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
- '[[2026-04-19-stop-collapsing-your-data-why-window-functions-are-a-game-changer]]'
status: unread
---

> **TL;DR:** Window Functions vs. Aggregate Functions: What's the Real Difference? If you've spent any time writing SQL, you've probably reached for an aggregate function like SUM() or COUNT() without thinking twice. But then someone…

## What’s new and why it matters
Window Functions vs. Aggregate Functions: What's the Real Difference? If you've spent any time writing SQL, you've probably reached for an aggregate function like SUM() or COUNT() without thinking twice. But then someone mentions window functions, and suddenly things feel confusing. Both do calculations across rows... so what actually sets them apart? It boils down to one simple idea: aggregates collapse your rows, window functions keep them. Aggregate Functions: The Collapsers Aggregate functions take a bunch of rows and squeeze them down into a single value. The individual rows disappear — y…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/emkoki/window-functions-vs-aggregate-functions-1hoj

## Related notes
- [[2026-09-20-window-functions-vs-aggregate-functions-in-sql-a-beginner-friendly-guide]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-09-07-sql-for-beginners-window-functions-vs-group-by]]
- [[2026-05-29-part-14-window-functions-ninja-mode]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
- [[2026-04-19-stop-collapsing-your-data-why-window-functions-are-a-game-changer]]
