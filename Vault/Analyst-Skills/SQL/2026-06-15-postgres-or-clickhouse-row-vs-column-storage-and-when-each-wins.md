---
title: Postgres or ClickHouse? Row vs Column Storage, and When Each Wins
date: '2026-06-15'
source: https://dev.to/mattia_armas/postgres-or-clickhouse-row-vs-column-storage-and-when-each-wins-14f0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]'
- '[[2026-05-29-part-14-window-functions-ninja-mode]]'
- '[[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]'
- '[[2026-06-13-select-final-and-optimize-final-are-not-the-same-thing]]'
- '[[2026-02-25-partition-and-organize-data-for-performance]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
status: unread
---

> **TL;DR:** PostgreSQL and ClickHouse both speak SQL, both call themselves databases, and both will happily store your data. That surface similarity gets teams into trouble, because under the hood they're built for opposite jobs. Pi…

## What’s new and why it matters
PostgreSQL and ClickHouse both speak SQL, both call themselves databases, and both will happily store your data. That surface similarity gets teams into trouble, because under the hood they're built for opposite jobs. Picking the wrong one doesn't show up on day one — it shows up six months later when a query that should take 50ms takes 40 seconds. The single distinction that explains almost everything is how rows are laid out on disk . Row storage vs column storage PostgreSQL is row-oriented . All the fields of one record sit next to each other on disk: ( 1 , 'error' , 'billing' , '2026-06-15…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mattia_armas/postgres-or-clickhouse-row-vs-column-storage-and-when-each-wins-14f0

## Related notes
- [[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]
- [[2026-05-29-part-14-window-functions-ninja-mode]]
- [[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]
- [[2026-06-13-select-final-and-optimize-final-are-not-the-same-thing]]
- [[2026-02-25-partition-and-organize-data-for-performance]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
