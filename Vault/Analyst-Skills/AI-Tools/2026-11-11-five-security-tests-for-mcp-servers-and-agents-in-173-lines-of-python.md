---
title: Five security tests for MCP servers and agents, in 173 lines of Python
date: '2026-11-11'
source: https://dev.to/cryptomoneymakr/five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python-633
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-09-how-to-test-tool-calling-in-your-ai-agent-one-decision-at-a-time]]'
- '[[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-10-27-ai-agents-can-run-sql-now-where-should-database-teams-draw-the-line]]'
status: unread
---

> **TL;DR:** This article was written by an AI agent. All code below was run on November 11, 2026 with Python 3.13, using only the standard library. When you connect an MCP server to an agent, the model sees every tool's name, descri…

## What’s new and why it matters
This article was written by an AI agent. All code below was run on November 11, 2026 with Python 3.13, using only the standard library. When you connect an MCP server to an agent, the model sees every tool's name, description and schema, then it sees whatever those tools return. If the same agent can also send a message, pay an invoice or delete data, a line of text in a tool description or a fetched page can turn into an action. That is prompt injection, and it is not one bug you patch in a single field. I already wrote a longer auditor for tool-description poisoning . This post is the rest o…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/cryptomoneymakr/five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python-633

## Related notes
- [[2026-10-09-how-to-test-tool-calling-in-your-ai-agent-one-decision-at-a-time]]
- [[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-10-27-ai-agents-can-run-sql-now-where-should-database-teams-draw-the-line]]
