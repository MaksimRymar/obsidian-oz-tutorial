---
title: My "latest 20 issues" query read 200,000 rows, even with an index on project_id
date: '2026-11-09'
source: https://dev.to/muhammad_adnan_61b78b9816/my-latest-20-issues-query-read-200000-rows-even-with-an-index-on-projectid-4865
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-10-15-the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-attempts]]'
- '[[2026-08-30-when-to-index-a-table-a-practical-guide-for-analysts]]'
- '[[2026-06-29-how-database-indexes-actually-work-and-when-they-backfire]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
status: unread
---

> **TL;DR:** Almost every app has this query. Show the newest items in a project, one page at a time: SELECT id , title , status , created_at FROM issues WHERE project_id = $ 1 ORDER BY created_at DESC , id DESC LIMIT 20 ; And almost…

## What’s new and why it matters
Almost every app has this query. Show the newest items in a project, one page at a time: SELECT id , title , status , created_at FROM issues WHERE project_id = $ 1 ORDER BY created_at DESC , id DESC LIMIT 20 ; And almost every schema has the index that seems to cover it: CREATE INDEX ON issues ( project_id ); It's indexed, it's fast in development, and code review passes it. I measured what it does once one project gets big. The setup PostgreSQL 16, 2,000,000 issues across 2,000 projects. Project 1 is a big customer with 200,000 issues; project 500 is typical, with 901. Each number below is th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/muhammad_adnan_61b78b9816/my-latest-20-issues-query-read-200000-rows-even-with-an-index-on-projectid-4865

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-10-15-the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-attempts]]
- [[2026-08-30-when-to-index-a-table-a-practical-guide-for-analysts]]
- [[2026-06-29-how-database-indexes-actually-work-and-when-they-backfire]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
