---
title: You added a second SQL engine. Your text-to-SQL model is still being told it's
  the first one.
date: '2026-08-31'
source: https://dev.to/omer_hochman/you-added-a-second-sql-engine-your-text-to-sql-model-is-still-being-told-its-the-first-one-2d92
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-08-30-you-added-clickhouse-your-postgres-sql-validator-now-rejects-valid-queries-quietly]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-08-29-why-your-sql-server-database-is-slow-and-how-to-fix-it]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
status: unread
---

> **TL;DR:** Originally published at nlqdb.com/blog A text-to-SQL model is dialect-aware by design. You hand it a target dialect, and it obliges — name Postgres, get Postgres. So when we added a second engine, ClickHouse alongside Po…

## What’s new and why it matters
Originally published at nlqdb.com/blog A text-to-SQL model is dialect-aware by design. You hand it a target dialect, and it obliges — name Postgres, get Postgres. So when we added a second engine, ClickHouse alongside Postgres, the model kept doing exactly what it does well: writing SQL for the dialect it was told. The trouble is what it was told. The happy path compiled, the Postgres queries still worked, and a class of analytical questions on the ClickHouse databases started coming back subtly wrong. The model wasn't confused. It was confidently writing Postgres for a database that speaks Cl…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/omer_hochman/you-added-a-second-sql-engine-your-text-to-sql-model-is-still-being-told-its-the-first-one-2d92

## Related notes
- [[2026-08-30-you-added-clickhouse-your-postgres-sql-validator-now-rejects-valid-queries-quietly]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-08-29-why-your-sql-server-database-is-slow-and-how-to-fix-it]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
