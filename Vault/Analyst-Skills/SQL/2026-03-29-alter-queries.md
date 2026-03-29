---
title: Alter Queries
date: '2026-03-29'
source: https://dev.to/christina_sharons_2b3205/alter-queries-2i8e
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-03-28-modifying-tables-in-sql-using-alter]]'
- '[[2026-03-26-create-tables]]'
- '[[2026-03-26-alter-table]]'
- '[[2026-03-24-sql-example]]'
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-03-15-sql-for-generating-test-data-in-mysql]]'
status: unread
---

> **TL;DR:** In this assignment, I worked on modifying existing tables using ALTER TABLE . This helped me understand how to update constraints without recreating tables. 1.Make email NOT NULL in customers ALTER TABLE customers ALTER…

## What’s new and why it matters
In this assignment, I worked on modifying existing tables using ALTER TABLE . This helped me understand how to update constraints without recreating tables. 1.Make email NOT NULL in customers ALTER TABLE customers ALTER COLUMN email SET NOT NULL ; 2.Make username UNIQUE in users ALTER TABLE users ADD CONSTRAINT unique_username UNIQUE ( username ); 3.Add CHECK constraint on price > 0 in products ALTER TABLE products ADD CONSTRAINT price_check CHECK ( price > 0 ); 4.Set default 'pending' for status in orders ALTER TABLE orders ALTER COLUMN status SET DEFAULT 'pending' ; 5.Add salary column with…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/christina_sharons_2b3205/alter-queries-2i8e

## Related notes
- [[2026-03-28-modifying-tables-in-sql-using-alter]]
- [[2026-03-26-create-tables]]
- [[2026-03-26-alter-table]]
- [[2026-03-24-sql-example]]
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-03-15-sql-for-generating-test-data-in-mysql]]
