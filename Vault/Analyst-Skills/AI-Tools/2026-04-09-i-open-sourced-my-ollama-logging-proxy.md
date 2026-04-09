---
title: I Open-Sourced My Ollama Logging Proxy
date: '2026-04-09'
source: https://dev.to/bash-thedev/i-open-sourced-my-ollama-logging-proxy-i3p
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
status: unread
---

> **TL;DR:** When you use a cloud LLM API, you get usage data for free. Token counts, latency, cost per request, all tracked and queryable. When you run Ollama locally, you get a response and nothing else. No logs, no token counts, n…

## What’s new and why it matters
When you use a cloud LLM API, you get usage data for free. Token counts, latency, cost per request, all tracked and queryable. When you run Ollama locally, you get a response and nothing else. No logs, no token counts, no way to tell which of your services is eating all the inference time. I had 5 services and a workflow engine all hitting the same Ollama instance on a Mac mini with 24GB of RAM. I couldn't tell which service was the heaviest consumer, whether my model-swapping strategy was working, or if specific workflows were making redundant calls. I was flying blind. So I built a transpare…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/bash-thedev/i-open-sourced-my-ollama-logging-proxy-i3p

## Related notes
- [[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
