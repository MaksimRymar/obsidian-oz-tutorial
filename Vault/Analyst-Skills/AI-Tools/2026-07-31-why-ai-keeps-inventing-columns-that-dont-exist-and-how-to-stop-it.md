---
title: Why AI Keeps Inventing Columns That Don't Exist (and How to Stop It)
date: '2026-07-31'
source: https://dev.to/vivekdraxlr/why-ai-keeps-inventing-columns-that-dont-exist-and-how-to-stop-it-2h9h
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-07-08-how-to-use-ai-to-write-sql-queries-from-plain-english]]'
- '[[2026-06-05-i-built-the-centralized-us-business-entity-api-that-doesnt-exist-with-an-mcp-server-for-ai-agents]]'
- '[[2026-07-16-natural-language-sql-needs-guardrails-not-just-better-prompts]]'
status: unread
---

> **TL;DR:** You ask an AI assistant for "total revenue by customer last month," it hands back a clean-looking query, you run it, and Postgres throws: ERROR : column "c.total_revenue" does not exist LINE 3 : SUM ( c . total_revenue )…

## What’s new and why it matters
You ask an AI assistant for "total revenue by customer last month," it hands back a clean-looking query, you run it, and Postgres throws: ERROR : column "c.total_revenue" does not exist LINE 3 : SUM ( c . total_revenue ) AS revenue The query was confident. It was syntactically perfect. It was also referencing a column that has never existed in your schema. Welcome to the single most common failure mode of AI-generated SQL: the schema hallucination . If you've spent any time using LLMs to write queries, you've hit this. The model invents a total_revenue column, joins to an accounts table you do…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vivekdraxlr/why-ai-keeps-inventing-columns-that-dont-exist-and-how-to-stop-it-2h9h

## Related notes
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-07-08-how-to-use-ai-to-write-sql-queries-from-plain-english]]
- [[2026-06-05-i-built-the-centralized-us-business-entity-api-that-doesnt-exist-with-an-mcp-server-for-ai-agents]]
- [[2026-07-16-natural-language-sql-needs-guardrails-not-just-better-prompts]]
