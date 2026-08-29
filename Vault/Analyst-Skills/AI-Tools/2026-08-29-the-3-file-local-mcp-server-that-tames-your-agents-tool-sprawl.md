---
title: The 3-File Local MCP Server That Tames Your Agent's Tool Sprawl
date: '2026-08-29'
source: https://dev.to/syed_anzar/the-3-file-local-mcp-server-that-tames-your-agents-tool-sprawl-4iom
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]'
- '[[2026-06-22-how-i-cut-my-llm-api-bill-by-80-with-a-simple-router]]'
- '[[2026-08-24-i-added-cryptographic-receipts-to-mcp-tool-calls-in-20-lines-of-code]]'
- '[[2026-08-08-how-to-set-up-a-sql-database-for-beginners]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
status: unread
---

> **TL;DR:** The 3-File Local MCP Server That Tames Your Agent's Tool Sprawl Your agent can already call a dozen tools — but they're scattered across three repos, each with its own transport, its own hand-rolled JSON-RPC framing, and…

## What’s new and why it matters
The 3-File Local MCP Server That Tames Your Agent's Tool Sprawl Your agent can already call a dozen tools — but they're scattered across three repos, each with its own transport, its own hand-rolled JSON-RPC framing, and its own half-broken schema validation. The Model Context Protocol (MCP) exists to kill that sprawl: it's "a web API, but designed for LLM interactions." And the 2026-era Python SDK lets you stand up a real, secure, local server in three files — no cloud, no boilerplate, no protocol code you have to maintain. This is a working, copy-paste server that exposes your Markdown notes…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/syed_anzar/the-3-file-local-mcp-server-that-tames-your-agents-tool-sprawl-4iom

## Related notes
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]
- [[2026-06-22-how-i-cut-my-llm-api-bill-by-80-with-a-simple-router]]
- [[2026-08-24-i-added-cryptographic-receipts-to-mcp-tool-calls-in-20-lines-of-code]]
- [[2026-08-08-how-to-set-up-a-sql-database-for-beginners]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
