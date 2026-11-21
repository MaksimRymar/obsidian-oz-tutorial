---
title: Hibernate Is Dead Weight — I Replaced It With Plain SQL and Cut Latency 60%
date: '2026-11-21'
source: https://medium.com/@maahisoft20/hibernate-is-dead-weight-i-replaced-it-with-plain-sql-and-cut-latency-60-e4e30c1d1ec5?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-03-25-database-keys-the-backbone-of-every-data-system]]'
- '[[2026-03-10-how-we-got-llms-to-query-our-database-without-leaking-a-single-unauthorized-row]]'
- '[[2026-07-22-postgresql-is-not-just-a-database-it-is-a-tiny-operating-system-for-your-data]]'
- '[[2026-05-05-the-sql-injection-that-still-works-in-2026-and-why-your-app-is-probably-vulnerable]]'
- '[[2026-09-29-the-n1-query-problem-your-api-makes-101-database-queries-to-return-100-rows]]'
- '[[2026-08-28-databend-cluster-key-best-practices-choosing-columns-key-order-and-granularity]]'
status: unread
---

> **TL;DR:** Our slowest endpoint sent 101 SQL queries to the database for a single request. I had written 0 of them. Continue reading on Medium »

## What’s new and why it matters
Our slowest endpoint sent 101 SQL queries to the database for a single request. I had written 0 of them. Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/@maahisoft20/hibernate-is-dead-weight-i-replaced-it-with-plain-sql-and-cut-latency-60-e4e30c1d1ec5?source=rss------sql-5

## Related notes
- [[2026-03-25-database-keys-the-backbone-of-every-data-system]]
- [[2026-03-10-how-we-got-llms-to-query-our-database-without-leaking-a-single-unauthorized-row]]
- [[2026-07-22-postgresql-is-not-just-a-database-it-is-a-tiny-operating-system-for-your-data]]
- [[2026-05-05-the-sql-injection-that-still-works-in-2026-and-why-your-app-is-probably-vulnerable]]
- [[2026-09-29-the-n1-query-problem-your-api-makes-101-database-queries-to-return-100-rows]]
- [[2026-08-28-databend-cluster-key-best-practices-choosing-columns-key-order-and-granularity]]
