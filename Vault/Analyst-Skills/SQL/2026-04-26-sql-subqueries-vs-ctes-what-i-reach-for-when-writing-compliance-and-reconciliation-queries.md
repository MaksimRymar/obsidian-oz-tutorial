---
title: 'SQL Subqueries vs CTEs: What I Reach For When Writing Compliance and Reconciliation
  Queries'
date: '2026-04-26'
source: https://dev.to/muriuki_kahuthu_54/sql-subqueries-vs-ctes-what-i-reach-for-when-writing-compliance-and-reconciliation-queries-2hfa
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-04-21-ctes-subqueries-and-query-optimisation-in-sql]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-04-26-sql-subqueries-vs-ctes-a-complete-guide-for-data-analysts-published]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
status: unread
---

> **TL;DR:** When I started writing SQL against transaction data in fintech and securities brokerage environments, my queries were a mess. Three levels of nesting, the same aggregate computed twice, and a debugging process that invol…

## What’s new and why it matters
When I started writing SQL against transaction data in fintech and securities brokerage environments, my queries were a mess. Three levels of nesting, the same aggregate computed twice, and a debugging process that involved commenting out chunks until something ran. The shift came when I stopped treating subqueries as the only way to compose logic and started picking the right structure for the job. This article walks through: what a subquery actually is the four shapes a subquery can take when a subquery is the correct choice what a Common Table Expression (CTE) is non-recursive and recursive…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/muriuki_kahuthu_54/sql-subqueries-vs-ctes-what-i-reach-for-when-writing-compliance-and-reconciliation-queries-2hfa

## Related notes
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-04-21-ctes-subqueries-and-query-optimisation-in-sql]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-04-26-sql-subqueries-vs-ctes-a-complete-guide-for-data-analysts-published]]
- [[2026-04-21-sql-window-functions-and-ctes]]
