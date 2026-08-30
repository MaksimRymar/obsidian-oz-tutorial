---
title: Can I veto the agent's DDL before it hits main?
date: '2026-08-30'
source: https://dev.to/erdonline/can-i-veto-the-agents-ddl-before-it-hits-main-3n0
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** Two hours before go-live, the DDL lands in the group chat Thursday, 10 p.m. The release window is 1 a.m. Someone drops alter_orders_v47.sql into the channel: "Agent generated it. CI is green. Can we merge?" You are the D…

## What’s new and why it matters
Two hours before go-live, the DDL lands in the group chat Thursday, 10 p.m. The release window is 1 a.m. Someone drops alter_orders_v47.sql into the channel: "Agent generated it. CI is green. Can we merge?" You are the DBA. You are not the Tech Lead who clicked Approve this afternoon — that already happened. You are the last person who can still say no. You open the file: add columns, change types, add indexes, attach foreign keys. The parser is happy. The names look like your team's. You know the things that actually blow up are not in the line numbers: how long this table locks tonight, whet…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/erdonline/can-i-veto-the-agents-ddl-before-it-hits-main-3n0

## Related notes
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
