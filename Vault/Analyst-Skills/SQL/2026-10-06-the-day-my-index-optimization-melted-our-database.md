---
title: The Day My "Index Optimization" Melted Our Database 🔥
date: '2026-10-06'
source: https://dev.to/rss_holmes/the-day-my-index-optimization-melted-our-database-2551
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-29-why-your-sql-server-database-is-slow-and-how-to-fix-it]]'
- '[[2026-07-02-dont-use-not-in]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** It was a regular Monday morning. I was sipping my chai ☕, scanning through our monitoring dashboards, when I noticed something that had been bugging me for weeks - a SQL condition that was obviously wrong. Many queries i…

## What’s new and why it matters
It was a regular Monday morning. I was sipping my chai ☕, scanning through our monitoring dashboards, when I noticed something that had been bugging me for weeks - a SQL condition that was obviously wrong. Many queries in our multi-tenant SaaS application had this filter: WHERE ( tenant_id = 42 OR tenant_id IS NULL ) AND org_id = 100 AND is_active = 1 AND is_deleted = 0 That “ OR tenant_id IS NULL” was sitting in every single query for a lot of tables. And I knew from years of database experience that OR conditions are index killers. Every DBA will tell you: “An OR with IS NULL prevents MySQL…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rss_holmes/the-day-my-index-optimization-melted-our-database-2551

## Related notes
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-29-why-your-sql-server-database-is-slow-and-how-to-fix-it]]
- [[2026-07-02-dont-use-not-in]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
