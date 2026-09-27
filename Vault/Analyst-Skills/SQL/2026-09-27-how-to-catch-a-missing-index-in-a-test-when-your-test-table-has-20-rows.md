---
title: How to catch a missing index in a test, when your test table has 20 rows.
date: '2026-09-27'
source: https://dev.to/ldavidsm/how-to-catch-a-missing-index-in-a-test-when-your-test-table-has-20-rows-1oh2
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]'
status: unread
---

> **TL;DR:** Here is a bug that no test suite catches. Someone adds a lookup by email. It works. Six months later the table has two million rows, that lookup has no index, and the endpoint takes four seconds. The tests were green the…

## What’s new and why it matters
Here is a bug that no test suite catches. Someone adds a lookup by email. It works. Six months later the table has two million rows, that lookup has no index, and the endpoint takes four seconds. The tests were green the whole time, because the test database had twenty rows and four seconds of two million rows is four milliseconds of twenty. The obvious fix is to assert on the query plan. That does not work either, and the reason it does not work is more interesting than the fix. What you would try first Ask PostgreSQL for the plan and fail the test if it contains a Seq Scan . Let us try it on…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ldavidsm/how-to-catch-a-missing-index-in-a-test-when-your-test-table-has-20-rows-1oh2

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]
