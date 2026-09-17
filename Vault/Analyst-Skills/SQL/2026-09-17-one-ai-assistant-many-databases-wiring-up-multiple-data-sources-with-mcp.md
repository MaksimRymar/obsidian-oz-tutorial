---
title: 'One AI Assistant, Many Databases: Wiring Up Multiple Data Sources with MCP'
date: '2026-09-17'
source: https://dev.to/vivekdraxlr/one-ai-assistant-many-databases-wiring-up-multiple-data-sources-with-mcp-35pm
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]'
- '[[2026-07-18-building-my-first-real-database-what-a-weekend-sql-assignment-taught-me-about-postgres-and-git]]'
- '[[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-05-let-non-technical-teammates-query-the-database-without-handing-out-db-access]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
status: unread
---

> **TL;DR:** You wired up an AI assistant to your database and it's great. You ask "what was MRR by plan last month?" and get back working SQL and an answer in seconds. Then reality sets in: that was your analytics database. Your use…

## What’s new and why it matters
You wired up an AI assistant to your database and it's great. You ask "what was MRR by plan last month?" and get back working SQL and an answer in seconds. Then reality sets in: that was your analytics database. Your user records live in a Postgres replica. Your billing events sit in a separate MySQL box that a previous team stood up and nobody wants to touch. Real teams almost never have one database — they have a small constellation of them. So the interesting question isn't "can an AI query my database?" It's "how do I give one assistant safe, sane access to all of my databases at once — an…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vivekdraxlr/one-ai-assistant-many-databases-wiring-up-multiple-data-sources-with-mcp-35pm

## Related notes
- [[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]
- [[2026-07-18-building-my-first-real-database-what-a-weekend-sql-assignment-taught-me-about-postgres-and-git]]
- [[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-05-let-non-technical-teammates-query-the-database-without-handing-out-db-access]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
