---
title: SQL Window Functions Clicked When I Stopped Collapsing Rows
date: '2026-11-04'
source: https://dev.to/shadowdevil07/sql-window-functions-clicked-when-i-stopped-collapsing-rows-dn4
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-08-23-sql-window-frames-explained-how-unbounded-preceding-creates-a-running-total]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-10-01-sql-window-functions-explained]]'
- '[[2026-09-21-understanding-sql-window-functions]]'
status: unread
---

> **TL;DR:** I needed a simple SQL report: every order, with the customer's total spending in the next column. My first instinct was GROUP BY . It gave me the right totals but removed every individual order. I could calculate the tot…

## What’s new and why it matters
I needed a simple SQL report: every order, with the customer's total spending in the next column. My first instinct was GROUP BY . It gave me the right totals but removed every individual order. I could calculate the totals separately and join them back to the orders table. That works, but it felt like a lot of work just to put a number next to each row. Then I came across this: SUM ( amount ) OVER ( PARTITION BY customer ) Same totals. All the original orders were still there. That's the idea that made SQL window functions click for me: GROUP BY combines rows. Window functions calculate acros…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/shadowdevil07/sql-window-functions-clicked-when-i-stopped-collapsing-rows-dn4

## Related notes
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-08-23-sql-window-frames-explained-how-unbounded-preceding-creates-a-running-total]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-10-01-sql-window-functions-explained]]
- [[2026-09-21-understanding-sql-window-functions]]
