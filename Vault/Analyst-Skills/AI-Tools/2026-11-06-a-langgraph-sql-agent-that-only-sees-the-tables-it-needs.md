---
title: A LangGraph SQL agent that only sees the tables it needs
date: '2026-11-06'
source: https://dev.to/ashish_sinha_5241c7673d93/a-langgraph-sql-agent-that-only-sees-the-tables-it-needs-23no
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-31-my-open-source-text-to-sql-layer-is-1-on-bird-mini-dev-in-all-three-dialects]]'
- '[[2026-10-26-schemagate-is-now-1-on-the-official-bird-mini-dev-leaderboard]]'
- '[[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]'
- '[[2026-11-05-sql-inner-join-vs-left-join-vs-right-join-vs-full-outer-join-differences-with-examples-tested-in-mysql-84-and-sqlite]]'
- '[[2026-04-22-sql-database-architecture-use-cases-and-monitoring-a-practitioners-guide]]'
- '[[2026-10-03-hiding-the-table-is-not-enough-your-llm-can-still-see-the-salary-column]]'
status: unread
---

> **TL;DR:** Most text-to-SQL agents paste the whole schema into every prompt. On a real database, most of it is tables the question never touches, and you pay for them on every call. I added a small LangGraph example to schemagate t…

## What’s new and why it matters
Most text-to-SQL agents paste the whole schema into every prompt. On a real database, most of it is tables the question never touches, and you pay for them on every call. I added a small LangGraph example to schemagate that does it differently. It has four nodes: select_schema : SchemagateRetriever picks the few tables the question needs. This step runs offline, with no model call. write_sql : the model writes one SELECT using only those tables. run_sql : the agent runs the query. If it fails, the error goes back to the model once. answer : the model answers in one sentence from the returned r…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashish_sinha_5241c7673d93/a-langgraph-sql-agent-that-only-sees-the-tables-it-needs-23no

## Related notes
- [[2026-10-31-my-open-source-text-to-sql-layer-is-1-on-bird-mini-dev-in-all-three-dialects]]
- [[2026-10-26-schemagate-is-now-1-on-the-official-bird-mini-dev-leaderboard]]
- [[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]
- [[2026-11-05-sql-inner-join-vs-left-join-vs-right-join-vs-full-outer-join-differences-with-examples-tested-in-mysql-84-and-sqlite]]
- [[2026-04-22-sql-database-architecture-use-cases-and-monitoring-a-practitioners-guide]]
- [[2026-10-03-hiding-the-table-is-not-enough-your-llm-can-still-see-the-salary-column]]
