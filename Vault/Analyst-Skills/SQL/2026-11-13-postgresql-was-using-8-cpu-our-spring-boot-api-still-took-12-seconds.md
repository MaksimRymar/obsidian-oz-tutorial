---
title: PostgreSQL Was Using 8% CPU. Our Spring Boot API Still Took 12 Seconds
date: '2026-11-13'
source: https://medium.com/javarevisited/postgresql-was-using-8-cpu-our-spring-boot-api-still-took-12-seconds-a457f4038295?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-09-21-our-spring-boot-api-hit-100-cpu-we-blamed-java-postgresql-was-doing-exactly-what-we-asked]]'
- '[[2026-10-02-our-database-wasnt-slow-one-select-was-quietly-costing-us-4800-a-month]]'
- '[[2026-11-13-we-had-zero-database-errors-our-customers-were-still-losing-payments]]'
- '[[2026-11-13-postgresql-had-200-gb-of-free-disk-one-table-still-stopped-accepting-writes]]'
- '[[2026-11-04-postgresql-vs-mongodb-we-built-the-same-backend-twice-one-design-failed-under-load]]'
- '[[2026-11-10-your-spring-boot-api-passed-every-test-postgresql-destroyed-it-in-production]]'
status: unread
---

> **TL;DR:** The database had spare capacity, the indexes were working, and the connection pool wasn’t exhausted. One PostgreSQL query exposed the… Continue reading on Javarevisited »

## What’s new and why it matters
The database had spare capacity, the indexes were working, and the connection pool wasn’t exhausted. One PostgreSQL query exposed the… Continue reading on Javarevisited »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/javarevisited/postgresql-was-using-8-cpu-our-spring-boot-api-still-took-12-seconds-a457f4038295?source=rss------sql-5

## Related notes
- [[2026-09-21-our-spring-boot-api-hit-100-cpu-we-blamed-java-postgresql-was-doing-exactly-what-we-asked]]
- [[2026-10-02-our-database-wasnt-slow-one-select-was-quietly-costing-us-4800-a-month]]
- [[2026-11-13-we-had-zero-database-errors-our-customers-were-still-losing-payments]]
- [[2026-11-13-postgresql-had-200-gb-of-free-disk-one-table-still-stopped-accepting-writes]]
- [[2026-11-04-postgresql-vs-mongodb-we-built-the-same-backend-twice-one-design-failed-under-load]]
- [[2026-11-10-your-spring-boot-api-passed-every-test-postgresql-destroyed-it-in-production]]
