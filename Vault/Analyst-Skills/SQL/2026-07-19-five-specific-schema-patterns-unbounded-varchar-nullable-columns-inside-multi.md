---
title: Five specific schema patterns — unbounded VARCHAR, nullable columns inside
  multi
date: '2026-07-19'
source: https://dev.to/philip_mcclarence_2ef9475/five-specific-schema-patterns-unbounded-varchar-nullable-columns-inside-multi-1glp
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-06-5-database-design-mistakes-i-keep-seeing-and-how-to-catch-them-early]]'
- '[[2026-07-17-five-schema-design-habits-that-look-harmless-in-a-migration-file-unbounded-var]]'
- '[[2026-06-10-your-database-is-fast-your-queries-are-slow]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
status: unread
---

> **TL;DR:** Title: The 5 Postgres Schema Mistakes That Kill Performance at Scale (and How to Fix Them) Target keyword: postgres schema mistakes performance I recorded a video walking through these five patterns on a whiteboard—how t…

## What’s new and why it matters
Title: The 5 Postgres Schema Mistakes That Kill Performance at Scale (and How to Fix Them) Target keyword: postgres schema mistakes performance I recorded a video walking through these five patterns on a whiteboard—how they look at 10k rows and why they fall apart at 10M. This post is the companion: exact copy‑paste SQL, concrete migration steps, and the trade‑offs you’ll actually weigh in production. If you’ve inherited a Rails or Django schema, you’ve probably seen at least three of these. TL;DR Unbounded VARCHAR → set a length: VARCHAR(255) . Block new oversized rows with a CHECK constraint…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/philip_mcclarence_2ef9475/five-specific-schema-patterns-unbounded-varchar-nullable-columns-inside-multi-1glp

## Related notes
- [[2026-03-06-5-database-design-mistakes-i-keep-seeing-and-how-to-catch-them-early]]
- [[2026-07-17-five-schema-design-habits-that-look-harmless-in-a-migration-file-unbounded-var]]
- [[2026-06-10-your-database-is-fast-your-queries-are-slow]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
