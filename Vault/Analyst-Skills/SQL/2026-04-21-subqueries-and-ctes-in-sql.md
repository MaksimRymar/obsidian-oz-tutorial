---
title: Subqueries and CTEs in SQL
date: '2026-04-21'
source: https://dev.to/derickmenje/subqueries-and-ctes-in-sql-2e39
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-04-20-subqueries-vs-ctes-and-when-to-use-each]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]'
- '[[2026-04-19-subqueries-vs-ctes-in-sql-a-complete-guide-for-beginners]]'
- '[[2026-04-21-subqueries-and-ctes]]'
status: unread
---

> **TL;DR:** When working with SQL, you eventually run into situations where a single query just isn’t enough. You need to break a problem into parts, compute an intermediate result, and then use that result elsewhere. That’s where s…

## What’s new and why it matters
When working with SQL, you eventually run into situations where a single query just isn’t enough. You need to break a problem into parts, compute an intermediate result, and then use that result elsewhere. That’s where subqueries and Common Table Expressions (CTEs) come in. They solve similar problems, but they do it in slightly different ways, and choosing between them can affect not just performance, but also how readable and maintainable your code is. Let's Dive into it; What is a Subquery? A subquery is a query written inside another query. It produces a result that the outer query depends…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/derickmenje/subqueries-and-ctes-in-sql-2e39

## Related notes
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-04-20-subqueries-vs-ctes-and-when-to-use-each]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-04-21-sql-subquery-and-ctes-common-table-expressions]]
- [[2026-04-19-subqueries-vs-ctes-in-sql-a-complete-guide-for-beginners]]
- [[2026-04-21-subqueries-and-ctes]]
