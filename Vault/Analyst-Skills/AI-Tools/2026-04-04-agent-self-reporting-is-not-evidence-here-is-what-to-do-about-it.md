---
title: Agent Self-Reporting Is Not Evidence. Here Is What to Do About It.
date: '2026-04-04'
source: https://dev.to/arkforge-ceo/agent-self-reporting-is-not-evidence-here-is-what-to-do-about-it-35pc
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]'
- '[[2026-03-02-five-things-that-break-in-production-that-anthropics-free-curriculum-skips]]'
- '[[2026-03-08-data-engineers-what-if-your-bigquery-function-could-return-multiple-tables]]'
- '[[2026-03-28-the-execution-guard-pattern-for-ai-agents]]'
status: unread
---

> **TL;DR:** MCP agents self-report their actions. When a tool call returns 'email sent', nothing independent confirms it actually happened. Here is how to add client-side verification to MCP tool calls with cryptographic receipts. A…

## What’s new and why it matters
MCP agents self-report their actions. When a tool call returns 'email sent', nothing independent confirms it actually happened. Here is how to add client-side verification to MCP tool calls with cryptographic receipts. Agent Self-Reporting Is Not Evidence. Here Is What to Do About It. Your agent just ran send_email . It returned {"status": "sent", "to": "alice@company.com", "timestamp": "2026-04-04T14:03:12Z"} . That response is a string produced by a tool running on a server you may not control. Between "agent invoked the tool" and "task complete", nothing independent confirms that the report…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/arkforge-ceo/agent-self-reporting-is-not-evidence-here-is-what-to-do-about-it-35pc

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]
- [[2026-03-02-five-things-that-break-in-production-that-anthropics-free-curriculum-skips]]
- [[2026-03-08-data-engineers-what-if-your-bigquery-function-could-return-multiple-tables]]
- [[2026-03-28-the-execution-guard-pattern-for-ai-agents]]
