---
title: Building Graph-Based Video Relationship Queries With Apache AGE
date: '2026-06-24'
source: https://dev.to/ahmet_gedik778845/building-graph-based-video-relationship-queries-with-apache-age-2p12
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tableau'
- '#tool'
- '#zendesk'
related:
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
- '[[2026-06-21-product-analytics-with-sql-tracking-what-actually-matters]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-06-08-retention-cohort-analysis-with-plain-sql]]'
- '[[2026-03-18-window-functions-for-call-centre-analytics-a-practical-postgresql-guide]]'
- '[[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]'
status: unread
---

> **TL;DR:** The related-videos query that brought our read replica to its knees At ViralVidVault we track viral video trends across European markets, and the single most expensive query in our stack was never the trend ranking or th…

## What’s new and why it matters
The related-videos query that brought our read replica to its knees At ViralVidVault we track viral video trends across European markets, and the single most expensive query in our stack was never the trend ranking or the GDPR-safe analytics rollups. It was the innocent-looking "show me videos related to this one" panel. Related, for us, means something fuzzy and multi-hop: videos that share a channel, share tags, OR are frequently co-viewed in the same anonymized session window. On SQLite that turned into a pile of self-joins and a WITH RECURSIVE block that walked the co-view table two and th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ahmet_gedik778845/building-graph-based-video-relationship-queries-with-apache-age-2p12

## Related notes
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
- [[2026-06-21-product-analytics-with-sql-tracking-what-actually-matters]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-06-08-retention-cohort-analysis-with-plain-sql]]
- [[2026-03-18-window-functions-for-call-centre-analytics-a-practical-postgresql-guide]]
- [[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]
