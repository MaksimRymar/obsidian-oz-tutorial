---
title: 'The Dialect Trap: Why AI Writes SQL Your Database Refuses to Run'
date: '2026-09-18'
source: https://dev.to/vivekdraxlr/the-dialect-trap-why-ai-writes-sql-your-database-refuses-to-run-5ci9
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]'
- '[[2026-07-31-why-ai-keeps-inventing-columns-that-dont-exist-and-how-to-stop-it]]'
- '[[2026-07-06-stop-pasting-your-database-schema-into-every-ai-prompt]]'
- '[[2026-08-20-read-only-by-design-letting-ai-explore-your-database-without-the-risk-of-writes]]'
status: unread
---

> **TL;DR:** You ask an AI assistant for "the 10 most recent orders." It confidently hands you this: SELECT TOP 10 * FROM orders ORDER BY created_at DESC ; Looks fine — until you run it on PostgreSQL and get syntax error at or near "…

## What’s new and why it matters
You ask an AI assistant for "the 10 most recent orders." It confidently hands you this: SELECT TOP 10 * FROM orders ORDER BY created_at DESC ; Looks fine — until you run it on PostgreSQL and get syntax error at or near "10" . The logic was perfect. The dialect was wrong. TOP is SQL Server syntax; Postgres wants LIMIT . This is one of the most common and most frustrating failure modes of text-to-SQL. The query reads like valid SQL, passes a human eyeball test, and still bounces off your database because SQL isn't really one language — it's a family of closely-related dialects that disagree on t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vivekdraxlr/the-dialect-trap-why-ai-writes-sql-your-database-refuses-to-run-5ci9

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]
- [[2026-07-31-why-ai-keeps-inventing-columns-that-dont-exist-and-how-to-stop-it]]
- [[2026-07-06-stop-pasting-your-database-schema-into-every-ai-prompt]]
- [[2026-08-20-read-only-by-design-letting-ai-explore-your-database-without-the-risk-of-writes]]
