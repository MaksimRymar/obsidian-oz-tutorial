---
title: 'Window Functions vs Aggregate Functions in SQL: A Beginner-Friendly Guide'
date: '2026-09-20'
source: https://dev.to/joseph_mwangi_3ae1f57a132/window-functions-vs-aggregate-functions-in-sql-a-beginner-friendly-guide-i72
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-09-07-sql-for-beginners-window-functions-vs-group-by]]'
- '[[2026-09-17-window-functions]]'
- '[[2026-08-23-sql-window-frames-explained-how-unbounded-preceding-creates-a-running-total]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
status: unread
---

> **TL;DR:** If you have written SQL for more than a week, you have used SUM() , AVG() or COUNT() . They are the bread and butter of reporting. Then one day someone says, "Just use a window function for that" , and suddenly you are s…

## What’s new and why it matters
If you have written SQL for more than a week, you have used SUM() , AVG() or COUNT() . They are the bread and butter of reporting. Then one day someone says, "Just use a window function for that" , and suddenly you are staring at a query with OVER (PARTITION BY ...) in it and wondering what you missed. This article is for you if you are just starting with window functions , or if you already know them and want a quick refresher . We will start with the one idea that separates the two, build both kinds of query side by side, and then explore what window functions can do that aggregates never co…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/joseph_mwangi_3ae1f57a132/window-functions-vs-aggregate-functions-in-sql-a-beginner-friendly-guide-i72

## Related notes
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-09-07-sql-for-beginners-window-functions-vs-group-by]]
- [[2026-09-17-window-functions]]
- [[2026-08-23-sql-window-frames-explained-how-unbounded-preceding-creates-a-running-total]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
