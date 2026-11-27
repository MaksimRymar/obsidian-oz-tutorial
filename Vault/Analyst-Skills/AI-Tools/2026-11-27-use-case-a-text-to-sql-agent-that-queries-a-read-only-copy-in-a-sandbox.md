---
title: 'Use case: a text-to-SQL agent that queries a read-only copy in a sandbox'
date: '2026-11-27'
source: https://dev.to/sandscale/use-case-a-text-to-sql-agent-that-queries-a-read-only-copy-in-a-sandbox-1i5b
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-11-06-a-langgraph-sql-agent-that-only-sees-the-tables-it-needs]]'
- '[[2026-11-20-sql-server-columnstore-indexes-fast-reporting-on-large-tables]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-09-30-a-select-that-returned-more-rows-than-its-limit]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
status: unread
---

> **TL;DR:** Text-to-SQL is one of the most useful things to put in front of a model, and one of the easiest to get wrong. The usual risks: The model writes a DELETE or UPDATE , through a prompt injection or a plain mistake. A query…

## What’s new and why it matters
Text-to-SQL is one of the most useful things to put in front of a model, and one of the easiest to get wrong. The usual risks: The model writes a DELETE or UPDATE , through a prompt injection or a plain mistake. A query scans a huge table and takes the production database with it. Results with personal data flow into the conversation. The model is pointed at more data than the question needs. This use case answers questions over a copy of the data, in a Sandscale sandbox , opened read-only. The production database never sees the model's SQL. The shape Export the tables the agent needs to a SQL…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sandscale/use-case-a-text-to-sql-agent-that-queries-a-read-only-copy-in-a-sandbox-1i5b

## Related notes
- [[2026-11-06-a-langgraph-sql-agent-that-only-sees-the-tables-it-needs]]
- [[2026-11-20-sql-server-columnstore-indexes-fast-reporting-on-large-tables]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-09-30-a-select-that-returned-more-rows-than-its-limit]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
