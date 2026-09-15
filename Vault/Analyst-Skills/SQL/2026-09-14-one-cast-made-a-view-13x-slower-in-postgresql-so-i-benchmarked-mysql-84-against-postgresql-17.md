---
title: One CAST made a view 13x slower in PostgreSQL. So I benchmarked MySQL 8.4 against
  PostgreSQL 17
date: '2026-09-14'
source: https://dev.to/aleksander_frolov/one-cast-made-a-view-13x-slower-in-postgresql-so-i-benchmarked-mysql-84-against-postgresql-17-11en
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-09-05-what-actually-happens-in-a-database-index-and-why-half-of-them-do-nothing]]'
- '[[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]'
- '[[2026-08-10-why-senior-data-engineers-write-sql-differently]]'
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
status: unread
---

> **TL;DR:** At one interview I was asked about VIEWs. I answered honestly: in real projects I had barely run into them; for aggregates it is safer to keep a separate table. One of the interviewers said, “You understand nothing about…

## What’s new and why it matters
At one interview I was asked about VIEWs. I answered honestly: in real projects I had barely run into them; for aggregates it is safer to keep a separate table. One of the interviewers said, “You understand nothing about VIEWs,” and everyone laughed. A lot of time has passed and the number of VIEWs in my code never grew, but the question stayed with me: what if things have changed? New engines have shipped. So I brought up MySQL 8.4.11 and PostgreSQL 17.11, loaded byte-for-byte identical data into both — a million orders, two million line items, 780 thousand payments — and ran the main scenari…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aleksander_frolov/one-cast-made-a-view-13x-slower-in-postgresql-so-i-benchmarked-mysql-84-against-postgresql-17-11en

## Related notes
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-09-05-what-actually-happens-in-a-database-index-and-why-half-of-them-do-nothing]]
- [[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]
- [[2026-08-10-why-senior-data-engineers-write-sql-differently]]
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
