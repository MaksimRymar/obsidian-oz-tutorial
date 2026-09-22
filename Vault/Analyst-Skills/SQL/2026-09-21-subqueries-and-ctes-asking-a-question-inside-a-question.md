---
title: 'Subqueries and CTEs: Asking a Question Inside a Question'
date: '2026-09-21'
source: https://dev.to/david_mwandairo_777f888b4/subqueries-and-ctes-asking-a-question-inside-a-question-3lpk
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-09-10-subqueries-ctes-breaking-complex-queries-into-steps]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-09-07-subqueries-ctes]]'
- '[[2026-09-15-sql-joins-explained]]'
status: unread
---

> **TL;DR:** Some questions can't be answered in one pass. "Which hive produced the most honey?" needs the maximum honey figure before it can find the hive that matches it. "Which keepers are above average?" needs the average before…

## What’s new and why it matters
Some questions can't be answered in one pass. "Which hive produced the most honey?" needs the maximum honey figure before it can find the hive that matches it. "Which keepers are above average?" needs the average before it can compare anyone to it. SQL handles this the same way you'd handle it on paper: work out the smaller number first, then use it. That's what a subquery is. A CTE does the same job with a different shape. We'll reuse the beekeeping co-op from the joins article, so the data below should look familiar, with one addition that makes the later examples worth running. The Data, Re…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/david_mwandairo_777f888b4/subqueries-and-ctes-asking-a-question-inside-a-question-3lpk

## Related notes
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-09-10-subqueries-ctes-breaking-complex-queries-into-steps]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-09-07-subqueries-ctes]]
- [[2026-09-15-sql-joins-explained]]
