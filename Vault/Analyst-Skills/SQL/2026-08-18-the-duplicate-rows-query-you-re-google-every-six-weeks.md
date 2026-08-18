---
title: The duplicate-rows query you re-Google every six weeks
date: '2026-08-18'
source: https://dev.to/omer_hochman/the-duplicate-rows-query-you-re-google-every-six-weeks-39km
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-06-02-5-sql-queries-developers-always-have-to-look-up-with-copy-paste-answers]]'
- '[[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
- '[[2026-08-15-data-modeling-interview-questions-dimensional-normalization-case-studies]]'
status: unread
---

> **TL;DR:** Originally published at nlqdb.com/blog There is a query nobody memorises and everybody needs: find the rows that are duplicated. A customer signed up twice, an import ran twice, a join fanned out and doubled every row. T…

## What’s new and why it matters
Originally published at nlqdb.com/blog There is a query nobody memorises and everybody needs: find the rows that are duplicated. A customer signed up twice, an import ran twice, a join fanned out and doubled every row. The answer has been the same for thirty years — GROUP BY the suspect columns, HAVING COUNT(*) > 1 — and yet if you are not writing SQL daily you look it up every single time , because the shape is just unusual enough to not stick. -- Which emails appear more than once? SELECT email , COUNT ( * ) AS n FROM customers GROUP BY email HAVING COUNT ( * ) > 1 ; The trap is not difficul…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/omer_hochman/the-duplicate-rows-query-you-re-google-every-six-weeks-39km

## Related notes
- [[2026-06-02-5-sql-queries-developers-always-have-to-look-up-with-copy-paste-answers]]
- [[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-08-12-sql-foundations-start-to-finish]]
- [[2026-08-15-data-modeling-interview-questions-dimensional-normalization-case-studies]]
