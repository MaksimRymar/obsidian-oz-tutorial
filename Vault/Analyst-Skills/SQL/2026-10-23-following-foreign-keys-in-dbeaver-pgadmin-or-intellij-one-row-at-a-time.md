---
title: 'Following foreign keys in DBeaver, pgAdmin or IntelliJ: one row at a time'
date: '2026-10-23'
source: https://dev.to/clementgpro/following-foreign-keys-in-dbeaver-pgadmin-or-intellij-one-row-at-a-time-b15
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-02-how-i-turn-ai-images-into-print-ready-vector-stickers-no-illustrator-no-gpu]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-09-11-every-tennis-match-with-15-bookmakers-form-and-head-to-head-in-one-json-row]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
status: unread
---

> **TL;DR:** You know the drill. Something looks wrong for one company in the database, and to understand what's going on you need to see everything connected to it: its departments, the teams in each department, the employees in eac…

## What’s new and why it matters
You know the drill. Something looks wrong for one company in the database, and to understand what's going on you need to see everything connected to it: its departments, the teams in each department, the employees in each team, their managers. I'm not doing this in raw SQL. I use the same tools as most of us: DBeaver, pgAdmin, or the Database tool in IntelliJ. They're great tools. But for this specific job, they all work the same way, and it gets painful fast. What it looks like today You open the companies table and find the row. Then you open departments in another tab and filter on company_…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/clementgpro/following-foreign-keys-in-dbeaver-pgadmin-or-intellij-one-row-at-a-time-b15

## Related notes
- [[2026-10-02-how-i-turn-ai-images-into-print-ready-vector-stickers-no-illustrator-no-gpu]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-09-11-every-tennis-match-with-15-bookmakers-form-and-head-to-head-in-one-json-row]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
