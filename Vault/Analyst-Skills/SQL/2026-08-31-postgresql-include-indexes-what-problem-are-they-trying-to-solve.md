---
title: 'PostgreSQL INCLUDE indexes: what problem are they trying to solve?'
date: '2026-08-31'
source: https://dev.to/franckpachot/postgresql-include-indexes-what-problem-are-they-trying-to-solve-4f4n
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]'
- '[[2026-03-02-dbeaver-postgres-aiven-and-other-sql-shenanigans]]'
- '[[2026-07-10-oracle-ora-01401-error-causes-and-solutions-complete-guide]]'
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]'
status: unread
---

> **TL;DR:** A common way to explain PostgreSQL's INCLUDE clause is that it helps with index-only scans. That's true, but it misses an important detail. Even before PostgreSQL 11, which introduced the INCLUDE clause, PostgreSQL was a…

## What’s new and why it matters
A common way to explain PostgreSQL's INCLUDE clause is that it helps with index-only scans. That's true, but it misses an important detail. Even before PostgreSQL 11, which introduced the INCLUDE clause, PostgreSQL was already capable of supporting covering indexes: postgres =# create table demo ( id text primary key , value text ) ; CREATE TABLE postgres =# insert into demo ( id , value ) select md5 ( g :: text ), -- using text to see it with pageinspect md5 (( g % 1000 ):: text ) -- using text to see it with pageinspect from generate_series ( 1 , 1000000 ) g ; INSERT 0 1000000 postgres =# cr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/franckpachot/postgresql-include-indexes-what-problem-are-they-trying-to-solve-4f4n

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]
- [[2026-03-02-dbeaver-postgres-aiven-and-other-sql-shenanigans]]
- [[2026-07-10-oracle-ora-01401-error-causes-and-solutions-complete-guide]]
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]
