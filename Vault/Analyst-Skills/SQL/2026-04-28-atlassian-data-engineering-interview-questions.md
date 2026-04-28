---
title: Atlassian Data Engineering Interview Questions
date: '2026-04-28'
source: https://dev.to/gowthampotureddi/atlassian-data-engineering-interview-questions-nmf
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-03-01-sql-joins]]'
- '[[2026-04-26-uber-data-engineering-interview-questions-prep]]'
status: unread
---

> **TL;DR:** Atlassian data engineering interview questions are the most SQL-window-function-heavy loop covered so far. Six of the curated eight problems are SQL—and five of those six lean directly on OVER (...) clauses for ranking,…

## What’s new and why it matters
Atlassian data engineering interview questions are the most SQL-window-function-heavy loop covered so far. Six of the curated eight problems are SQL—and five of those six lean directly on OVER (...) clauses for ranking, gaps-and-islands runs, frame-based moving averages, and continuous time-series. Expect aggregation for duplicate detection, daily ranking with ROW_NUMBER / RANK , subscription expiry math with date intervals, gaps-and-islands for consecutive runs, 3-day moving averages with ROWS BETWEEN , and continuous-day visitor counts via calendar tables. The two Python problems are classic…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/atlassian-data-engineering-interview-questions-nmf

## Related notes
- [[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-03-01-sql-joins]]
- [[2026-04-26-uber-data-engineering-interview-questions-prep]]
