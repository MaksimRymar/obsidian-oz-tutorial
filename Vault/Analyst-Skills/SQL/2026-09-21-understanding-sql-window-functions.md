---
title: Understanding SQL Window Functions
date: '2026-09-21'
source: https://dev.to/raphael_njeri_7f67f81f527/understanding-sql-window-functions-359f
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-14-sql-window-functions-the-part-that-took-me-a-while-to-understand]]'
- '[[2026-07-01-10-sql-window-functions-that-separate-junior-from-senior-developers]]'
- '[[2026-09-17-window-functions]]'
- '[[2026-08-17-the-sql-time-machine-how-to-use-lag-lead-firstvalue-lastvalue-to-analyse-business-performance]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
status: unread
---

> **TL;DR:** When I first came across SQL window functions, I found them a bit confusing. I was already comfortable with basic queries, filtering data, using GROUP BY, and calculating things like totals and averages. Window functions…

## What’s new and why it matters
When I first came across SQL window functions, I found them a bit confusing. I was already comfortable with basic queries, filtering data, using GROUP BY, and calculating things like totals and averages. Window functions looked different because they allowed me to perform calculations without losing the individual rows. As I practiced them, I started to understand that window functions are mainly useful when I want to analyse a row while also looking at other related rows. What is a window function? A window function performs a calculation across a set of rows while keeping the original rows i…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/raphael_njeri_7f67f81f527/understanding-sql-window-functions-359f

## Related notes
- [[2026-09-14-sql-window-functions-the-part-that-took-me-a-while-to-understand]]
- [[2026-07-01-10-sql-window-functions-that-separate-junior-from-senior-developers]]
- [[2026-09-17-window-functions]]
- [[2026-08-17-the-sql-time-machine-how-to-use-lag-lead-firstvalue-lastvalue-to-analyse-business-performance]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
