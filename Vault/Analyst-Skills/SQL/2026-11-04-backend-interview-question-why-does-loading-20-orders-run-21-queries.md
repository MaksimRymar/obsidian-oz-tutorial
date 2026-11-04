---
title: 'Backend Interview Question: Why Does Loading 20 Orders Run 21 Queries?'
date: '2026-11-04'
source: https://dev.to/emilywoodsnyc/backend-interview-question-why-does-loading-20-orders-run-21-queries-24pp
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-07-10-build-a-location-aware-serp-check-for-local-seo-experiments]]'
- '[[2026-10-29-it-passed-every-constraint-it-was-still-wrong]]'
- '[[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]'
- '[[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]'
- '[[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]'
status: unread
---

> **TL;DR:** A practical way to spot hidden database calls, fix the read path, and check what the fix costs. You open an orders page with 20 rows. The endpoint returns the right customers, the response looks perfectly normal, and not…

## What’s new and why it matters
A practical way to spot hidden database calls, fix the read path, and check what the fix costs. You open an orders page with 20 rows. The endpoint returns the right customers, the response looks perfectly normal, and nothing throws an error. Then you check the query log and see 21 database calls. One query loaded the orders while the other 20 fetched a customer for each order. That pattern is called an N+1 query problem, and it is easy to miss because the code that triggers it often sits inside a serializer, template, or property rather than next to the query that loaded the list. Let’s trace…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/emilywoodsnyc/backend-interview-question-why-does-loading-20-orders-run-21-queries-24pp

## Related notes
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-07-10-build-a-location-aware-serp-check-for-local-seo-experiments]]
- [[2026-10-29-it-passed-every-constraint-it-was-still-wrong]]
- [[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]
- [[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]
- [[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]
