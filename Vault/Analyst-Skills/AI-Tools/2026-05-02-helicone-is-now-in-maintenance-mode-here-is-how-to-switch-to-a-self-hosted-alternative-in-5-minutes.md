---
title: Helicone is now in maintenance mode. Here is how to switch to a self-hosted
  alternative in 5 minutes.
date: '2026-05-02'
source: https://dev.to/torrixai/helicone-is-now-in-maintenance-mode-here-is-how-to-switch-to-a-self-hosted-alternative-in-5-4li0
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-03-28-i-built-a-cli-that-migrates-your-js-codebase-to-typescript-automatically-using-ai]]'
- '[[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]'
- '[[2026-02-25-i-built-a-free-alternative-to-langsmith-one-decorator-local-sqlite-zero-infrastructure]]'
- '[[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]'
- '[[2026-04-14-claude-api-prompt-caching-cut-costs-80-on-every-repeated-request]]'
status: unread
---

> **TL;DR:** If you have been using Helicone to track LLM costs and traces, you may have noticed it was acquired by Mintlify in March 2026. Development has stopped. The self-hosted version has open issues that are not being fixed. Th…

## What’s new and why it matters
If you have been using Helicone to track LLM costs and traces, you may have noticed it was acquired by Mintlify in March 2026. Development has stopped. The self-hosted version has open issues that are not being fixed. The team is focused on Mintlify now. If you need a replacement, this post covers how to migrate to Torrix, a self-hosted LLM observability proxy that uses the same proxy-header model as Helicone. What Torrix does Torrix is a single Docker container that sits between your app and any LLM provider. Every call is logged to a local SQLite database with full prompt, response, token co…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/torrixai/helicone-is-now-in-maintenance-mode-here-is-how-to-switch-to-a-self-hosted-alternative-in-5-4li0

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-03-28-i-built-a-cli-that-migrates-your-js-codebase-to-typescript-automatically-using-ai]]
- [[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]
- [[2026-02-25-i-built-a-free-alternative-to-langsmith-one-decorator-local-sqlite-zero-infrastructure]]
- [[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]
- [[2026-04-14-claude-api-prompt-caching-cut-costs-80-on-every-repeated-request]]
