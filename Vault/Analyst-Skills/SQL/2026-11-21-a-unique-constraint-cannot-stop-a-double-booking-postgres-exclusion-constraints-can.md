---
title: A Unique Constraint Cannot Stop a Double Booking. Postgres Exclusion Constraints
  Can
date: '2026-11-21'
source: https://martin128.medium.com/a-unique-constraint-cannot-stop-a-double-booking-postgres-exclusion-constraints-can-60f40d45ca59?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-05-20-preventing-double-bookings-with-postgresql-exclusion-constraints]]'
- '[[2026-10-12-matched-is-not-agreed-a-sql-pattern-for-reconciling-orders-payments-and-refunds]]'
- '[[2026-10-30-using-claude-to-build-a-postgres-job-queue-with-for-update-skip-locked]]'
- '[[2026-09-26-sqljev-typesafe-jevs-jev-for-sql-server-postgres-snowflake-bigquery-and-duckdb-on-jev-or]]'
- '[[2026-11-20-stop-writing-select-then-insert-postgres-upserts-in-one-statement]]'
- '[[2026-10-13-postgres-18-can-enforce-no-two-bookings-overlap-for-you]]'
status: unread
---

> **TL;DR:** UNIQUE catches exact duplicates. “No two bookings for the same room at overlapping times” needs EXCLUDE USING gist. Here is the whole… Continue reading on Medium »

## What’s new and why it matters
UNIQUE catches exact duplicates. “No two bookings for the same room at overlapping times” needs EXCLUDE USING gist. Here is the whole… Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://martin128.medium.com/a-unique-constraint-cannot-stop-a-double-booking-postgres-exclusion-constraints-can-60f40d45ca59?source=rss------sql-5

## Related notes
- [[2026-05-20-preventing-double-bookings-with-postgresql-exclusion-constraints]]
- [[2026-10-12-matched-is-not-agreed-a-sql-pattern-for-reconciling-orders-payments-and-refunds]]
- [[2026-10-30-using-claude-to-build-a-postgres-job-queue-with-for-update-skip-locked]]
- [[2026-09-26-sqljev-typesafe-jevs-jev-for-sql-server-postgres-snowflake-bigquery-and-duckdb-on-jev-or]]
- [[2026-11-20-stop-writing-select-then-insert-postgres-upserts-in-one-statement]]
- [[2026-10-13-postgres-18-can-enforce-no-two-bookings-overlap-for-you]]
