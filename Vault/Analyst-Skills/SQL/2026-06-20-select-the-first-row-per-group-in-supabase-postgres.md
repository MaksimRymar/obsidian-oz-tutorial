---
title: Select the First Row per Group in Supabase Postgres
date: '2026-06-20'
source: https://dev.to/mahdi_benrhouma_fe1c6005/select-the-first-row-per-group-in-supabase-postgres-52gg
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-05-11-postgresql-sql-cheat-sheet-clause-order-joins-aggregates-windows]]'
- '[[2026-05-28-how-to-correctly-read-a-postgresql-explain-analyze-output]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
status: unread
---

> **TL;DR:** You want the most recent order per customer , or the highest-scoring row per team . You reach for GROUP BY ... and hit a wall: GROUP BY returns aggregates, not the full non-aggregated row that achieved the max. This is t…

## What’s new and why it matters
You want the most recent order per customer , or the highest-scoring row per team . You reach for GROUP BY ... and hit a wall: GROUP BY returns aggregates, not the full non-aggregated row that achieved the max. This is the classic greatest-N-per-group problem, and PostgreSQL has a clean answer that supabase-js can't express directly. { name: "PostgreSQL", version: "DISTINCT ON / window fns" }, { name: "Supabase", version: "view / RPC" }, ]} /> The idiomatic way: DISTINCT ON PostgreSQL's DISTINCT ON "keeps only the first row of each set of rows where the given expressions evaluate to equal." Th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mahdi_benrhouma_fe1c6005/select-the-first-row-per-group-in-supabase-postgres-52gg

## Related notes
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-05-11-postgresql-sql-cheat-sheet-clause-order-joins-aggregates-windows]]
- [[2026-05-28-how-to-correctly-read-a-postgresql-explain-analyze-output]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
