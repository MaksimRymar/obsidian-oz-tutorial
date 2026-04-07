---
title: Writing SQL That Doesn't Come Back to Haunt You
date: '2026-04-07'
source: https://dev.to/whoffagents/writing-sql-that-doesnt-come-back-to-haunt-you-2537
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-03-25-sql-queries-youll-use-every-day-but-nobody-teaches-in-tutorials]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-25-the-only-sql-cheatsheet-youll-ever-need-with-real-examples]]'
- '[[2026-03-09-mastering-sql-joins-and-window-functions-with-real-examples]]'
- '[[2026-03-08-i-built-a-sql-query-builder-in-python---never-hand-write-sql-again]]'
status: unread
---

> **TL;DR:** SQL Is Not Self-Documenting A year from now, you won't remember why you wrote that LEFT JOIN with five conditions. Your colleagues definitely won't. Good SQL is readable SQL. Format Like You Mean It -- Bad: good luck rea…

## What’s new and why it matters
SQL Is Not Self-Documenting A year from now, you won't remember why you wrote that LEFT JOIN with five conditions. Your colleagues definitely won't. Good SQL is readable SQL. Format Like You Mean It -- Bad: good luck reading this at 9 AM SELECT u . id , u . email , COUNT ( o . id ) as order_count , SUM ( o . total ) as lifetime_value FROM users u LEFT JOIN orders o ON o . user_id = u . id WHERE u . created_at > '2024-01-01' AND u . status = 'active' GROUP BY u . id , u . email HAVING COUNT ( o . id ) > 0 ORDER BY lifetime_value DESC LIMIT 100 ; -- Good: obvious structure SELECT u . id , u . em…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/whoffagents/writing-sql-that-doesnt-come-back-to-haunt-you-2537

## Related notes
- [[2026-03-25-sql-queries-youll-use-every-day-but-nobody-teaches-in-tutorials]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-25-the-only-sql-cheatsheet-youll-ever-need-with-real-examples]]
- [[2026-03-09-mastering-sql-joins-and-window-functions-with-real-examples]]
- [[2026-03-08-i-built-a-sql-query-builder-in-python---never-hand-write-sql-again]]
