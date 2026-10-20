---
title: 'SQLazy: Find Strings with 5 or More Consecutive Alphabetical Letters'
date: '2026-10-20'
source: https://dev.to/esproc_spl/sqlazy-find-strings-with-5-or-more-consecutive-alphabetical-letters-1aic
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-09-22-window-functions-vs-aggregate-functions-in-sql-with-examples]]'
- '[[2026-09-28-group-by-aggregate-functions-explained-the-where-vs-having-mistake-almost-everyone-makes]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
status: unread
---

> **TL;DR:** Problem Description Table table_name has a single string field VALUE (max length 50). Find strings that contain at least 5 consecutive letters in ascending alphabetical order. That is: for each string, extract all letter…

## What’s new and why it matters
Problem Description Table table_name has a single string field VALUE (max length 50). Find strings that contain at least 5 consecutive letters in ascending alphabetical order. That is: for each string, extract all letters, check them in original order, find the longest consecutive ascending subsequence (each letter >= previous one), and keep rows where the length >= 5. Non-letter characters must be excluded. Source Data Expected Result Two qualifying strings as examples: ABCDTest: the letters are A, B, C, D, T, e, s, t. The first four A-B-C-D are consecutively ascending. Then T (ASCII 84) is s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/esproc_spl/sqlazy-find-strings-with-5-or-more-consecutive-alphabetical-letters-1aic

## Related notes
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-09-22-window-functions-vs-aggregate-functions-in-sql-with-examples]]
- [[2026-09-28-group-by-aggregate-functions-explained-the-where-vs-having-mistake-almost-everyone-makes]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
