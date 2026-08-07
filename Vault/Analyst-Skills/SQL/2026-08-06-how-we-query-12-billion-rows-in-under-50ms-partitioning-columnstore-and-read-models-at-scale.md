---
title: How We Query 1.2 Billion Rows in Under 50ms — Partitioning, Columnstore, and
  Read Models at Scale
date: '2026-08-06'
source: https://dev.to/kirandeepjassalcrypto/how-we-query-12-billion-rows-in-under-50ms-partitioning-columnstore-and-read-models-at-scale-44jk
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#presentations'
- '#sql'
- '#tool'
related:
- '[[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-07-24-you-dont-need-a-backend-to-store-form-submissions-you-need-a-place-to-ask-how-many]]'
- '[[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]'
- '[[2026-04-22-sql-database-architecture-use-cases-and-monitoring-a-practitioners-guide]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
status: unread
---

> **TL;DR:** Every dashboard load ran a SUM and a COUNT over a 1.2-billion-row table, and each one took just over two seconds. At 110,000 monthly active users hammering those dashboards, our Azure SQL sat at 78% CPU and every campaig…

## What’s new and why it matters
Every dashboard load ran a SUM and a COUNT over a 1.2-billion-row table, and each one took just over two seconds. At 110,000 monthly active users hammering those dashboards, our Azure SQL sat at 78% CPU and every campaign view felt like wading through mud. The fix wasn't a bigger database tier. It was realizing that you never make a billion-row aggregate fast — you make sure you never run it. This is the data-architecture story behind one of the numbers we're proudest of on Mattrx , our multi-tenant marketing-analytics SaaS: KPI query p95 from 2,100ms to 48ms , on a CampaignEvents table that h…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kirandeepjassalcrypto/how-we-query-12-billion-rows-in-under-50ms-partitioning-columnstore-and-read-models-at-scale-44jk

## Related notes
- [[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-07-24-you-dont-need-a-backend-to-store-form-submissions-you-need-a-place-to-ask-how-many]]
- [[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]
- [[2026-04-22-sql-database-architecture-use-cases-and-monitoring-a-practitioners-guide]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
