---
title: I tested 5 LLMs for prompt-injection leaks. Same code, 0% to 90%.
date: '2026-06-18'
source: https://dev.to/leeryeong/i-tested-5-llms-for-prompt-injection-leaks-same-code-0-to-90-g34
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#tool'
related:
- '[[2026-03-20-your-ai-agent-will-be-prompt-injected-heres-how-to-defend-it]]'
- '[[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]'
- '[[2026-04-06-i-built-an-open-source-benchmark-that-scores-ai-agents-not-models]]'
- '[[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]'
- '[[2026-04-30-how-attackers-hijack-llm-agents-and-how-to-stop-them]]'
- '[[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]'
status: unread
---

> **TL;DR:** I built a scanner that fires prompt-injection probes at a self-hosted AI agent and checks whether it leaks (a) real secret-shaped strings (API keys) or (b) the content of its own system prompt. Then I ran the same agent…

## What’s new and why it matters
I built a scanner that fires prompt-injection probes at a self-hosted AI agent and checks whether it leaks (a) real secret-shaped strings (API keys) or (b) the content of its own system prompt. Then I ran the same agent across 5 model backends. The leak rate ranged from 0% to 90% depending only on the model. Here's what I found and how it works. Why this matters now Prompt injection is #1 on the OWASP 2025 LLM Top 10. It's not theoretical anymore: EchoLeak (CVE-2025-32711, CVSS 9.3) — a zero-click flaw in Microsoft 365 Copilot. One crafted email could exfiltrate internal files and API keys wit…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/leeryeong/i-tested-5-llms-for-prompt-injection-leaks-same-code-0-to-90-g34

## Related notes
- [[2026-03-20-your-ai-agent-will-be-prompt-injected-heres-how-to-defend-it]]
- [[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]
- [[2026-04-06-i-built-an-open-source-benchmark-that-scores-ai-agents-not-models]]
- [[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]
- [[2026-04-30-how-attackers-hijack-llm-agents-and-how-to-stop-them]]
- [[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]
