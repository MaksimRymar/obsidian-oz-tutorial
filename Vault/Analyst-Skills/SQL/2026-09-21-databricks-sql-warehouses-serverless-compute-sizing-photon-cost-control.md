---
title: 'Databricks SQL Warehouses & Serverless Compute: Sizing, Photon & Cost Control'
date: '2026-09-21'
source: https://dev.to/gowthampotureddi/databricks-sql-warehouses-serverless-compute-sizing-photon-cost-control-4dbp
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-08-postgres-autovacuum-isnt-keeping-up-diagnosing-bloat-long-transactions-and-wraparound-warnings]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
status: unread
---

> **TL;DR:** databricks sql warehouse is the compute you point a dashboard, a BI tool, or an ad-hoc SQL editor at — a pool of Photon-accelerated nodes that runs SQL against your lakehouse tables and nothing else. It is deliberately n…

## What’s new and why it matters
databricks sql warehouse is the compute you point a dashboard, a BI tool, or an ad-hoc SQL editor at — a pool of Photon-accelerated nodes that runs SQL against your lakehouse tables and nothing else. It is deliberately not the same thing as the general-purpose cluster you attach a notebook to. A warehouse has one job: answer SQL queries fast, share itself across many concurrent users, and get out of the way (and off the bill) the moment nobody is asking. Everything an interviewer will drill you on — types, t-shirt sizing, Photon, caching, scaling, and DBUs — is a consequence of that single-pur…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/databricks-sql-warehouses-serverless-compute-sizing-photon-cost-control-4dbp

## Related notes
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-08-postgres-autovacuum-isnt-keeping-up-diagnosing-bloat-long-transactions-and-wraparound-warnings]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
