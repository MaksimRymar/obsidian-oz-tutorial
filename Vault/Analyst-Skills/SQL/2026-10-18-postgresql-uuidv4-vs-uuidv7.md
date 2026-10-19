---
title: 'PostgreSQL: UUIDv4 vs UUIDv7'
date: '2026-10-18'
source: https://dev.to/regyl/postgresql-uuidv4-vs-uuidv7-1pdf
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]'
- '[[2026-09-27-how-to-catch-a-missing-index-in-a-test-when-your-test-table-has-20-rows]]'
- '[[2026-08-10-why-uuid-v4-is-killing-your-database-indexes-and-how-uuid-v7-fixes-it]]'
- '[[2026-10-03-database-indexes-explained-like-a-book-index]]'
- '[[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
status: unread
---

> **TL;DR:** About a year ago, PostgreSQL 18 delivered native support for UUIDv7. In the article below, I'm gonna deep dive into the impact of UUIDv4 in comparison with the new UUIDv7. TL;DR While on a small amount of data, the amoun…

## What’s new and why it matters
About a year ago, PostgreSQL 18 delivered native support for UUIDv7. In the article below, I'm gonna deep dive into the impact of UUIDv4 in comparison with the new UUIDv7. TL;DR While on a small amount of data, the amount of time needed to insert v4 and v7 is so close; on a larger data set, UUIDv7 surprisingly wins with almost 10x faster results than a common UUIDv4. Meanwhile, the resulting index size is growing linearly: v7 index size is always about a quarter less than v4. LR;WI First, let's define the main difference between UUIDv4 and UUIDv7. As RFC 9562 says: UUIDv7 features a time-order…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/regyl/postgresql-uuidv4-vs-uuidv7-1pdf

## Related notes
- [[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]
- [[2026-09-27-how-to-catch-a-missing-index-in-a-test-when-your-test-table-has-20-rows]]
- [[2026-08-10-why-uuid-v4-is-killing-your-database-indexes-and-how-uuid-v7-fixes-it]]
- [[2026-10-03-database-indexes-explained-like-a-book-index]]
- [[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
