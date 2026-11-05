---
title: Cloudflare D1’s 50 MB Cap Exposes a Trap in Paginated Search
date: '2026-11-05'
source: https://dev.to/keith_azodeh/cloudflare-d1s-50-mb-cap-exposes-a-trap-in-paginated-search-n24
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-10-03-replacing-deep-offset-pagination-in-d1-rows-read-and-inserts-between-pages]]'
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
status: unread
---

> **TL;DR:** A support archive can show 25 case cards and still pull thousands of work notes to render them. That difference matters on Cloudflare D1. The company announced on October 30 that it would start rejecting query results la…

## What’s new and why it matters
A support archive can show 25 case cards and still pull thousands of work notes to render them. That difference matters on Cloudflare D1. The company announced on October 30 that it would start rejecting query results larger than 50 MB on November 4, 2026. D1’s limits page lists the cap and exempts REST API import and export operations. The first thing to check is what the query returns before your application groups, trims, or renders it. Cloudflare announcement · D1 limits Disclosure: AI generated and fact-checked this article against the linked public sources. Keith has not reviewed it. The…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/keith_azodeh/cloudflare-d1s-50-mb-cap-exposes-a-trap-in-paginated-search-n24

## Related notes
- [[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-10-03-replacing-deep-offset-pagination-in-d1-rows-read-and-inserts-between-pages]]
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
