---
title: How I Fixed a Correlated Subquery That Was Behaving Like an N+1 Problem in
  Production
date: '2026-04-14'
source: https://dev.to/fazghfr/how-i-fixed-a-correlated-subquery-that-was-behaving-like-an-n1-problem-in-production-abn
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]'
- '[[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
status: unread
---

> **TL;DR:** What Happened A user reported seeing no data after an absurdly long loading time in one of the procurement menus. I was maintaining an e-procurement system for a state-owned enterprise subsidiary in the mining sector and…

## What’s new and why it matters
What Happened A user reported seeing no data after an absurdly long loading time in one of the procurement menus. I was maintaining an e-procurement system for a state-owned enterprise subsidiary in the mining sector and this wasn't just a UI glitch. It completely blocked the user's business process. From the network tab, the problematic request was just sitting there with endless pending status, until it hit the server's timeout and resulted in 504, effectively sending no data to the user. The culprit turned out to be a correlated subquery behaving exactly like an N+1 problem: common, easy to…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/fazghfr/how-i-fixed-a-correlated-subquery-that-was-behaving-like-an-n1-problem-in-production-abn

## Related notes
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]
- [[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-08-understanding-group-by-in-sql]]
