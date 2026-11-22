---
title: 'Why Shopify Moved Inventory from Redis to MySQL? : Part 1: the problem and
  the schema'
date: '2026-11-22'
source: https://dev.to/kick933/deep-dive-into-shopify-using-mysql-for-inventory-part-1-4a55
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-11-20-sql-server-columnstore-indexes-fast-reporting-on-large-tables]]'
- '[[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
status: unread
---

> **TL;DR:** Redis is faster than MySQL. So why would Shopify move inventory reservations to MySQL? Shopify Engineering Blog: https://shopify.engineering/scaling-inventory-reservations Read it first. Short answer: Redis and MySQL can…

## What’s new and why it matters
Redis is faster than MySQL. So why would Shopify move inventory reservations to MySQL? Shopify Engineering Blog: https://shopify.engineering/scaling-inventory-reservations Read it first. Short answer: Redis and MySQL can't be updated together atomically, so a crash between the two leaves them out of sync. Problem Let's first list down the problem of Inventory reservation, which Shopify was trying to do better on. All E-commerce apps need to reserve inventory when you make a purchase. Normal purchase flow is Customer adding some X SKUs (items) in varying quantity to my cart. Customer clicks Pay…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kick933/deep-dive-into-shopify-using-mysql-for-inventory-part-1-4a55

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-11-20-sql-server-columnstore-indexes-fast-reporting-on-large-tables]]
- [[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
