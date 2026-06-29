---
title: 'One query language for SQL, Mongo, and the browser: the case for Forge'
date: '2026-06-28'
source: https://dev.to/johnsonfash/one-query-language-for-sql-mongo-and-the-browser-the-case-for-forge-247o
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]'
- '[[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]'
status: unread
---

> **TL;DR:** There's a moment in most TypeScript backend projects when the data layer stops being one thing. Maybe you started on Postgres, then a feature shipped where audit events made more sense as a flat Mongo document. Maybe you…

## What’s new and why it matters
There's a moment in most TypeScript backend projects when the data layer stops being one thing. Maybe you started on Postgres, then a feature shipped where audit events made more sense as a flat Mongo document. Maybe your mobile app needs to work on the train, so you added SQLite in the browser. Maybe a "find me the three nearest locations" endpoint forced you to drop into raw ST_Distance_Sphere() because your ORM didn't know what a geo point was. Maybe you added embeddings for an AI search box and now half your query path is a $queryRaw with a hand-rolled vector cosine clause. Each of those m…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/johnsonfash/one-query-language-for-sql-mongo-and-the-browser-the-case-for-forge-247o

## Related notes
- [[2026-05-18-top-orm-tools-practical-comparison]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]
- [[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]
