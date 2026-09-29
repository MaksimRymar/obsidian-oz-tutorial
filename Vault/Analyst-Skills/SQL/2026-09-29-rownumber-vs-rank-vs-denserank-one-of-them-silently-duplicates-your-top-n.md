---
title: 'ROW_NUMBER vs RANK vs DENSE_RANK: one of them silently duplicates your Top-N'
date: '2026-09-29'
source: https://dev.to/sharefun2023/rownumber-vs-rank-vs-denserank-one-of-them-silently-duplicates-your-top-n-i6a
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]'
- '[[2026-09-07-sql-for-beginners-window-functions-vs-group-by]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
status: unread
---

> **TL;DR:** I was reviewing a "top 3 products per category" report last week and found a bug that had been live for months. One category showed four products. Another showed the same product twice. The query used RANK() . It should…

## What’s new and why it matters
I was reviewing a "top 3 products per category" report last week and found a bug that had been live for months. One category showed four products. Another showed the same product twice. The query used RANK() . It should have used ROW_NUMBER() . They look interchangeable in a tutorial and behave completely differently the moment your data has ties. The setup Here is a small sales table with an obvious tie — two products in the same category sold 120 units: CREATE TABLE product_sales ( category text , product text , units_sold int ); INSERT INTO product_sales VALUES ( 'tools' , 'Hammer' , 120 ),…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sharefun2023/rownumber-vs-rank-vs-denserank-one-of-them-silently-duplicates-your-top-n-i6a

## Related notes
- [[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]
- [[2026-09-07-sql-for-beginners-window-functions-vs-group-by]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
