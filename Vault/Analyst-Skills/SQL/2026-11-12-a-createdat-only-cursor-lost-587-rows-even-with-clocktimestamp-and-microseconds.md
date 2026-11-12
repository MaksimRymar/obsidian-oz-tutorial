---
title: A created_at-only cursor lost 587 rows, even with clock_timestamp() and microseconds
date: '2026-11-12'
source: https://dev.to/muhammad_adnan_61b78b9816/a-createdat-only-cursor-lost-587-rows-even-with-clocktimestamp-and-microseconds-12d0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-11-09-my-latest-20-issues-query-read-200000-rows-even-with-an-index-on-projectid]]'
- '[[2026-10-24-how-to-find-missing-ids-between-two-lists-and-get-the-sql-for-free]]'
- '[[2026-10-22-why-offset-pagination-is-killing-your-postgresql-queries-and-how-to-implement-keyset-pagination-in-nodejs]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** A reader on one of my Postgres posts asked a fair question: why put id in the pagination index at all? With clock_timestamp() instead of now() , it's hard to create two rows at exactly the same time. So I measured it. Th…

## What’s new and why it matters
A reader on one of my Postgres posts asked a fair question: why put id in the pagination index at all? With clock_timestamp() instead of now() , it's hard to create two rows at exactly the same time. So I measured it. The setup PostgreSQL 16, a 4-vCPU machine. The table is the one every app has: CREATE TABLE concurrent ( id bigserial PRIMARY KEY , created_at timestamptz NOT NULL DEFAULT clock_timestamp ( ) , n int ) ; Then I filled it two ways: Concurrent inserts: pgbench with 16 clients, one INSERT per autocommit transaction, for 20 seconds (about 29,000 inserts a second). One bulk insert: IN…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/muhammad_adnan_61b78b9816/a-createdat-only-cursor-lost-587-rows-even-with-clocktimestamp-and-microseconds-12d0

## Related notes
- [[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-11-09-my-latest-20-issues-query-read-200000-rows-even-with-an-index-on-projectid]]
- [[2026-10-24-how-to-find-missing-ids-between-two-lists-and-get-the-sql-for-free]]
- [[2026-10-22-why-offset-pagination-is-killing-your-postgresql-queries-and-how-to-implement-keyset-pagination-in-nodejs]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
