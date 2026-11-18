---
title: Why a £24,000 HubSpot pipeline shows £44,000 in Power BI
date: '2026-11-17'
source: https://dev.to/datplan_datapull/why-a-ps24000-hubspot-pipeline-shows-ps44000-in-power-bi-28gf
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tableau'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-11-16-oracle-fusion-rest-api-returns-only-25-invoices-page-through-with-limit-offset-and-hasmore]]'
status: unread
---

> **TL;DR:** The sales team added two calls and a meeting to a deal. The forecast went up even though nobody changed the amount. If you export HubSpot data into Power BI, you can reproduce that symptom with three deals and four activ…

## What’s new and why it matters
The sales team added two calls and a meeting to a deal. The forecast went up even though nobody changed the amount. If you export HubSpot data into Power BI, you can reproduce that symptom with three deals and four activity records. Here is a small test you can run in a fresh SQLite session. The data is invented, the deals are open and all three amounts use one currency. WITH deals ( deal_id , amount ) AS ( VALUES ( 'A' , 10000 ) , ( 'B' , 10000 ) , ( 'C' , 4000 ) ) , activities ( activity_id , deal_id ) AS ( VALUES ( 1 , 'A' ) , ( 2 , 'A' ) , ( 3 , 'A' ) , ( 4 , 'B' ) ) , joined AS ( SELECT d…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datplan_datapull/why-a-ps24000-hubspot-pipeline-shows-ps44000-in-power-bi-28gf

## Related notes
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-11-16-oracle-fusion-rest-api-returns-only-25-invoices-page-through-with-limit-offset-and-hasmore]]
