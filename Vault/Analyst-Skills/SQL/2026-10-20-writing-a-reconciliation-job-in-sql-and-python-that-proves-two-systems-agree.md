---
title: Writing a Reconciliation Job in SQL and Python That Proves Two Systems Agree
date: '2026-10-20'
source: https://dev.to/eproxim/writing-a-reconciliation-job-in-sql-and-python-that-proves-two-systems-agree-46oi
domain: SQL
relevance: 🔴
tags:
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-09-30-a-select-that-returned-more-rows-than-its-limit]]'
status: unread
---

> **TL;DR:** On one engagement, operations and finance relied on a SQL Server data warehouse that brought manufacturing and inventory data across from SAP every night – production volumes, inventory movements and material consumption…

## What’s new and why it matters
On one engagement, operations and finance relied on a SQL Server data warehouse that brought manufacturing and inventory data across from SAP every night – production volumes, inventory movements and material consumption for several manufacturing plants. The loads ran in SQL Server Integration Services, and every morning the dashboard showed every job as completed successfully. Then a plant controller noticed something odd. According to the warehouse, raw material consumption had stayed almost perfectly flat for four days in a row, while production volumes had gone up substantially. We picked…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/eproxim/writing-a-reconciliation-job-in-sql-and-python-that-proves-two-systems-agree-46oi

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-09-30-a-select-that-returned-more-rows-than-its-limit]]
