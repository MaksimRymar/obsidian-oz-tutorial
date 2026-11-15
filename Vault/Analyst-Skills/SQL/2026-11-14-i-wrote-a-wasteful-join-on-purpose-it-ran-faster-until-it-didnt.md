---
title: I Wrote a Wasteful JOIN on Purpose. It Ran Faster, Until It Didn't.
date: '2026-11-14'
source: https://dev.to/danny0728/i-wrote-a-wasteful-join-on-purpose-it-ran-faster-until-it-didnt-2ifj
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-11-11-setting-up-postgresql-with-docker-psql-and-pgadmin]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-11-12-a-createdat-only-cursor-lost-587-rows-even-with-clocktimestamp-and-microseconds]]'
- '[[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]'
status: unread
---

> **TL;DR:** On my projects, GORM wrote most of the SQL. We used it for almost everything and dropped down to a SQL library only for the complex queries. Over time GORM became the comfortable default, and the idea of writing raw SQL…

## What’s new and why it matters
On my projects, GORM wrote most of the SQL. We used it for almost everything and dropped down to a SQL library only for the complex queries. Over time GORM became the comfortable default, and the idea of writing raw SQL with sqlc and pgx made me uneasy. The worry was specific. GORM has its own way of building queries, and I trusted its defaults to produce something reasonably efficient. When I write the SQL myself, nothing stops me from taking a strange route: joining through a table I don't need, because the result comes out the same. The rows are right, so nothing looks wrong, and the wasted…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/danny0728/i-wrote-a-wasteful-join-on-purpose-it-ran-faster-until-it-didnt-2ifj

## Related notes
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-11-11-setting-up-postgresql-with-docker-psql-and-pgadmin]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-11-12-a-createdat-only-cursor-lost-587-rows-even-with-clocktimestamp-and-microseconds]]
- [[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]
