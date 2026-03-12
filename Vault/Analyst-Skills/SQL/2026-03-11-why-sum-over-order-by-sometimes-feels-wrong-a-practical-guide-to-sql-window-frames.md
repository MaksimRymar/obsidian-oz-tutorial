---
title: 'Why `SUM() OVER (ORDER BY ...)` Sometimes Feels Wrong: A Practical Guide to
  SQL Window Frames'
date: '2026-03-11'
source: https://dev.to/rozhnev/why-sum-over-order-by-sometimes-feels-wrong-a-practical-guide-to-sql-window-frames-1iga
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-02-sql-joins-and-window-functions-a-developers-guide]]'
- '[[2026-03-01-sql-joins-and-window-functions-a-beginner-friendly-guide]]'
- '[[2026-03-01-understanding-joins-and-window-functions-in-sql]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
status: unread
---

> **TL;DR:** Window functions in SQL can make you feel productive very quickly. You learn PARTITION BY , add ORDER BY , use ROW_NUMBER() , RANK() , and running totals, and it feels like you already have the mental model. That was exa…

## What’s new and why it matters
Window functions in SQL can make you feel productive very quickly. You learn PARTITION BY , add ORDER BY , use ROW_NUMBER() , RANK() , and running totals, and it feels like you already have the mental model. That was exactly my mistake. For a while, I thought I understood window functions well enough because my queries were working and the results looked plausible. The confusion only started later, when I began getting results that were syntactically correct but did not match what I expected logically. A classic example looks like this: SUM ( amount ) OVER ( ORDER BY amount ) You expect a norm…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rozhnev/why-sum-over-order-by-sometimes-feels-wrong-a-practical-guide-to-sql-window-frames-1iga

## Related notes
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-02-sql-joins-and-window-functions-a-developers-guide]]
- [[2026-03-01-sql-joins-and-window-functions-a-beginner-friendly-guide]]
- [[2026-03-01-understanding-joins-and-window-functions-in-sql]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
