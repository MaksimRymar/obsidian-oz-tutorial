---
title: Why one SQL join returns 5 rows and another returns 12?
date: '2026-07-09'
source: https://dev.to/codewithshreya/sql-joins-without-the-confusion-22b8
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-05-22-sql-joins-interview-questions-inner-left-right-full-self-anti-joins]]'
- '[[2026-03-02-simple-guides-to-table-joins-and-window-functions-in-sql]]'
- '[[2026-05-11-inner-vs-outer-joins-the-two-fundamental-join-types-in-sql]]'
- '[[2026-03-01-a-simple-guide-to-joins-and-window-functions]]'
- '[[2026-03-02-joins-and-window-functions-in-sql]]'
status: unread
---

> **TL;DR:** Why does the same SQL query return five rows with INNER JOIN but twelve with LEFT JOIN? Nothing random happened. The two joins answered different questions. INNER JOIN kept only students with a matching submission. LEFT…

## What’s new and why it matters
Why does the same SQL query return five rows with INNER JOIN but twelve with LEFT JOIN? Nothing random happened. The two joins answered different questions. INNER JOIN kept only students with a matching submission. LEFT JOIN kept every student, then filled missing submission columns with NULL. In this guide, I explain SQL joins using one simple dataset so beginners can clearly understand INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN. By the end, you will be able to predict a join’s output before running it, choose the correct join for a requirement, and avoid a common WHERE clause mis…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/codewithshreya/sql-joins-without-the-confusion-22b8

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-05-22-sql-joins-interview-questions-inner-left-right-full-self-anti-joins]]
- [[2026-03-02-simple-guides-to-table-joins-and-window-functions-in-sql]]
- [[2026-05-11-inner-vs-outer-joins-the-two-fundamental-join-types-in-sql]]
- [[2026-03-01-a-simple-guide-to-joins-and-window-functions]]
- [[2026-03-02-joins-and-window-functions-in-sql]]
