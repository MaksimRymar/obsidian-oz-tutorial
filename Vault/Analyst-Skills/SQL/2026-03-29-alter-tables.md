---
title: Alter Tables
date: '2026-03-29'
source: https://dev.to/shreya_princy_8194cc37e3f/alter-tables-4d1m
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-03-28-modifying-tables-in-sql-using-alter]]'
- '[[2026-03-29-alter-queries]]'
- '[[2026-03-26-alter-table]]'
- '[[2026-03-20-postgresql-constraints]]'
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-03-26-create-tables]]'
status: unread
---

> **TL;DR:** Modifying TabModifying Tables Using ALTER in PostgreSQL In real-world database systems, requirements often change after tables are created. Instead of recreating tables, we use the ALTER TABLE command to update structure…

## What’s new and why it matters
Modifying TabModifying Tables Using ALTER in PostgreSQL In real-world database systems, requirements often change after tables are created. Instead of recreating tables, we use the ALTER TABLE command to update structure, constraints, and relationships. Below are practical examples demonstrating how to modify existing tables effectively. Making Email Mandatory in Customers Table Initially, the email column may allow NULL values. To enforce that every new record must include an email: ALTER TABLE customers ALTER COLUMN email SET NOT NULL; Enforcing Unique Usernames To ensure that no two users s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/shreya_princy_8194cc37e3f/alter-tables-4d1m

## Related notes
- [[2026-03-28-modifying-tables-in-sql-using-alter]]
- [[2026-03-29-alter-queries]]
- [[2026-03-26-alter-table]]
- [[2026-03-20-postgresql-constraints]]
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-03-26-create-tables]]
