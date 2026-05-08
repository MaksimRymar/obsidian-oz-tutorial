---
title: I built an AI agent that does OSINT investigations from your terminal
date: '2026-05-08'
source: https://dev.to/sonotommy/i-built-an-ai-agent-that-does-osint-investigations-from-your-terminal-22jh
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-05-04-how-i-built-an-agentic-coding-cli-from-scratch]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
- '[[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]'
- '[[2026-04-25-build-your-first-ai-agent-in-60-lines-of-python-no-framework-needed]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
status: unread
---

> **TL;DR:** Most OSINT tools are great at one thing. You run holehe for emails, sherlock for usernames, sublist3r for domains. But you're the one deciding the workflow, switching between tools, copy-pasting results. I wanted to remo…

## What’s new and why it matters
Most OSINT tools are great at one thing. You run holehe for emails, sherlock for usernames, sublist3r for domains. But you're the one deciding the workflow, switching between tools, copy-pasting results. I wanted to remove that middle layer. So I built OpenOSINT — you describe a target in plain English, the AI figures out what to investigate and how, runs the tools, and hands you a report. How it works The core idea is simple: instead of hardcoding a fixed pipeline, I use Claude's native tool use API to let the model decide at each step what to do next based on what it found so far. you ❯ inve…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sonotommy/i-built-an-ai-agent-that-does-osint-investigations-from-your-terminal-22jh

## Related notes
- [[2026-05-04-how-i-built-an-agentic-coding-cli-from-scratch]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
- [[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]
- [[2026-04-25-build-your-first-ai-agent-in-60-lines-of-python-no-framework-needed]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
