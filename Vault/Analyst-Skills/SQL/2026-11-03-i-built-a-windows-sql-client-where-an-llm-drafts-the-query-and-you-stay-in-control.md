---
title: I built a Windows SQL client where an LLM drafts the query and you stay in
  control
date: '2026-11-03'
source: https://dev.to/mirinai_ai/i-built-a-windows-sql-client-where-an-llm-drafts-the-query-and-you-stay-in-control-1j3i
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]'
- '[[2026-09-07-ottoch---ask-your-database-questions-in-you-plain-language-self-hosted]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-03-30-dataai-a-local-ai-database-client-from-plain-language-to-executable-sql]]'
- '[[2026-10-29-it-passed-every-constraint-it-was-still-wrong]]'
- '[[2026-08-20-read-only-by-design-letting-ai-explore-your-database-without-the-risk-of-writes]]'
status: unread
---

> **TL;DR:** Disclosure: I work at Mirinai and built this app. This post was drafted with the help of AI and reviewed by me. Letting an LLM near a database worries me in two ways: what leaves my machine, and what happens if the gener…

## What’s new and why it matters
Disclosure: I work at Mirinai and built this app. This post was drafted with the help of AI and reviewed by me. Letting an LLM near a database worries me in two ways: what leaves my machine, and what happens if the generated SQL is wrong. I built Chat DB Manager, a Windows desktop database client, around those two questions. You ask a question in plain language and the app fills the editor with SQL for the connected DBMS. Nothing runs until you read it and press Run. What goes to the LLM Default mode (SQL Helper) sends the schema in a compact notation (tables, columns, types, keys, comments, i…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mirinai_ai/i-built-a-windows-sql-client-where-an-llm-drafts-the-query-and-you-stay-in-control-1j3i

## Related notes
- [[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]
- [[2026-09-07-ottoch---ask-your-database-questions-in-you-plain-language-self-hosted]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-03-30-dataai-a-local-ai-database-client-from-plain-language-to-executable-sql]]
- [[2026-10-29-it-passed-every-constraint-it-was-still-wrong]]
- [[2026-08-20-read-only-by-design-letting-ai-explore-your-database-without-the-risk-of-writes]]
