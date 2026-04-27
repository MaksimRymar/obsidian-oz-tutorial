---
title: PostgreSQL Subquery and CTE Optimization
date: '2026-04-27'
source: https://medium.com/@philmcc/postgresql-subquery-and-cte-optimization-a4020956171f?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-03-19-your-orm-is-making-3-round-trips-when-postgresql-can-do-it-in-1]]'
- '[[2026-04-23-postgresql-index-usage-and-optimization]]'
- '[[2026-02-24-beyond-the-select-the-sql-mastery-every-data-engineer-needs]]'
- '[[2026-04-06-how-would-you-process-a-large-dataset-that-doesnt-fit-in-memory]]'
- '[[2026-03-07-most-businesses-are-making-decisions-blindly-heres-how-data-science-changes-that]]'
- '[[2026-03-15-when-the-data-doesnt-liebut-nobody-trusts-it]]'
status: unread
---

> **TL;DR:** Every SELECT in PostgreSQL is made of smaller SELECTs, even when it doesn't look that way. WHERE col IN (SELECT ...), WHERE EXISTS (SELECT… Continue reading on Medium »

## What’s new and why it matters
Every SELECT in PostgreSQL is made of smaller SELECTs, even when it doesn't look that way. WHERE col IN (SELECT ...), WHERE EXISTS (SELECT… Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/@philmcc/postgresql-subquery-and-cte-optimization-a4020956171f?source=rss------sql-5

## Related notes
- [[2026-03-19-your-orm-is-making-3-round-trips-when-postgresql-can-do-it-in-1]]
- [[2026-04-23-postgresql-index-usage-and-optimization]]
- [[2026-02-24-beyond-the-select-the-sql-mastery-every-data-engineer-needs]]
- [[2026-04-06-how-would-you-process-a-large-dataset-that-doesnt-fit-in-memory]]
- [[2026-03-07-most-businesses-are-making-decisions-blindly-heres-how-data-science-changes-that]]
- [[2026-03-15-when-the-data-doesnt-liebut-nobody-trusts-it]]
