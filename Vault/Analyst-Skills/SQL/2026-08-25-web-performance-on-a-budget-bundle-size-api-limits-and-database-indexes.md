---
title: 'Web Performance on a Budget: Bundle Size, API Limits, and Database Indexes'
date: '2026-08-25'
source: https://dev.to/apeder/web-performance-on-a-budget-bundle-size-api-limits-and-database-indexes-44c6
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#sql'
- '#tableau'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-07-10-build-a-location-aware-serp-check-for-local-seo-experiments]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-13-cohort-retention-analysis-in-sql-the-query-that-tells-you-if-your-product-is-actually-sticky]]'
status: unread
---

> **TL;DR:** The three budgets every web app hits: bundle size, API rate limits, and database index selectivity. Learn the formulas, thresholds, and PR checklist. Introduction Every web app has three budgets, and only one of them liv…

## What’s new and why it matters
The three budgets every web app hits: bundle size, API rate limits, and database index selectivity. Learn the formulas, thresholds, and PR checklist. Introduction Every web app has three budgets, and only one of them lives in your code. The bundle budget lives in the browser — 244 kB gzip is where Lighthouse starts penalizing Time to Interactive. The API budget lives at the provider — 5,000 requests per hour on GitHub, 500 per minute on OpenAI Tier 1, 100 writes per second on Stripe. The database budget lives in the planner — an index with 0.5 selectivity will be ignored and the query will seq…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/apeder/web-performance-on-a-budget-bundle-size-api-limits-and-database-indexes-44c6

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-07-10-build-a-location-aware-serp-check-for-local-seo-experiments]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-13-cohort-retention-analysis-in-sql-the-query-that-tells-you-if-your-product-is-actually-sticky]]
