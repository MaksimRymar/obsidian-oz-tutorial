---
title: 'Month-over-Month Growth in SQL: LAG, the Growth Formula, and the Traps'
date: '2026-08-21'
source: https://dev.to/michaelnocito/month-over-month-growth-in-sql-lag-the-growth-formula-and-the-traps-5bnp
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#python'
- '#sql'
- '#tableau'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
status: unread
---

> **TL;DR:** By Michael Nocito , data analyst · Published August 7, 2026 By the end of this page you can write a month-over-month growth query and trust its answer. You will know the growth formula and how to say it in a sentence, wh…

## What’s new and why it matters
By Michael Nocito , data analyst · Published August 7, 2026 By the end of this page you can write a month-over-month growth query and trust its answer. You will know the growth formula and how to say it in a sentence, what LAG() actually does, and the three traps that produce wrong percentages without producing an error: integer division, the empty first month, and the missing month. It is about twenty minutes. Here is what to actually do today. Before you trust any growth query you have already written, run one check: count the distinct months in your data and compare that count to the calend…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/michaelnocito/month-over-month-growth-in-sql-lag-the-growth-formula-and-the-traps-5bnp

## Related notes
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-08-12-sql-foundations-start-to-finish]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
