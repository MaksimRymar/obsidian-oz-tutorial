---
title: Post Apache Ossie, what distinguishes semantic layers?
date: '2026-09-14'
source: https://dev.to/motley/post-apache-ossie-what-distinguishes-semantic-layers-45m2
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#support-analytics'
- '#tableau'
- '#tool'
related:
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-06-18-building-an-mcp-sql-tool-that-lets-llms-query-live-databases-with-wanaku]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-05-12-schema-context-is-the-missing-layer-for-ai-database-agents]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-05-31-how-to-build-an-agent-using-coral]]'
status: unread
---

> **TL;DR:** Enough has been said recently about why having a semantic layer is a good thing. Unfortunately, each of them has its own data model and corresponding storage format for storing those models, so migrating from one to anot…

## What’s new and why it matters
Enough has been said recently about why having a semantic layer is a good thing. Unfortunately, each of them has its own data model and corresponding storage format for storing those models, so migrating from one to another was a nontrivial endeavour. Apache Ossie sets out to change that. It is an open-source standard for describing semantic layer models, with a lot of heavy hitters behind it. It's early days yet, and it only defines the semantic model interchange format, but with the kind of backers it has, it seems very likely it will get broad adoption (the obligatory xkcd comes to mind). T…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/motley/post-apache-ossie-what-distinguishes-semantic-layers-45m2

## Related notes
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-06-18-building-an-mcp-sql-tool-that-lets-llms-query-live-databases-with-wanaku]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-05-12-schema-context-is-the-missing-layer-for-ai-database-agents]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-05-31-how-to-build-an-agent-using-coral]]
