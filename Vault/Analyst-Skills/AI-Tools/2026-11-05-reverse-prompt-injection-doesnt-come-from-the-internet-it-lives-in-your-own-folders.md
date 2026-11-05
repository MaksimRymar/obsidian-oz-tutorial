---
title: 'Reverse Prompt Injection doesn''t come from the internet: it lives in your
  own folders'
date: '2026-11-05'
source: https://dev.to/yonijd/reverse-prompt-injection-doesnt-come-from-the-internet-it-lives-in-your-own-folders-part-1-21c9
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#presentations'
- '#sql'
- '#tool'
related:
- '[[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-06-22-the-ai-security-gap-why-your-autonomous-agents-are-completely-unprotected]]'
- '[[2026-11-04-i-gave-ai-agents-a-video-downloader-building-a-remote-mcp-server-in-python]]'
- '[[2026-03-10-building-a-production-ready-agentic-ai-system-with-langgraph-and-mcp]]'
- '[[2026-06-26-i-built-a-tool-that-found-my-langgraph-email-agent-could-be-hijacked-to-forward-the-entire-inbox-to-an-attacker]]'
status: unread
---

> **TL;DR:** We all look for Reverse Prompt Injection outside. We assume the attack vector lives on a malicious website, inside a downloaded PDF, or through a third-party API. I found it inside . On my own drive, while building the d…

## What’s new and why it matters
We all look for Reverse Prompt Injection outside. We assume the attack vector lives on a malicious website, inside a downloaded PDF, or through a third-party API. I found it inside . On my own drive, while building the demo video for WAIO (Web AI Orchestrator) . If you are not familiar with it, WAIO is a local engine that gives hands to web AIs: the AI generates a structured JSON, WAIO detects it in the downloads folder, and executes it locally (no APIs, no tokens). During my tests, I discovered something both fascinating and alarming: the environment turns into a prompt . The Experiment: Pass…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/yonijd/reverse-prompt-injection-doesnt-come-from-the-internet-it-lives-in-your-own-folders-part-1-21c9

## Related notes
- [[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-06-22-the-ai-security-gap-why-your-autonomous-agents-are-completely-unprotected]]
- [[2026-11-04-i-gave-ai-agents-a-video-downloader-building-a-remote-mcp-server-in-python]]
- [[2026-03-10-building-a-production-ready-agentic-ai-system-with-langgraph-and-mcp]]
- [[2026-06-26-i-built-a-tool-that-found-my-langgraph-email-agent-could-be-hijacked-to-forward-the-entire-inbox-to-an-attacker]]
