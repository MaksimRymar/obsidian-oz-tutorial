---
title: Running LLMs on Apple Silicon Is Getting Serious — Hypura Scheduler (194pts
  on HN)
date: '2026-03-25'
source: https://dev.to/0012303/running-llms-on-apple-silicon-is-getting-serious-hypura-scheduler-194pts-on-hn-14od
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]'
- '[[2026-03-09-building-a-resilient-multi-model-ai-router-in-python]]'
- '[[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]'
- '[[2026-03-22-getting-started-with-tinygrad-the-lean-neural-network-framework-powering-ai-on-consumer-hardware]]'
- '[[2026-02-23-your-mac-is-now-a-personal-doctor-analyzing-5-years-of-healthkit-data-locally-with-llama-3-mlx]]'
status: unread
---

> **TL;DR:** A new project just hit Hacker News at 194+ points: Hypura — a storage-tier-aware LLM inference scheduler specifically for Apple Silicon. This is significant because it addresses the biggest limitation of running LLMs loc…

## What’s new and why it matters
A new project just hit Hacker News at 194+ points: Hypura — a storage-tier-aware LLM inference scheduler specifically for Apple Silicon. This is significant because it addresses the biggest limitation of running LLMs locally on Mac: memory management. The Problem Running a 70B parameter model on a MacBook Pro: Model RAM Needed M3 Max (96GB) M4 Ultra (192GB) Llama 3 8B 8GB ✅ Fast ✅ Fast Llama 3 70B 40GB ⚠️ Slow (swap) ✅ Fast Mixtral 8x22B 88GB ❌ Won't fit ⚠️ Tight Llama 3 405B 200GB+ ❌ ❌ Apple's unified memory is great, but when models exceed available RAM, inference falls off a cliff. What Hyp…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/0012303/running-llms-on-apple-silicon-is-getting-serious-hypura-scheduler-194pts-on-hn-14od

## Related notes
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]
- [[2026-03-09-building-a-resilient-multi-model-ai-router-in-python]]
- [[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]
- [[2026-03-22-getting-started-with-tinygrad-the-lean-neural-network-framework-powering-ai-on-consumer-hardware]]
- [[2026-02-23-your-mac-is-now-a-personal-doctor-analyzing-5-years-of-healthkit-data-locally-with-llama-3-mlx]]
