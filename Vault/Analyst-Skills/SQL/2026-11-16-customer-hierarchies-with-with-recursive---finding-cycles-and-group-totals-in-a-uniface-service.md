---
title: Customer hierarchies with WITH RECURSIVE - finding cycles and group totals
  in a Uniface service
date: '2026-11-16'
source: https://dev.to/f345345dfg/customer-hierarchies-with-with-recursive-finding-cycles-and-group-totals-in-a-uniface-service-1kj
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-09-05-how-query-optimizers-work-statistics-cardinality-join-order]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]'
status: unread
---

> **TL;DR:** A customer app built in Uniface 10 lets users link customers: a branch belongs to a company, a subsidiary to a group. The table is simple: CUSTOMER_RELATION (CHILD_ID, PARENT_ID, RELATION_TYPE, ...) Nothing stops a user…

## What’s new and why it matters
A customer app built in Uniface 10 lets users link customers: a branch belongs to a company, a subsidiary to a group. The table is simple: CUSTOMER_RELATION (CHILD_ID, PARENT_ID, RELATION_TYPE, ...) Nothing stops a user from saying "A belongs to B" and later "B belongs to A". Every report that walks up or down the hierarchy then has a problem. This article shows two queries from a check module: one finds such loops, the other adds up revenue per group. Tested with Rocket Uniface 10.4.03 Community Edition (10.4.03.021) on Windows, November 2026. The app uses SQLite through the SLE driver (SQLit…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/f345345dfg/customer-hierarchies-with-with-recursive-finding-cycles-and-group-totals-in-a-uniface-service-1kj

## Related notes
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-09-05-how-query-optimizers-work-statistics-cardinality-join-order]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]
