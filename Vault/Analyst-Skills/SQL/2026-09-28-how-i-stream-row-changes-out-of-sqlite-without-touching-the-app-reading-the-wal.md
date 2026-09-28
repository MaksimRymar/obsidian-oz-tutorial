---
title: How I stream row changes out of SQLite without touching the app (reading the
  WAL)
date: '2026-09-28'
source: https://dev.to/zaydmulani09/how-i-stream-row-changes-out-of-sqlite-without-touching-the-app-reading-the-wal-2abb
domain: SQL
relevance: 🟡
tags:
- '#career'
- '#library'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-09-24-sql-database-projects-and-ai-a-match-made-in-heaven]]'
- '[[2026-06-20-green-unit-tests-are-a-comfort-blanket]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]'
status: unread
---

> **TL;DR:** SQ Lite has no way to tell another process "row 42 in users just changed." I wanted that, so I built tailite : it follows a live SQLite database from outside and emits every committed insert, update and delete with befor…

## What’s new and why it matters
SQ Lite has no way to tell another process "row 42 in users just changed." I wanted that, so I built tailite : it follows a live SQLite database from outside and emits every committed insert, update and delete with before and after values. The writing app doesn't change. The options that didn't work sqlite3_update_hook and the preupdate hook only run inside the process doing the write. The session extension has to be turned on by the writer. Trigger-based CDC adds triggers and a log table, which is fine for your own app and not an option for a database some other app owns. Litestream and LiteF…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/zaydmulani09/how-i-stream-row-changes-out-of-sqlite-without-touching-the-app-reading-the-wal-2abb

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-09-24-sql-database-projects-and-ai-a-match-made-in-heaven]]
- [[2026-06-20-green-unit-tests-are-a-comfort-blanket]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]
