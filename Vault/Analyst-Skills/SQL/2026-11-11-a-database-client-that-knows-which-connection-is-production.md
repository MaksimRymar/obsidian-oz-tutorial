---
title: A database client that knows which connection is production
date: '2026-11-11'
source: https://dev.to/mrcatz/a-database-client-that-knows-which-connection-is-production-3ehn
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
related:
- '[[2026-08-21-which-sql-database-should-you-install]]'
- '[[2026-11-03-i-built-a-windows-sql-client-where-an-llm-drafts-the-query-and-you-stay-in-control]]'
- '[[2026-10-15-why-my-database-client-makes-you-review-every-edit-before-it-runs]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]'
- '[[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]'
status: unread
---

> **TL;DR:** DBCatz is a free, open-source client for MySQL, PostgreSQL, SQLite, Redis, MongoDB and Elasticsearch with a Production mode that makes mistakes harmless. Most of us have done it, or watched someone do it: a query meant f…

## What’s new and why it matters
DBCatz is a free, open-source client for MySQL, PostgreSQL, SQLite, Redis, MongoDB and Elasticsearch with a Production mode that makes mistakes harmless. Most of us have done it, or watched someone do it: a query meant for the local database, run in the tab that was connected to production. Same window, same colours, same confident Enter key. DBCatz is built around one idea: the client should know which connection is production, and behave differently there. It is free and open source (GPL-3.0), for macOS, Windows and Linux. Safety mode, per connection Every connection has a safety mode: Norma…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mrcatz/a-database-client-that-knows-which-connection-is-production-3ehn

## Related notes
- [[2026-08-21-which-sql-database-should-you-install]]
- [[2026-11-03-i-built-a-windows-sql-client-where-an-llm-drafts-the-query-and-you-stay-in-control]]
- [[2026-10-15-why-my-database-client-makes-you-review-every-edit-before-it-runs]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]
- [[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]
