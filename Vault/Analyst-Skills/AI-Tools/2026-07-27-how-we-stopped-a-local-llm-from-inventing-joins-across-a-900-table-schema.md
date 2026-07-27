---
title: How we stopped a local LLM from inventing JOINs across a 900-table schema
date: '2026-07-27'
source: https://dev.to/__11f7ea740fa6/how-we-stopped-a-local-llm-from-inventing-joins-across-a-900-table-schema-6o0
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]'
- '[[2026-03-01-sql-joins]]'
- '[[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
status: unread
---

> **TL;DR:** Practical notes from building an internal text-to-SQL agent. Everything runs on-prem: a local model behind a LiteLLM proxy, bge-m3 embeddings, Postgres with pgvector for retrieval, and ClickHouse as the target warehouse.…

## What’s new and why it matters
Practical notes from building an internal text-to-SQL agent. Everything runs on-prem: a local model behind a LiteLLM proxy, bge-m3 embeddings, Postgres with pgvector for retrieval, and ClickHouse as the target warehouse. Disclosure: English is not my native language. I wrote the original draft in Russian and used an LLM to help edit and translate it. The system, implementation details, and conclusions described below are my own. TL;DR Reliable text-to-SQL over a large schema is not a prompting problem alone. Finding the right tables and joining them safely are different problems, so we separat…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/__11f7ea740fa6/how-we-stopped-a-local-llm-from-inventing-joins-across-a-900-table-schema-6o0

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]
- [[2026-03-01-sql-joins]]
- [[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
