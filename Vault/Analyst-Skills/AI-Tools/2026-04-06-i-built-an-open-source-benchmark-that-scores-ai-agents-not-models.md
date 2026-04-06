---
title: I built an open-source benchmark that scores AI agents, not models
date: '2026-04-06'
source: https://dev.to/alethios000/i-built-an-open-source-benchmark-that-scores-ai-agents-not-models-36aa
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#tool'
related:
- '[[2026-04-02-im-an-ai-agent-that-built-its-own-training-data-pipeline]]'
- '[[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]'
- '[[2026-03-07-im-an-autonomous-ai-that-built-a-pay-per-use-api-heres-how-x402-works]]'
- '[[2026-04-06-ai-os-comparison-why-we-built-on-openclaw-gemma-4-instead-of-renting-perplexity]]'
- '[[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]'
- '[[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]'
status: unread
---

> **TL;DR:** Two agents built on the same GPT-4o can have wildly different reliability. But every benchmark only evaluates the model. So I built Legit — an open-source platform that scores the agent as a whole. How it works pip insta…

## What’s new and why it matters
Two agents built on the same GPT-4o can have wildly different reliability. But every benchmark only evaluates the model. So I built Legit — an open-source platform that scores the agent as a whole. How it works pip install getlegit legit init --agent "MyBot" --endpoint "http://localhost:8000/run" legit run v1 --local 36 tasks across 6 categories (Research, Extract, Analyze, Code, Write, Operate). Two scoring layers: Layer 1: deterministic checks, runs locally, free Layer 2: 3 AI judges (Claude, GPT-4o, Gemini), median score Agents get an Elo rating and tier (Platinum/Gold/Silver/Bronze). Free,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/alethios000/i-built-an-open-source-benchmark-that-scores-ai-agents-not-models-36aa

## Related notes
- [[2026-04-02-im-an-ai-agent-that-built-its-own-training-data-pipeline]]
- [[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]
- [[2026-03-07-im-an-autonomous-ai-that-built-a-pay-per-use-api-heres-how-x402-works]]
- [[2026-04-06-ai-os-comparison-why-we-built-on-openclaw-gemma-4-instead-of-renting-perplexity]]
- [[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]
- [[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]
