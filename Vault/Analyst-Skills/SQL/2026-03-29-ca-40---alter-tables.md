---
title: CA 40 - Alter Tables
date: '2026-03-29'
source: https://dev.to/santhosh_v/ca-40-alter-tables-938
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-03-28-modifying-tables-in-sql-using-alter]]'
- '[[2026-03-29-alter-queries]]'
- '[[2026-03-26-create-tables]]'
- '[[2026-03-20-postgresqlalternations]]'
- '[[2026-03-26-create-tables]]'
- '[[2026-03-29-alter-tables]]'
status: unread
---

> **TL;DR:** Today I practiced ALTER TABLE in SQL. This is used when we want to change an existing table. 1. Make Email NOT NULL (customers) ALTER TABLE customers MODIFY email VARCHAR ( 100 ) NOT NULL ; Now email is required 2. Make…

## What’s new and why it matters
Today I practiced ALTER TABLE in SQL. This is used when we want to change an existing table. 1. Make Email NOT NULL (customers) ALTER TABLE customers MODIFY email VARCHAR ( 100 ) NOT NULL ; Now email is required 2. Make Username UNIQUE (users) ALTER TABLE users ADD CONSTRAINT unique_username UNIQUE ( username ); No duplicate usernames 3. Add CHECK on Price (products) ALTER TABLE products ADD CONSTRAINT check_price CHECK ( price > 0 ); price must be > 0 4. Default Status (orders) ALTER TABLE orders ALTER COLUMN status SET DEFAULT 'pending' ; if not given → pending 5. Add Salary Column (employee…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/santhosh_v/ca-40-alter-tables-938

## Related notes
- [[2026-03-28-modifying-tables-in-sql-using-alter]]
- [[2026-03-29-alter-queries]]
- [[2026-03-26-create-tables]]
- [[2026-03-20-postgresqlalternations]]
- [[2026-03-26-create-tables]]
- [[2026-03-29-alter-tables]]
