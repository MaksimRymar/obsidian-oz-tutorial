---
title: SQL Window Functions Explained
date: '2026-10-01'
source: https://dev.to/sguantai/sql-window-functions-explained-7k0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-09-23-sql--window-functions]]'
- '[[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]'
- '[[2026-09-17-window-functions]]'
- '[[2026-05-30-sql-window-functions-a-practical-guide-to-rownumber-rank-lag-and-lead]]'
- '[[2026-05-29-part-14-window-functions-ninja-mode]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
status: unread
---

> **TL;DR:** When I first learned SQL, GROUP BY felt like all I needed. Then I hit a question it couldn't answer: "Show me every trip, and next to it, that rider's total spend." GROUP BY collapses rows. I wanted to keep every row and…

## What’s new and why it matters
When I first learned SQL, GROUP BY felt like all I needed. Then I hit a question it couldn't answer: "Show me every trip, and next to it, that rider's total spend." GROUP BY collapses rows. I wanted to keep every row and still see an aggregate beside it. That's what window functions are for. In this post we'll use a small taxi company database (a safari schema with trips and drivers tables) to walk through the basics. What is a window function? A window function performs a calculation across a set of rows related to the current row without collapsing them into one. The general shape is: functi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sguantai/sql-window-functions-explained-7k0

## Related notes
- [[2026-09-23-sql--window-functions]]
- [[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]
- [[2026-09-17-window-functions]]
- [[2026-05-30-sql-window-functions-a-practical-guide-to-rownumber-rank-lag-and-lead]]
- [[2026-05-29-part-14-window-functions-ninja-mode]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
