---
title: The Slow Query Hidden Inside Your PL/pgSQL Function
date: '2026-03-21'
source: https://dev.to/philip_mcclarence_2ef9475/the-slow-query-hidden-inside-your-plpgsql-function-41np
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]'
status: unread
---

> **TL;DR:** The Slow Query Hidden Inside Your PL/pgSQL Function You have a function that takes 800ms. You open pg_stat_statements to find the culprit. Nothing over 100ms. You sort by total time, check the top 20 entries — nothing ma…

## What’s new and why it matters
The Slow Query Hidden Inside Your PL/pgSQL Function You have a function that takes 800ms. You open pg_stat_statements to find the culprit. Nothing over 100ms. You sort by total time, check the top 20 entries — nothing matches. The slow query does not appear to exist. But the function is definitely slow, and the application is definitely waiting for it. What gives? The Problem A function call takes 800ms but you cannot find a matching slow query in pg_stat_statements . You search for queries averaging over 100ms, check the top entries by total time, and the function does not appear. This is not…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/philip_mcclarence_2ef9475/the-slow-query-hidden-inside-your-plpgsql-function-41np

## Related notes
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]
