---
title: 'greatCircleDistance in ClickHouse: Avoiding Full Table Scans'
date: '2026-04-20'
source: https://dev.to/mohhddhassan/greatcircledistance-in-clickhouse-avoiding-full-table-scans-375p
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]'
- '[[2026-04-10-sql-case-expressions-write-smarter-queries-with-conditional-logic]]'
- '[[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]'
- '[[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]'
- '[[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
status: unread
---

> **TL;DR:** When working with location data, one problem shows up almost immediately: “How do I calculate the distance between two coordinates stored in my database?” At first, it seems like something you’d have to handle outside th…

## What’s new and why it matters
When working with location data, one problem shows up almost immediately: “How do I calculate the distance between two coordinates stored in my database?” At first, it seems like something you’d have to handle outside the database. But if you're using ClickHouse, there’s a built-in function for this. The Right Tool: greatCircleDistance greatCircleDistance ( lat1 , lon1 , lat2 , lon2 ) It calculates the shortest distance between two points on Earth. Example SELECT greatCircleDistance ( 13 . 0827 , 80 . 2707 , 12 . 9716 , 77 . 5946 ) AS distance_meters ; This gives you the distance between Chenn…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mohhddhassan/greatcircledistance-in-clickhouse-avoiding-full-table-scans-375p

## Related notes
- [[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]
- [[2026-04-10-sql-case-expressions-write-smarter-queries-with-conditional-logic]]
- [[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]
- [[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]
- [[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
