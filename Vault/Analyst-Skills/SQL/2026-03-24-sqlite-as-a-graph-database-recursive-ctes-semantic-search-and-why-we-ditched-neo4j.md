---
title: 'SQLite as a Graph Database: Recursive CTEs, Semantic Search, and Why We Ditched
  Neo4j'
date: '2026-03-24'
source: https://dev.to/rohansx/sqlite-as-a-graph-database-recursive-ctes-semantic-search-and-why-we-ditched-neo4j-1ai
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-15-data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-02-24-database-decoded-navigating-queries-in-fastapi-django-orm-vs-raw-sql]]'
- '[[2026-03-20-from-68-to-100-how-we-built-a-text-to-sql-system-that-gets-smarter-every-day]]'
- '[[2026-03-13-postgresql-vs-mysql-vs-sqlite-choosing-the-right-database-for-your-project]]'
status: unread
---

> **TL;DR:** Knowledge graphs are having a moment. Every AI agent framework wants one. The typical stack looks like this: Neo4j for graph storage, OpenAI for extraction, Docker to run it all. Three moving parts, two network dependenc…

## What’s new and why it matters
Knowledge graphs are having a moment. Every AI agent framework wants one. The typical stack looks like this: Neo4j for graph storage, OpenAI for extraction, Docker to run it all. Three moving parts, two network dependencies, one docker-compose.yml you'll fight with for an hour. We built ctxgraph to see how far you can get with just SQLite. The answer: surprisingly far. 0.800 combined F1 on extraction benchmarks, zero API calls, ~2 seconds for 50 episodes, single binary. No Docker. No API keys. No Neo4j. This post walks through the actual implementation: the schema, the recursive CTEs that make…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rohansx/sqlite-as-a-graph-database-recursive-ctes-semantic-search-and-why-we-ditched-neo4j-1ai

## Related notes
- [[2026-03-15-data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-02-24-database-decoded-navigating-queries-in-fastapi-django-orm-vs-raw-sql]]
- [[2026-03-20-from-68-to-100-how-we-built-a-text-to-sql-system-that-gets-smarter-every-day]]
- [[2026-03-13-postgresql-vs-mysql-vs-sqlite-choosing-the-right-database-for-your-project]]
