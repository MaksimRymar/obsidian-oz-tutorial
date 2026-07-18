---
title: The Data Dictionary Should Live in the ERD, Not in a Spreadsheet
date: '2026-07-18'
source: https://dev.to/tbson87/the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet-23c3
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-06-18-building-an-mcp-sql-tool-that-lets-llms-query-live-databases-with-wanaku]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-04-05-how-a-database-really-works-underneath]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: The meaning of a schema - what tables are for, who owns them, why a grouping exists - usually lives in h…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: The meaning of a schema - what tables are for, who owns them, why a grouping exists - usually lives in heads, spreadsheets, or wikis that drift out of date. Schemity attaches markdown descriptions to entities, legends, and context views, shown behind a file icon on the diagram itself, so the data dictionary lives inside the ERD and stays where the schema is. You can write what a table, a group of tables, or an entire view of your schema means directly into the diagram: Schemity s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet-23c3

## Related notes
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-06-18-building-an-mcp-sql-tool-that-lets-llms-query-live-databases-with-wanaku]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-04-05-how-a-database-really-works-underneath]]
