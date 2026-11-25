---
title: Why Prompt Firewalls Miss AI Agent Privilege Escalation (and How to Intercept
  Tool Calls at Runtime)
date: '2026-11-25'
source: https://dev.to/purvanshbhatt/why-prompt-firewalls-miss-ai-agent-privilege-escalation-and-how-to-intercept-tool-calls-at-runtime-eog
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-09-07-score-the-trace-not-the-final-payload]]'
- '[[2026-10-28-build-an-mcp-server-in-c-that-safely-queries-sql-server]]'
- '[[2026-06-15-a-40-line-llm-based-bash-command-executor-in-python]]'
- '[[2026-11-04-backend-interview-question-why-does-loading-20-orders-run-21-queries]]'
status: unread
---

> **TL;DR:** Most AI security gateways check what enters the model and stop watching once inference begins. That gap breaks down the moment an autonomous agent can run SQL queries, fetch URLs, or invoke shell tools. An indirect promp…

## What’s new and why it matters
Most AI security gateways check what enters the model and stop watching once inference begins. That gap breaks down the moment an autonomous agent can run SQL queries, fetch URLs, or invoke shell tools. An indirect prompt injection hidden in a retrieved ticket or web page can pass an input classifier, persuade the model to build a malicious tool payload, and reach your execution layer unchallenged. To close that gap, you need a deterministic boundary between the model's tool intent and the underlying OS, database, or network runtime. While building ToolShield (an MIT-licensed Python runtime pr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/purvanshbhatt/why-prompt-firewalls-miss-ai-agent-privilege-escalation-and-how-to-intercept-tool-calls-at-runtime-eog

## Related notes
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-09-07-score-the-trace-not-the-final-payload]]
- [[2026-10-28-build-an-mcp-server-in-c-that-safely-queries-sql-server]]
- [[2026-06-15-a-40-line-llm-based-bash-command-executor-in-python]]
- [[2026-11-04-backend-interview-question-why-does-loading-20-orders-run-21-queries]]
