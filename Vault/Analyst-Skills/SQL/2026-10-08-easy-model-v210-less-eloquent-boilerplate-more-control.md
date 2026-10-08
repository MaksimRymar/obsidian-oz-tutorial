---
title: 'Easy Model v2.1.0: Less Eloquent Boilerplate, More Control'
date: '2026-10-08'
source: https://dev.to/mmramadan496/easy-model-v210-less-eloquent-boilerplate-more-control-4eg1
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-03-10-building-a-production-ready-agentic-ai-system-with-langgraph-and-mcp]]'
- '[[2026-08-12-can-you-run-hybrid-search-on-one-database-yes-heres-how-cratedb-does-it]]'
- '[[2026-05-04-a-practical-project-structure-for-fastapi-applications]]'
- '[[2026-08-26-building-a-defi-yield-scanner-with-python-and-ai]]'
- '[[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]'
- '[[2026-05-15-sql-queries-every-developer-should-know-with-examples]]'
status: unread
---

> **TL;DR:** 🚀 Easy Model v2.1.0 is here! Eloquent makes simple queries easy. But as an application grows, the same filtering, sorting, searching, eager loading, pagination, and relationship logic can start appearing across multiple…

## What’s new and why it matters
🚀 Easy Model v2.1.0 is here! Eloquent makes simple queries easy. But as an application grows, the same filtering, sorting, searching, eager loading, pagination, and relationship logic can start appearing across multiple controllers and repositories. A typical endpoint can quickly turn into a long chain of conditional query logic: $query = User :: query (); $query -> when ( $request -> filled ( 'search' ), function ( $query ) use ( $request ) { $query -> where ( 'name' , 'like' , '%' . $request -> search . '%' ); }); $query -> when ( $request -> filled ( 'sort' ), function ( $query ) use ( $req…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mmramadan496/easy-model-v210-less-eloquent-boilerplate-more-control-4eg1

## Related notes
- [[2026-03-10-building-a-production-ready-agentic-ai-system-with-langgraph-and-mcp]]
- [[2026-08-12-can-you-run-hybrid-search-on-one-database-yes-heres-how-cratedb-does-it]]
- [[2026-05-04-a-practical-project-structure-for-fastapi-applications]]
- [[2026-08-26-building-a-defi-yield-scanner-with-python-and-ai]]
- [[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]
- [[2026-05-15-sql-queries-every-developer-should-know-with-examples]]
