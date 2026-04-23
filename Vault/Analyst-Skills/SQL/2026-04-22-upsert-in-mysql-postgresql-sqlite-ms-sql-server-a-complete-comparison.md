---
title: UPSERT in MySQL, PostgreSQL, SQLite & MS SQL Server — A Complete Comparison
date: '2026-04-22'
source: https://dev.to/digipackhq/upsert-in-mysql-postgresql-sqlite-ms-sql-server-a-complete-comparison-37em
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]'
- '[[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]'
- '[[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]'
- '[[2026-03-18-sql-mastery-the-essential-cheat-sheet-for-data-professionals]]'
- '[[2026-03-26-sqlite-can-do-more-than-you-think-full-text-search-json-window-functions-and-281tb-databases]]'
- '[[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]'
status: unread
---

> **TL;DR:** One of the most searched SQL topics — and one of the most confusing — is UPSERT: insert a row if it doesn't exist, update it if it does. The problem? Every database does it differently. Here's the definitive comparison a…

## What’s new and why it matters
One of the most searched SQL topics — and one of the most confusing — is UPSERT: insert a row if it doesn't exist, update it if it does. The problem? Every database does it differently. Here's the definitive comparison across all 4 major databases. MySQL INSERT INTO users (id, email) VALUES (1, ' new@x.com ') ON DUPLICATE KEY UPDATE email = VALUES(email); Works on any duplicate key — primary or unique index. PostgreSQL INSERT INTO users (id, email) VALUES (1, ' new@x.com ') ON CONFLICT (id) DO UPDATE SET email = EXCLUDED.email; EXCLUDED refers to the row that failed to insert. You can also use…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/digipackhq/upsert-in-mysql-postgresql-sqlite-ms-sql-server-a-complete-comparison-37em

## Related notes
- [[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]
- [[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]
- [[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]
- [[2026-03-18-sql-mastery-the-essential-cheat-sheet-for-data-professionals]]
- [[2026-03-26-sqlite-can-do-more-than-you-think-full-text-search-json-window-functions-and-281tb-databases]]
- [[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]
