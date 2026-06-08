---
title: Building an agentic Jira automation platform with MCP and Temporal
date: '2026-06-08'
source: https://dev.to/ahmetozel/building-an-agentic-jira-automation-platform-with-mcp-and-temporal-1521
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#python'
- '#tool'
- '#zendesk'
related:
- '[[2026-05-23-how-to-build-a-supervisor-agent-architecture-without-frameworks]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-05-15-stop-passing-entire-chat-histories-to-ai-agents]]'
- '[[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]'
- '[[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]'
status: unread
---

> **TL;DR:** Most "AI automation" demos fall apart the moment a workflow needs to run longer than a single request. An agent makes a few tool calls, the process crashes or times out, and you lose all state. I wanted something that co…

## What’s new and why it matters
Most "AI automation" demos fall apart the moment a workflow needs to run longer than a single request. An agent makes a few tool calls, the process crashes or times out, and you lose all state. I wanted something that could drive real, multi-step work inside Atlassian (Jira and Confluence) and survive restarts, retries, and failures. So I built an open-source platform around two ideas: MCP for tool access and Temporal for durable execution. Repo: https://github.com/ahmet-ozel/atlassian-ai-workflow-platform The problem with one-shot agents A typical agent loop looks like: read a ticket, decide…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ahmetozel/building-an-agentic-jira-automation-platform-with-mcp-and-temporal-1521

## Related notes
- [[2026-05-23-how-to-build-a-supervisor-agent-architecture-without-frameworks]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-05-15-stop-passing-entire-chat-histories-to-ai-agents]]
- [[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]
- [[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]
