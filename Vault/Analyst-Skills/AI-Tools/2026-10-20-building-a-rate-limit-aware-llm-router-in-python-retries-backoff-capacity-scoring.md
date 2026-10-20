---
title: 'Building a Rate-Limit-Aware LLM Router in Python: Retries, Backoff & Capacity
  Scoring'
date: '2026-10-20'
source: https://dev.to/sentiogate-org/building-a-rate-limit-aware-llm-router-in-python-retries-backoff-capacity-scoring-4f9p
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-10-openai-compatible-is-a-spectrum-not-a-boolean-heres-an-11-check-conformance-suite]]'
- '[[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]'
- '[[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]'
- '[[2026-10-17-retries-timeouts-and-model-fallback-for-openai-compatible-apis-in-40-lines-of-python]]'
- '[[2026-07-30-how-to-detect-and-handle-api-outages-gracefully-in-ai-powered-apps]]'
status: unread
---

> **TL;DR:** If your app has ever fallen over because a provider returned 429 Too Many Requests , and your fallback was "sleep a second and try again", you know the pain. That pattern hurts twice: you hit the provider again while it'…

## What’s new and why it matters
If your app has ever fallen over because a provider returned 429 Too Many Requests , and your fallback was "sleep a second and try again", you know the pain. That pattern hurts twice: you hit the provider again while it's already telling you to slow down, and you still don't know how long to wait. I built SentioGate partly because I kept writing that loop. Here's how it handles rate limits, and how to use it from Python or JavaScript. The problem: a 429 is information A 429 isn't a random failure. It's the provider telling you something specific: this model, on this key, is unavailable for a w…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sentiogate-org/building-a-rate-limit-aware-llm-router-in-python-retries-backoff-capacity-scoring-4f9p

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-10-openai-compatible-is-a-spectrum-not-a-boolean-heres-an-11-check-conformance-suite]]
- [[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]
- [[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]
- [[2026-10-17-retries-timeouts-and-model-fallback-for-openai-compatible-apis-in-40-lines-of-python]]
- [[2026-07-30-how-to-detect-and-handle-api-outages-gracefully-in-ai-powered-apps]]
