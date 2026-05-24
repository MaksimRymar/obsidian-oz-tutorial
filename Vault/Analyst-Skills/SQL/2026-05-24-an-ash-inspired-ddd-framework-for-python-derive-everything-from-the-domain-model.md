---
title: 'An Ash-Inspired DDD Framework for Python: Derive Everything from the Domain
  Model'
date: '2026-05-24'
source: https://dev.to/sahil_pohare/an-ash-inspired-ddd-framework-for-python-derive-everything-from-the-domain-model-890
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-05-06-four-ways-to-use-ai-with-your-database-in-vs-code]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]'
- '[[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
status: unread
---

> **TL;DR:** I've been building PingerAgents — a multitenant AI agent orchestration platform. Along the way I ended up writing something that felt worth writing up on its own: a domain-driven design framework for Python that derives…

## What’s new and why it matters
I've been building PingerAgents — a multitenant AI agent orchestration platform. Along the way I ended up writing something that felt worth writing up on its own: a domain-driven design framework for Python that derives persistence, durable execution handlers, and tenant isolation from a single resource class. It's inspired by Elixir's Ash framework . This is a writeup of what it is, how it works, and the mistakes made building it. The Problem with Backend Glue Most backend code isn't business logic. It's wiring. You write a domain object, then you write: A SQLAlchemy model to persist it A rep…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sahil_pohare/an-ash-inspired-ddd-framework-for-python-derive-everything-from-the-domain-model-890

## Related notes
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-05-06-four-ways-to-use-ai-with-your-database-in-vs-code]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]
- [[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
