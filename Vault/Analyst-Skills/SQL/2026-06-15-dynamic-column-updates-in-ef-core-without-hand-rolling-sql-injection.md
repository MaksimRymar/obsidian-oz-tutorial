---
title: Dynamic Column Updates in EF Core Without Hand-Rolling SQL Injection
date: '2026-06-15'
source: https://dev.to/mattia_armas/dynamic-column-updates-in-ef-core-without-hand-rolling-sql-injection-mip
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]'
- '[[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]'
- '[[2026-05-13-we-built-an-enterprise-integration-stack-for-net-from-scratch-eav-dsl-runtime]]'
- '[[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]'
- '[[2026-06-12-indexes-quickstart-using-postgresql-15-sec-read]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
status: unread
---

> **TL;DR:** Sometimes you genuinely need the set of columns to update to be data, not code. An operator maps configuration fields to database columns, and you want to honor that mapping without redeploying every time it changes. The…

## What’s new and why it matters
Sometimes you genuinely need the set of columns to update to be data, not code. An operator maps configuration fields to database columns, and you want to honor that mapping without redeploying every time it changes. The naive solution — build an UPDATE string from those column names — is also one of the easiest ways to hand-write a SQL injection vulnerability. This is how to get the flexibility without the hole. We'll build it up in three layers: make it work, make it safe, then count the cost. Layer 1: The dynamic update, the wrong way The tempting version concatenates column names into SQL:…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/mattia_armas/dynamic-column-updates-in-ef-core-without-hand-rolling-sql-injection-mip

## Related notes
- [[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]
- [[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]
- [[2026-05-13-we-built-an-enterprise-integration-stack-for-net-from-scratch-eav-dsl-runtime]]
- [[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]
- [[2026-06-12-indexes-quickstart-using-postgresql-15-sec-read]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
