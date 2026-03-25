---
title: SQL example
date: '2026-03-24'
source: https://dev.to/timxcollyx/sql-example-3hbb
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-15-sql-for-generating-test-data-in-mysql]]'
- '[[2026-03-08-i-built-a-sql-query-builder-in-python---never-hand-write-sql-again]]'
- '[[2026-03-20-postgresql-constraints]]'
- '[[2026-03-14-ch-6-working-with-tables-and-other-sql-need-to-knows]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-05-im-an-ai-with-88-days-to-profit-or-i-die-day-3-30-burned-0-earned]]'
status: unread
---

> **TL;DR:** CREATE DATABASE IF NOT EXISTS greenfield_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci ; USE greenfield_db ; SET FOREIGN_KEY_CHECKS = 0 ; DROP TABLE IF EXISTS reviews ; DROP TABLE IF EXISTS order_items ; DROP TABLE…

## What’s new and why it matters
CREATE DATABASE IF NOT EXISTS greenfield_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci ; USE greenfield_db ; SET FOREIGN_KEY_CHECKS = 0 ; DROP TABLE IF EXISTS reviews ; DROP TABLE IF EXISTS order_items ; DROP TABLE IF EXISTS orders ; DROP TABLE IF EXISTS products ; DROP TABLE IF EXISTS categories ; DROP TABLE IF EXISTS users ; SET FOREIGN_KEY_CHECKS = 1 ; CREATE TABLE users ( id INT AUTO_INCREMENT PRIMARY KEY , first_name VARCHAR ( 100 ) NOT NULL , last_name VARCHAR ( 100 ) NOT NULL , email VARCHAR ( 255 ) NOT NULL UNIQUE , password_hash VARCHAR ( 255 ) NOT NULL , role ENUM ( 'customer'…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/timxcollyx/sql-example-3hbb

## Related notes
- [[2026-03-15-sql-for-generating-test-data-in-mysql]]
- [[2026-03-08-i-built-a-sql-query-builder-in-python---never-hand-write-sql-again]]
- [[2026-03-20-postgresql-constraints]]
- [[2026-03-14-ch-6-working-with-tables-and-other-sql-need-to-knows]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-05-im-an-ai-with-88-days-to-profit-or-i-die-day-3-30-burned-0-earned]]
