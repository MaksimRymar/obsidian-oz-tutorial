---
title: Why LLM Agents Still Can't Query NoSQL Databases
date: '2026-06-04'
source: https://dev.to/camma_smith_1/why-llm-agents-still-cant-query-nosql-databases-38ja
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]'
- '[[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]'
- '[[2026-05-13-ai-database-agents-need-result-contracts-not-just-rows]]'
status: unread
---

> **TL;DR:** When it comes to SQL databases, LLMs are great at writing SQL. It's precise, expressive, and unambiguous. LLMs write it well. Connect an MCP server to Postgres and the agent can write queries directly and efficiently. It…

## What’s new and why it matters
When it comes to SQL databases, LLMs are great at writing SQL. It's precise, expressive, and unambiguous. LLMs write it well. Connect an MCP server to Postgres and the agent can write queries directly and efficiently. It's a lot harder for agents to work with NoSQL databases, and given how much production data lives in them, I'm surprised there isn't more discussion about it. Why SQL works so well for LLMs The core reason SQL is a natural interface for language models is specificity. A SQL query says exactly what data you want, in exactly what shape, with exactly what conditions. There's no am…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/camma_smith_1/why-llm-agents-still-cant-query-nosql-databases-38ja

## Related notes
- [[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]
- [[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]
- [[2026-05-13-ai-database-agents-need-result-contracts-not-just-rows]]
