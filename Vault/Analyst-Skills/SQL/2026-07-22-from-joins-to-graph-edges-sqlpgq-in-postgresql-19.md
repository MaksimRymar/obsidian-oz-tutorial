---
title: 'From Joins to Graph Edges: SQL/PGQ in PostgreSQL 19'
date: '2026-07-22'
source: https://dev.to/franckpachot/from-joins-to-graph-edges-sqlpgq-in-postgresql-19-2doo
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-06-24-semantic-search-with-postgresql-pragmatism-beats-hype---most-of-the-time]]'
- '[[2026-03-02-designing-efficient-queries-with-sql-joins-and-window-functions]]'
- '[[2026-07-21-from-tables-to-insights-a-beginners-journey-into-sql]]'
status: unread
---

> **TL;DR:** In the previous post, Cypher graph queries on PostgreSQL with Apache AGE , I showed how to model and query a property graph in PostgreSQL using Apache AGE. The graph was materialized as vertices and edges stored in dedic…

## What’s new and why it matters
In the previous post, Cypher graph queries on PostgreSQL with Apache AGE , I showed how to model and query a property graph in PostgreSQL using Apache AGE. The graph was materialized as vertices and edges stored in dedicated tables. PostgreSQL 19, currently in beta, takes a different route for built-in support of graph queries. With SQL/PGQ, a property graph is defined as a logical model on top of existing relational tables, without duplicating the underlying data. In short: Apache AGE: the graph is a stored data structure. SQL/PGQ: the graph is a semantic layer over relational data. Unlike gr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/franckpachot/from-joins-to-graph-edges-sqlpgq-in-postgresql-19-2doo

## Related notes
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-05-18-top-orm-tools-practical-comparison]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-06-24-semantic-search-with-postgresql-pragmatism-beats-hype---most-of-the-time]]
- [[2026-03-02-designing-efficient-queries-with-sql-joins-and-window-functions]]
- [[2026-07-21-from-tables-to-insights-a-beginners-journey-into-sql]]
