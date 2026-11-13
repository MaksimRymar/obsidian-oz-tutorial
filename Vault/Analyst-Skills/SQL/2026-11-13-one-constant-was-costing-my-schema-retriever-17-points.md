---
title: One constant was costing my schema retriever 17 points
date: '2026-11-13'
source: https://dev.to/ashish_sinha_5241c7673d93/one-constant-was-costing-my-schema-retriever-17-points-l19
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-10-26-schemagate-is-now-1-on-the-official-bird-mini-dev-leaderboard]]'
- '[[2026-10-31-my-open-source-text-to-sql-layer-is-1-on-bird-mini-dev-in-all-three-dialects]]'
- '[[2026-10-24-what-one-month-of-public-benchmarks-says-about-my-text-to-sql-access-layer]]'
- '[[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]'
- '[[2026-10-19-schemagate-tops-bird-mini-dev-in-sqlite-postgresql-and-mysql]]'
- '[[2026-04-22-sql-database-architecture-use-cases-and-monitoring-a-practitioners-guide]]'
status: unread
---

> **TL;DR:** If your warehouse columns are called questregistry and climtune , keyword search picks the wrong tables, and the model writes confident SQL against them. schemagate sends the model only the tables a question needs and th…

## What’s new and why it matters
If your warehouse columns are called questregistry and climtune , keyword search picks the wrong tables, and the model writes confident SQL against them. schemagate sends the model only the tables a question needs and the caller may read: 91.1% fewer schema tokens (median, databases with 50+ tables). #1 on BIRD's Mini-Dev leaderboard in SQLite / PostgreSQL / MySQL (81.0 / 72.6 / 72.4 EX, official board); 74.34 EX on BIRD's hidden test set , scored by the BIRD team. Listed in LangChain's retriever docs, usable from LangGraph. What I found Snowflake's SQL-Schema-Retrieval benchmark (arXiv 2607.1…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashish_sinha_5241c7673d93/one-constant-was-costing-my-schema-retriever-17-points-l19

## Related notes
- [[2026-10-26-schemagate-is-now-1-on-the-official-bird-mini-dev-leaderboard]]
- [[2026-10-31-my-open-source-text-to-sql-layer-is-1-on-bird-mini-dev-in-all-three-dialects]]
- [[2026-10-24-what-one-month-of-public-benchmarks-says-about-my-text-to-sql-access-layer]]
- [[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]
- [[2026-10-19-schemagate-tops-bird-mini-dev-in-sqlite-postgresql-and-mysql]]
- [[2026-04-22-sql-database-architecture-use-cases-and-monitoring-a-practitioners-guide]]
