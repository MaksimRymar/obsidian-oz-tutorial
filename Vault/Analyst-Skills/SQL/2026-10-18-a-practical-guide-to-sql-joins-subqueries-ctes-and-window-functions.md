---
title: A Practical Guide to SQL Joins, Subqueries, CTEs, and Window Functions.
date: '2026-10-18'
source: https://dev.to/esther_njihia/a-practical-guide-to-sql-joins-subqueries-ctes-and-window-functions-4jaj
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-18-sql-concepts---window-functions-joins-common-table-expressions-subqueries]]'
- '[[2026-09-09-sql-joins]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-10-17-joins-in-sql]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]'
status: unread
---

> **TL;DR:** A hospital database rarely stores every useful detail in one table. Patient details may be stored separately from visit records. Doctor, department, ward, diagnosis, and procedure information may live in their own tables…

## What’s new and why it matters
A hospital database rarely stores every useful detail in one table. Patient details may be stored separately from visit records. Doctor, department, ward, diagnosis, and procedure information may live in their own tables. That structure is useful because it reduces duplication, but it also means that answering practical questions requires more than a basic SELECT statement. For example: Which doctors handled the most visits in each department? Which patients have had emergency visits? Which visits had bills above the hospital average? How has each patient’s visit history changed over time? Thi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/esther_njihia/a-practical-guide-to-sql-joins-subqueries-ctes-and-window-functions-4jaj

## Related notes
- [[2026-10-18-sql-concepts---window-functions-joins-common-table-expressions-subqueries]]
- [[2026-09-09-sql-joins]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-10-17-joins-in-sql]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]
