---
title: 'From 30 Minutes to 5 Seconds: Testing Agent Memory with Pytest + SQLite'
date: '2026-08-17'
source: https://dev.to/_eb7f2a654e97a60ae9f96e/from-30-minutes-to-5-seconds-testing-agent-memory-with-pytest-sqlite-4nfm
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-15-debugging-ai-agent-context-pollution-with-pytest-redis-3-cross-talk-bugs-in-6-hours]]'
- '[[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]'
- '[[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]'
- '[[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-04-22-upsert-in-mysql-postgresql-sqlite-ms-sql-server-a-complete-comparison]]'
status: unread
---

> **TL;DR:** At 1 AM, a message popped up in the test group chat: the agent had leaked one user's memory into a new session. I opened DB Browser, hand-wrote 8 SELECT queries, and compared session_id and key row by row. Half an hour l…

## What’s new and why it matters
At 1 AM, a message popped up in the test group chat: the agent had leaked one user's memory into a new session. I opened DB Browser, hand-wrote 8 SELECT queries, and compared session_id and key row by row. Half an hour later, I tracked it down to a missing session_id in the WHERE condition of the upsert. This wasn't the first time. Breaking Down the Problem The agent's memory storage is basically just a SQLite table with three core fields: session_id, key, and value. The consistency requirements are simple too: updating the same key within a session must not create duplicate rows; different se…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/_eb7f2a654e97a60ae9f96e/from-30-minutes-to-5-seconds-testing-agent-memory-with-pytest-sqlite-4nfm

## Related notes
- [[2026-08-15-debugging-ai-agent-context-pollution-with-pytest-redis-3-cross-talk-bugs-in-6-hours]]
- [[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]
- [[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]
- [[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-04-22-upsert-in-mysql-postgresql-sqlite-ms-sql-server-a-complete-comparison]]
