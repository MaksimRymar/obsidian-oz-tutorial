---
title: Modifying Tables in SQL using ALTER
date: '2026-03-28'
source: https://dev.to/arul_selviml_7/modifying-tables-in-sql-using-alter-12dl
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-03-26-create-tables]]'
- '[[2026-03-26-create-tables]]'
- '[[2026-03-26-alter-table]]'
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-03-20-postgresqlalternations]]'
- '[[2026-03-02-joins-and-window-functions-made-super-simple]]'
status: unread
---

> **TL;DR:** 1. Making a Column NOT NULL Suppose we already created a customers table, but now we want to ensure that email is always provided. ALTER TABLE customers ALTER COLUMN email SET NOT NULL ; 2. Adding UNIQUE Constraint To ma…

## What’s new and why it matters
1. Making a Column NOT NULL Suppose we already created a customers table, but now we want to ensure that email is always provided. ALTER TABLE customers ALTER COLUMN email SET NOT NULL ; 2. Adding UNIQUE Constraint To make sure no two users have the same username: ALTER TABLE users ADD CONSTRAINT unique_username UNIQUE ( username ); 3. Adding CHECK Constraint We want to ensure product price is always greater than 0: ALTER TABLE products ADD CONSTRAINT check_price CHECK ( price > 0 ); 4. Setting DEFAULT Value To make status = 'pending' by default: ALTER TABLE orders ALTER COLUMN status SET DEFA…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/arul_selviml_7/modifying-tables-in-sql-using-alter-12dl

## Related notes
- [[2026-03-26-create-tables]]
- [[2026-03-26-create-tables]]
- [[2026-03-26-alter-table]]
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-03-20-postgresqlalternations]]
- [[2026-03-02-joins-and-window-functions-made-super-simple]]
