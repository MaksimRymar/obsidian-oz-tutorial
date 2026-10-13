---
title: 'PostgreSQL Data Types:'
date: '2026-10-13'
source: https://dev.to/im_nishant/postgresql-data-types-36em
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-14-choosing-a-primary-key-a-tour-of-the-ids-real-systems-actually-use]]'
- '[[2026-08-29-why-your-sql-server-database-is-slow-and-how-to-fix-it]]'
- '[[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]'
- '[[2026-05-20-top-10-agentic-ai-frameworks-compared-langgraph-vs-crewai-vs-autogen-vs-benchmarks-inside]]'
status: unread
---

> **TL;DR:** There's a specific kind of bug that doesn't show up right away. A latitude column stored as FLOAT , and months later your distance calculations are just slightly off in a way that's hard to pin down. Or a price column us…

## What’s new and why it matters
There's a specific kind of bug that doesn't show up right away. A latitude column stored as FLOAT , and months later your distance calculations are just slightly off in a way that's hard to pin down. Or a price column using the same type, and a customer notices their total is a cent wrong, in a way that somehow compounds across enough transactions to matter. Nobody wrote a bug in the usual sense. The data type was the bug, and it had been sitting there quietly since the table was created. Choosing a column's type feels like the most mechanical part of designing a schema — pick something that l…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/im_nishant/postgresql-data-types-36em

## Related notes
- [[2026-09-14-choosing-a-primary-key-a-tour-of-the-ids-real-systems-actually-use]]
- [[2026-08-29-why-your-sql-server-database-is-slow-and-how-to-fix-it]]
- [[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]
- [[2026-05-20-top-10-agentic-ai-frameworks-compared-langgraph-vs-crewai-vs-autogen-vs-benchmarks-inside]]
