---
title: Claude Code to Outlook via pywin32 — no MCP, no permission, no problem.
date: '2026-06-29'
source: https://dev.to/joseph_solomon_20a1569494/claude-code-to-outlook-via-pywin32-no-mcp-no-permission-no-problem-113b
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-25-i-stopped-fighting-the-reddit-api-so-i-built-supermcp-to-read-it-for-me]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-03-14-claude-code-practical-guide-debugging-test-automation-and-cuda-environment-setup-with-opus-46]]'
- '[[2026-04-20-try-asqav-in-30-seconds]]'
- '[[2026-04-13-python-314-free-threading-real-benchmarks-real-breakage-real-code]]'
- '[[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]'
status: unread
---

> **TL;DR:** I work on a locked-down enterprise Windows machine. Can't register an Azure app. Can't install browser extensions. Managed device — IT controls what's approved. I still needed Claude Code to read and draft my emails. The…

## What’s new and why it matters
I work on a locked-down enterprise Windows machine. Can't register an Azure app. Can't install browser extensions. Managed device — IT controls what's approved. I still needed Claude Code to read and draft my emails. The fix turned out to be simpler than I expected. What COM automation actually is Outlook Desktop on Windows exposes a COM interface. It's been there since the 90s. Any program running on the same machine can connect to it, provided Outlook is open and signed in. That's the whole authentication model: if Outlook is running, you're in. pywin32 wraps this interface in Python: import…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/joseph_solomon_20a1569494/claude-code-to-outlook-via-pywin32-no-mcp-no-permission-no-problem-113b

## Related notes
- [[2026-04-25-i-stopped-fighting-the-reddit-api-so-i-built-supermcp-to-read-it-for-me]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-03-14-claude-code-practical-guide-debugging-test-automation-and-cuda-environment-setup-with-opus-46]]
- [[2026-04-20-try-asqav-in-30-seconds]]
- [[2026-04-13-python-314-free-threading-real-benchmarks-real-breakage-real-code]]
- [[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]
