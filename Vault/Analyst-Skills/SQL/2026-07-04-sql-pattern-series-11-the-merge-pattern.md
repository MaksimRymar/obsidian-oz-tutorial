---
title: 'SQL Pattern Series #11: The Merge Pattern'
date: '2026-07-04'
source: https://dev.to/baldwin_apps/sql-pattern-series-11-the-merge-pattern-46aj
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-06-30-sql-pattern-series-10-the-hierarchy-pattern]]'
- '[[2026-06-09-sql-pattern-series-4-the-moving-sum-pattern]]'
- '[[2026-06-20-sql-pattern-series-7-the-running-total-pattern]]'
- '[[2026-05-30-sql-pattern-series-1-the-presence-pattern]]'
- '[[2026-06-23-sql-pattern-series-8-the-query-order-pattern]]'
- '[[2026-06-27-sql-pattern-series-9-the-period-over-period-pattern]]'
status: unread
---

> **TL;DR:** Combining result sets without accidentally paying the deduplication tax SQL Pattern Series #11 of 21 A collection of practical SQL patterns that help developers recognize common solutions to recurring database problems.…

## What’s new and why it matters
Combining result sets without accidentally paying the deduplication tax SQL Pattern Series #11 of 21 A collection of practical SQL patterns that help developers recognize common solutions to recurring database problems. What You'll Learn In this article you'll learn: The difference between UNION and UNION ALL Why UNION removes duplicates Why UNION ALL is often faster When to keep duplicates and when to remove them Sometimes you need to combine rows from multiple queries. For example: Show active customers and archived customers together. or: Combine current orders with historical orders. That…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/baldwin_apps/sql-pattern-series-11-the-merge-pattern-46aj

## Related notes
- [[2026-06-30-sql-pattern-series-10-the-hierarchy-pattern]]
- [[2026-06-09-sql-pattern-series-4-the-moving-sum-pattern]]
- [[2026-06-20-sql-pattern-series-7-the-running-total-pattern]]
- [[2026-05-30-sql-pattern-series-1-the-presence-pattern]]
- [[2026-06-23-sql-pattern-series-8-the-query-order-pattern]]
- [[2026-06-27-sql-pattern-series-9-the-period-over-period-pattern]]
