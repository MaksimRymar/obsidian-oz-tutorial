---
title: 'SQL Deep Dive: Subqueries vs. CTEs — Which One Should You Use?'
date: '2026-04-19'
source: https://dev.to/abdiwahab/sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use-51hb
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-04-19-understanding-subqueries-and-ctes-in-sql]]'
- '[[2026-02-25-common-table-expressions]]'
- '[[2026-03-10-joins-window-functions]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-03-01-sql-joins]]'
status: unread
---

> **TL;DR:** When your data questions get harder, you need to perform calculations before you perform your final SELECT . This is where Subqueries and Common Table Expressions (CTEs) come in. 1. What is a Subquery? A subquery is a qu…

## What’s new and why it matters
When your data questions get harder, you need to perform calculations before you perform your final SELECT . This is where Subqueries and Common Table Expressions (CTEs) come in. 1. What is a Subquery? A subquery is a query nested inside another query . It acts as a temporary result set that the outer query uses to filter or calculate data. The 4 Types of Subqueries A. Scalar Subquery Returns exactly one value (one row and one column). Use Case: When you need a single number, like an average or a maximum, to compare against other rows. SELECT first_name , mark FROM exam_results WHERE mark > (…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/abdiwahab/sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use-51hb

## Related notes
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-04-19-understanding-subqueries-and-ctes-in-sql]]
- [[2026-02-25-common-table-expressions]]
- [[2026-03-10-joins-window-functions]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-03-01-sql-joins]]
