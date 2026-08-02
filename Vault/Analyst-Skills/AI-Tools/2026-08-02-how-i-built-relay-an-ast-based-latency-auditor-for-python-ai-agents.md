---
title: 'How I built Relay: An AST-based latency auditor for Python AI agents'
date: '2026-08-02'
source: https://dev.to/abdur_rafay_ar/how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents-2jaj
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#tool'
related:
- '[[2026-06-09-how-i-messed-up-ai-streaming-and-how-you-can-avoid-it]]'
- '[[2026-02-22-i-built-an-ai-system-that-generates-trading-signals-across-4-stock-markets-heres-how]]'
- '[[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]'
- '[[2026-05-08-how-i-built-an-api-that-cuts-llm-token-costs-by-11-22]]'
- '[[2026-07-07-i-turned-a-claude-code-only-web-reader-into-a-normal-mcp-server]]'
- '[[2026-07-19-how-i-built-a-9-ai-agent-toolkit-that-automates-my-entire-workflow]]'
status: unread
---

> **TL;DR:** I kept running into the same problem building AI agents. They were slow and I had no idea why. No obvious errors, logs looked fine, but requests were taking way longer than they should. Turns out the codebase was full of…

## What’s new and why it matters
I kept running into the same problem building AI agents. They were slow and I had no idea why. No obvious errors, logs looked fine, but requests were taking way longer than they should. Turns out the codebase was full of async anti-patterns. Missing awaits, sequential LLM calls that could've been parallel, blocking I/O hiding inside async functions. So I built Relay. It uses AST analysis to scan your agent codebase and find exactly these spots. Not just flagging them, it suggests fixes too. And since it runs as an MCP server, it works directly inside Claude Code. No log files, no context switc…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/abdur_rafay_ar/how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents-2jaj

## Related notes
- [[2026-06-09-how-i-messed-up-ai-streaming-and-how-you-can-avoid-it]]
- [[2026-02-22-i-built-an-ai-system-that-generates-trading-signals-across-4-stock-markets-heres-how]]
- [[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]
- [[2026-05-08-how-i-built-an-api-that-cuts-llm-token-costs-by-11-22]]
- [[2026-07-07-i-turned-a-claude-code-only-web-reader-into-a-normal-mcp-server]]
- [[2026-07-19-how-i-built-a-9-ai-agent-toolkit-that-automates-my-entire-workflow]]
