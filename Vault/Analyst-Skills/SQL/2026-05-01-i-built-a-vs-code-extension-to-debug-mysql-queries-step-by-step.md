---
title: I built a VS Code extension to debug MySQL queries step by step
date: '2026-05-01'
source: https://dev.to/ariel_e3e7016e92641fadead/i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step-5gd7
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-03-19-i-built-visual-execution-tools-for-sql-and-python---heres-why]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-04-29-postgresql-subquery-and-cte-optimization]]'
- '[[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]'
- '[[2026-04-22-sql-without-confusion-subqueries-vs-ctes-visual-practical-guide]]'
status: unread
---

> **TL;DR:** I kept running into SQL queries where the final result looked surprising, but it was hard to understand exactly which part of the query changed the data in that way. When a query gets larger, reasoning about it from the…

## What’s new and why it matters
I kept running into SQL queries where the final result looked surprising, but it was hard to understand exactly which part of the query changed the data in that way. When a query gets larger, reasoning about it from the final output alone becomes annoying. I wanted an easier way to see how the data changed as the query moved forward. So I built SQL Visual Debugger, a VS Code extension that lets me step through supported MySQL SELECT queries clause by clause and inspect the intermediate result after each stage. Instead of only seeing the final output, I can see how the rows change throughout th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ariel_e3e7016e92641fadead/i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step-5gd7

## Related notes
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-03-19-i-built-visual-execution-tools-for-sql-and-python---heres-why]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-04-29-postgresql-subquery-and-cte-optimization]]
- [[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]
- [[2026-04-22-sql-without-confusion-subqueries-vs-ctes-visual-practical-guide]]
