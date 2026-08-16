---
title: Why Your Fully-Cached Database Query Still Takes 5.6 Seconds
date: '2026-08-16'
source: https://medium.com/@tech_61992/why-your-fully-cached-database-query-still-takes-5-6-seconds-64560029f45c?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-05-07-sql-indexing-internals-what-no-one-tells-you-until-your-query-takes-40-seconds]]'
- '[[2026-08-05-black-box-to-blueprint-why-indexes-exist]]'
- '[[2026-05-29-part-11-indexes-and-performance]]'
- '[[2026-06-29-the-first-lesson-my-manager-taught-me-had-nothing-to-do-with-sql]]'
- '[[2026-07-10-partitioning-a-500-million-row-table-in-postgresql-with-zero-downtime]]'
- '[[2026-04-05-the-query-that-took-14-hours-in-our-old-database-ran-in-11-seconds-in-snowflake]]'
status: unread
---

> **TL;DR:** A product page query on a 14 MB table was taking 5.6 seconds. Nothing was locked, nothing was on disk, and the table had eight indexes… Continue reading on Medium »

## What’s new and why it matters
A product page query on a 14 MB table was taking 5.6 seconds. Nothing was locked, nothing was on disk, and the table had eight indexes… Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/@tech_61992/why-your-fully-cached-database-query-still-takes-5-6-seconds-64560029f45c?source=rss------sql-5

## Related notes
- [[2026-05-07-sql-indexing-internals-what-no-one-tells-you-until-your-query-takes-40-seconds]]
- [[2026-08-05-black-box-to-blueprint-why-indexes-exist]]
- [[2026-05-29-part-11-indexes-and-performance]]
- [[2026-06-29-the-first-lesson-my-manager-taught-me-had-nothing-to-do-with-sql]]
- [[2026-07-10-partitioning-a-500-million-row-table-in-postgresql-with-zero-downtime]]
- [[2026-04-05-the-query-that-took-14-hours-in-our-old-database-ran-in-11-seconds-in-snowflake]]
