---
title: My SQL JOIN Ran Perfectly and Doubled the Refunds
date: '2026-10-28'
source: https://dev.to/shadowdevil07/my-sql-join-ran-perfectly-and-doubled-the-refunds-1700
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
status: unread
---

> **TL;DR:** The SQL query ran without errors. The columns looked right. The totals seemed reasonable. Except Ava's refund total was $60. She'd only been refunded $30. No missing data. No syntax error. Nothing obviously wrong with th…

## What’s new and why it matters
The SQL query ran without errors. The columns looked right. The totals seemed reasonable. Except Ava's refund total was $60. She'd only been refunded $30. No missing data. No syntax error. Nothing obviously wrong with the query. SQL had done exactly what the query asked it to do. The problem was that the query wasn't asking the right question. Here's the idea that explains it: A JOIN doesn't guarantee one result row per row in your first table. One row can match multiple rows, and those matches can multiply your results. That might sound harmless until you start calculating totals. Let's repro…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/shadowdevil07/my-sql-join-ran-perfectly-and-doubled-the-refunds-1700

## Related notes
- [[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
