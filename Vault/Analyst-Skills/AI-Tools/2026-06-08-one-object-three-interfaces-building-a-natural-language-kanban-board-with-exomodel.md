---
title: 'One object, three interfaces: building a natural-language Kanban board with
  ExoModel'
date: '2026-06-08'
source: https://dev.to/pessoabuilds/one-object-three-interfaces-building-a-natural-language-kanban-board-with-exomodel-bhl
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-04-how-i-built-an-agentic-coding-cli-from-scratch]]'
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
- '[[2026-06-05-i-built-the-centralized-us-business-entity-api-that-doesnt-exist-with-an-mcp-server-for-ai-agents]]'
- '[[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]'
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
status: unread
---

> **TL;DR:** Every interface you add to an AI-powered app comes with a tax: an intent router written by hand, for that interface, parsing the same instructions your other interfaces already handle. CLI gets one. Telegram gets another…

## What’s new and why it matters
Every interface you add to an AI-powered app comes with a tax: an intent router written by hand, for that interface, parsing the same instructions your other interfaces already handle. CLI gets one. Telegram gets another. MCP gets a third. By the third interface, you're not building a product — you're maintaining parsers. ExoKanban is a personal Kanban board where all three interfaces — CLI, Telegram bot, and MCP server — share the same object with zero duplicated routing logic. Here's how it's built, and why the architecture looks the way it does. The foundation: an active Card Every task in…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/pessoabuilds/one-object-three-interfaces-building-a-natural-language-kanban-board-with-exomodel-bhl

## Related notes
- [[2026-05-04-how-i-built-an-agentic-coding-cli-from-scratch]]
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
- [[2026-06-05-i-built-the-centralized-us-business-entity-api-that-doesnt-exist-with-an-mcp-server-for-ai-agents]]
- [[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]
- [[2026-05-18-top-orm-tools-practical-comparison]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
