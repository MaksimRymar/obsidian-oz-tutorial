---
title: I Ran a Loop Over 100,000 Rows in My FastAPI App and Called commit() Inside
  It.
date: '2026-08-31'
source: https://medium.com/@rameshkannanyt0078/i-ran-a-loop-over-100-000-rows-in-my-fastapi-app-and-called-commit-inside-it-5bebdc99f636?source=rss------python-5
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-15-a-production-messenger-stack-for-10000-users-fastapi-sqlite-in-production-and-why-i-kept-it]]'
- '[[2026-05-13-snowflake-time-travel-saved-my-data-and-my-week]]'
- '[[2026-05-21-architecting-sub-150ms-hybrid-rag-for-voice-agents-combining-pgvector-bm25-and-async-fastapi]]'
- '[[2026-06-11-redis-vs-dragonfly-vs-keydb-2026-i-benchmarked-1-million-cache-hits-for-my-fastapi-app-one-is-25x]]'
- '[[2026-06-13-how-i-lost-100-in-my-database-without-a-single-error-log]]'
- '[[2026-06-14-day-5-fastapi-crud-apis-with-validations]]'
status: unread
---

> **TL;DR:** I wrote a script to update user statuses. for user in users: user.status = "active"; db.commit(). 100,000 commits. Postgres wrote to disk… Continue reading on Medium »

## What’s new and why it matters
I wrote a script to update user statuses. for user in users: user.status = "active"; db.commit(). 100,000 commits. Postgres wrote to disk… Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/@rameshkannanyt0078/i-ran-a-loop-over-100-000-rows-in-my-fastapi-app-and-called-commit-inside-it-5bebdc99f636?source=rss------python-5

## Related notes
- [[2026-05-15-a-production-messenger-stack-for-10000-users-fastapi-sqlite-in-production-and-why-i-kept-it]]
- [[2026-05-13-snowflake-time-travel-saved-my-data-and-my-week]]
- [[2026-05-21-architecting-sub-150ms-hybrid-rag-for-voice-agents-combining-pgvector-bm25-and-async-fastapi]]
- [[2026-06-11-redis-vs-dragonfly-vs-keydb-2026-i-benchmarked-1-million-cache-hits-for-my-fastapi-app-one-is-25x]]
- [[2026-06-13-how-i-lost-100-in-my-database-without-a-single-error-log]]
- [[2026-06-14-day-5-fastapi-crud-apis-with-validations]]
