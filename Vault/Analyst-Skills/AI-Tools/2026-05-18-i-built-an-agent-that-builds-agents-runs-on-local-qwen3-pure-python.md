---
title: I built an agent that builds agents — runs on local Qwen3, pure Python.
date: '2026-05-18'
source: https://dev.to/0c33/i-built-an-agent-that-builds-agents-runs-on-local-qwen3-pure-python-2hjp
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#python'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-06-i-built-an-open-source-benchmark-that-scores-ai-agents-not-models]]'
- '[[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]'
- '[[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]'
- '[[2026-04-02-im-an-ai-agent-that-built-its-own-training-data-pipeline]]'
- '[[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]'
- '[[2026-04-08-your-ai-agent-is-reading-poisoned-web-pages-heres-how-to-stop-it]]'
status: unread
---

> **TL;DR:** Hi, I built this agentic AI system. Closed-loop — takes a raw idea, ships a standalone .py agent file. What's different: Interviews you until it understands the request before building anything Two testing stages: prompt…

## What’s new and why it matters
Hi, I built this agentic AI system. Closed-loop — takes a raw idea, ships a standalone .py agent file. What's different: Interviews you until it understands the request before building anything Two testing stages: prompt validation via LLM invoke, then real subprocess execution of generated code. Not the same thing. Self-referential: injects its own source as a reference template for generation Structured rating schema drives iteration. Human approval gate before anything saves. Runs on Qwen3.6-35B A3B Q8_0 locally via llama.cpp. GITHUB PAGE Give it a shot and tell me what you think.

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/0c33/i-built-an-agent-that-builds-agents-runs-on-local-qwen3-pure-python-2hjp

## Related notes
- [[2026-04-06-i-built-an-open-source-benchmark-that-scores-ai-agents-not-models]]
- [[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]
- [[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]
- [[2026-04-02-im-an-ai-agent-that-built-its-own-training-data-pipeline]]
- [[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]
- [[2026-04-08-your-ai-agent-is-reading-poisoned-web-pages-heres-how-to-stop-it]]
