---
title: The Postgres job-claim query that silently claims the same job twice
date: '2026-09-19'
source: https://dev.to/vishwam_1705/the-postgres-job-claim-query-that-silently-claims-the-same-job-twice-2on6
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
- '[[2026-09-06-your-audit-log-is-probably-lying-to-you-postgres-18-fixes-it-in-one-statement]]'
- '[[2026-09-14-postgres-advisory-locks-are-not-the-lock-you-think]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** The Postgres job-claim query that silently claims the same job twice A common way to claim a background job in PostgreSQL is a single UPDATE with a subquery that picks the oldest pending row. It is one statement, so it l…

## What’s new and why it matters
The Postgres job-claim query that silently claims the same job twice A common way to claim a background job in PostgreSQL is a single UPDATE with a subquery that picks the oldest pending row. It is one statement, so it looks atomic. It is not. The most common version of it lets two sessions claim the same row. Both get rowcount = 1 . Neither gets an error. This happens on PostgreSQL's default isolation level, READ COMMITTED . The failure leaves nothing behind. The row ends up with status = 'running' , which is exactly what one clean claim looks like. There is no query you can run afterwards to…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vishwam_1705/the-postgres-job-claim-query-that-silently-claims-the-same-job-twice-2on6

## Related notes
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
- [[2026-09-06-your-audit-log-is-probably-lying-to-you-postgres-18-fixes-it-in-one-statement]]
- [[2026-09-14-postgres-advisory-locks-are-not-the-lock-you-think]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
