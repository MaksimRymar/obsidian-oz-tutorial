---
title: 'Your Search Query Is a Program: Composing Role-Based SQL With the Strategy
  Pattern'
date: '2026-09-26'
source: https://dev.to/purbano/your-search-query-is-a-program-composing-role-based-sql-with-the-strategy-pattern-3o3a
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]'
status: unread
---

> **TL;DR:** Every business application has this screen somewhere: a table of records, filter boxes above it, and a user who may only see part of the data. The first query is a SELECT with a WHERE on the user's office. Filters arrive…

## What’s new and why it matters
Every business application has this screen somewhere: a table of records, filter boxes above it, and a user who may only see part of the data. The first query is a SELECT with a WHERE on the user's office. Filters arrive one at a time, then a role that sees two offices, then an auditor who sees everything once approved. Eventually the query is a two-hundred-line method nobody wants to touch. Our argument is that this query was never a string. A search with optional filters and role-based visibility is application logic, and one of its invariants is a security boundary. Built by appending text,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/purbano/your-search-query-is-a-program-composing-role-based-sql-with-the-strategy-pattern-3o3a

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]
