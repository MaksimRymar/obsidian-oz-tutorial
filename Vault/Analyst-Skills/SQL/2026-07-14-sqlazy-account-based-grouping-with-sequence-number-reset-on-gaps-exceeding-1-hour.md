---
title: 'SQLazy: Account-based Grouping with Sequence Number Reset on Gaps Exceeding
  1 Hour'
date: '2026-07-14'
source: https://dev.to/esproc_spl/sqlazy-account-based-grouping-with-sequence-number-reset-on-gaps-exceeding-1-hour-4jip
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-04-27-sql-building-blocks-how-subqueries-and-ctes-shape-your-data]]'
- '[[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]'
- '[[2026-07-01-10-sql-window-functions-that-separate-junior-from-senior-developers]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
status: unread
---

> **TL;DR:** Problem description Group by account and reset the sequence number when the time interval between events exceeds 1 hour A table consists of two fields: account_number and dt. Records within each account are ordered by ti…

## What’s new and why it matters
Problem description Group by account and reset the sequence number when the time interval between events exceeds 1 hour A table consists of two fields: account_number and dt. Records within each account are ordered by time, and sequence numbers (Seq) need to be generated according to the following rules: Group records by account and order them by datetime in ascending order. If the interval between the current event time and the previous one exceeds 1 hour, reset the sequence number to 1. Otherwise (the interval ≤ 1 hour), add 1 to the sequence number. Source data: account_number dt 19 2024-04…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/esproc_spl/sqlazy-account-based-grouping-with-sequence-number-reset-on-gaps-exceeding-1-hour-4jip

## Related notes
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-04-27-sql-building-blocks-how-subqueries-and-ctes-shape-your-data]]
- [[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]
- [[2026-07-01-10-sql-window-functions-that-separate-junior-from-senior-developers]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
