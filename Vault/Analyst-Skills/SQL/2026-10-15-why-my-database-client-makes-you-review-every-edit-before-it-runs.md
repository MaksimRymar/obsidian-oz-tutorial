---
title: Why my database client makes you review every edit before it runs
date: '2026-10-15'
source: https://dev.to/mohammadalfarra/why-my-database-client-makes-you-review-every-edit-before-it-runs-2e4d
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-09-03-speeding-up-a-slow-plsql-routine-with-bulk-collect-and-forall]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-21-which-sql-database-should-you-install]]'
status: unread
---

> **TL;DR:** Most database clients let you edit a cell and the change is saved immediately. That's fine until it isn't: a wrong row, a wrong table, a connection pointed at production. I built Tabelaro, a free database client for Mac…

## What’s new and why it matters
Most database clients let you edit a cell and the change is saved immediately. That's fine until it isn't: a wrong row, a wrong table, a connection pointed at production. I built Tabelaro, a free database client for Mac (PostgreSQL, MySQL/MariaDB and SQLite), around a different idea: edits should wait. Wax When you change a value, Tabelaro doesn't run anything. The change sits as a draft in "wax". Before it touches the database you open the review and read the exact SQL it will run. Then you commit it, or discard it. Stylus (⌘K) Instead of hunting through panels, one box takes you to any table…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mohammadalfarra/why-my-database-client-makes-you-review-every-edit-before-it-runs-2e4d

## Related notes
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-09-03-speeding-up-a-slow-plsql-routine-with-bulk-collect-and-forall]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-21-which-sql-database-should-you-install]]
