---
title: In some scenarios, relying on LLMs to generate SQL is neither rigorous nor
  reliable.Right way to teach LLMs to generate SQL is here
date: '2026-05-19'
source: https://dev.to/jaco_siu_748a48197d7f91e9/in-some-scenarios-relying-on-llms-to-generate-sql-is-neither-rigorous-nor-reliable-13c6
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-28-i-built-a-natural-language-to-sql-generator-with-langchain-groq-and-streamlit-full-tutorial]]'
- '[[2026-03-23-generate-er-diagram-from-select-queries-join-analysis-tool]]'
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
- '[[2026-03-10-joins-window-functions]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
status: unread
---

> **TL;DR:** Over the past two years, tools that generate SQL from natural language have become very popular. Type a question in plain English, and an LLM produces SQL for you. It's convenient. But from my experience on real‑world pr…

## What’s new and why it matters
Over the past two years, tools that generate SQL from natural language have become very popular. Type a question in plain English, and an LLM produces SQL for you. It's convenient. But from my experience on real‑world projects, there is a clear problem when business requirements demand high accuracy . This isn't because LLMs are weak. It's because of how they work – non‑deterministically . Three practical issues with LLM‑generated SQL 1. Same question, different answers The same natural language description can lead to different SQL statements. Edge cases may be handled inconsistently. For fin…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/jaco_siu_748a48197d7f91e9/in-some-scenarios-relying-on-llms-to-generate-sql-is-neither-rigorous-nor-reliable-13c6

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-28-i-built-a-natural-language-to-sql-generator-with-langchain-groq-and-streamlit-full-tutorial]]
- [[2026-03-23-generate-er-diagram-from-select-queries-join-analysis-tool]]
- [[2026-05-18-top-orm-tools-practical-comparison]]
- [[2026-03-10-joins-window-functions]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
