---
title: 'schemagate: 91% fewer schema tokens for text-to-SQL, and only the tables the
  caller may read'
date: '2026-11-23'
source: https://dev.to/ashish_sinha_5241c7673d93/schemagate-91-fewer-schema-tokens-for-text-to-sql-and-only-the-tables-the-caller-may-read-1df5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
related:
- '[[2026-11-18-text-to-sql-on-oracle-637-first-try-on-a-benchmark-my-bug-reports-helped-fix]]'
- '[[2026-11-13-one-constant-was-costing-my-schema-retriever-17-points]]'
- '[[2026-11-06-a-langgraph-sql-agent-that-only-sees-the-tables-it-needs]]'
- '[[2026-10-26-schemagate-is-now-1-on-the-official-bird-mini-dev-leaderboard]]'
- '[[2026-10-31-my-open-source-text-to-sql-layer-is-1-on-bird-mini-dev-in-all-three-dialects]]'
- '[[2026-10-19-schemagate-tops-bird-mini-dev-in-sqlite-postgresql-and-mysql]]'
status: unread
---

> **TL;DR:** Text-to-SQL prompts usually carry the whole database schema, and pay for it on every question. schemagate sends the model only the tables a question needs, and only the ones the person asking may read. 91% fewer schema t…

## What’s new and why it matters
Text-to-SQL prompts usually carry the whole database schema, and pay for it on every question. schemagate sends the model only the tables a question needs, and only the ones the person asking may read. 91% fewer schema tokens on real warehouses (Spider 2.0, databases with 50+ tables, median) #1 on UniQL Oracle: 64.93%, ahead of Claude-4.5-Sonnet (49.61) #1 on BIRD Mini-Dev Legacy: SQLite 81.0 · MySQL 72.4 · PostgreSQL 72.6 LiveSQLBench-Large: 34.58%, #9 among agents; the BIRD team is adding it to the board In LangChain's official integrations as SchemagateRetriever ( pip install langchain-sche…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashish_sinha_5241c7673d93/schemagate-91-fewer-schema-tokens-for-text-to-sql-and-only-the-tables-the-caller-may-read-1df5

## Related notes
- [[2026-11-18-text-to-sql-on-oracle-637-first-try-on-a-benchmark-my-bug-reports-helped-fix]]
- [[2026-11-13-one-constant-was-costing-my-schema-retriever-17-points]]
- [[2026-11-06-a-langgraph-sql-agent-that-only-sees-the-tables-it-needs]]
- [[2026-10-26-schemagate-is-now-1-on-the-official-bird-mini-dev-leaderboard]]
- [[2026-10-31-my-open-source-text-to-sql-layer-is-1-on-bird-mini-dev-in-all-three-dialects]]
- [[2026-10-19-schemagate-tops-bird-mini-dev-in-sqlite-postgresql-and-mysql]]
