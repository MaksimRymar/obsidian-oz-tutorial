---
title: SQL Window Functions and CTEs
date: '2026-04-21'
source: https://dev.to/brian_muriithi/sql-window-functions-and-ctes-m4g
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-04-19-stop-collapsing-your-data-why-window-functions-are-a-game-changer]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
status: unread
---

> **TL;DR:** You can do quite a lot with some of the most popular SQL queries such as SELECT, WHERE, and JOIN. But there exists some question that you cannot answer with these queries such as What is each student's mark compared to t…

## What’s new and why it matters
You can do quite a lot with some of the most popular SQL queries such as SELECT, WHERE, and JOIN. But there exists some question that you cannot answer with these queries such as What is each student's mark compared to their own average?" or "Can we rank results without losing any rows?" That is where window functions and CTEs come in. They sound intimidating, but once they click, you will wonder how you ever wrote SQL without them. Part 1 - Window Functions What even is a "window"? Think about a regular GROUP BY query. When you group data, the individual rows collapse into summary rows. You l…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/brian_muriithi/sql-window-functions-and-ctes-m4g

## Related notes
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-04-19-stop-collapsing-your-data-why-window-functions-are-a-game-changer]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-03-08-understanding-group-by-in-sql]]
