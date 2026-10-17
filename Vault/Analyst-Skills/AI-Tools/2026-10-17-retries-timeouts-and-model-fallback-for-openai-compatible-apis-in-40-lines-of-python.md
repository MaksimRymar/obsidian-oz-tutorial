---
title: Retries, timeouts and model fallback for OpenAI-compatible APIs in ~40 lines
  of Python
date: '2026-10-17'
source: https://dev.to/lucky_wang_52b64623a6001a/retries-timeouts-and-model-fallback-for-openai-compatible-apis-in-40-lines-of-python-3d9j
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#tool'
related:
- '[[2026-06-19-use-gpt-claude-and-gemini-with-the-openai-sdk---one-baseurl-any-language]]'
- '[[2026-05-03-how-i-added-llm-fallback-to-my-openai-app-in-10-minutes]]'
- '[[2026-08-17-retry-the-request-not-the-prompt-an-error-taxonomy-for-free-coding-models]]'
- '[[2026-10-17-your-retry-logic-has-never-seen-a-real-429-here-is-how-to-test-it-with-a-local-fault-injecting-mock]]'
- '[[2026-08-19-a-practical-guide-to-the-ace-data-cloud-python-sdk]]'
- '[[2026-08-03-your-ai-fallback-strategy-may-be-making-things-worse]]'
status: unread
---

> **TL;DR:** Disclosure: I work on the APIGOTO team. APIGOTO is an independent OpenAI-compatible API gateway and is not affiliated with OpenAI, Anthropic or Google. The pattern below works with any OpenAI-compatible endpoint, ours or…

## What’s new and why it matters
Disclosure: I work on the APIGOTO team. APIGOTO is an independent OpenAI-compatible API gateway and is not affiliated with OpenAI, Anthropic or Google. The pattern below works with any OpenAI-compatible endpoint, ours or not. When a prototype calls an LLM API, the first production problem is rarely the prompt. It's a 429, a slow response that hangs your worker, or one model being temporarily unavailable. Here is the small wrapper I use to handle all three. The idea Set a hard timeout on every request. Retry rate-limit and server errors with exponential backoff. If a model keeps failing, move o…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/lucky_wang_52b64623a6001a/retries-timeouts-and-model-fallback-for-openai-compatible-apis-in-40-lines-of-python-3d9j

## Related notes
- [[2026-06-19-use-gpt-claude-and-gemini-with-the-openai-sdk---one-baseurl-any-language]]
- [[2026-05-03-how-i-added-llm-fallback-to-my-openai-app-in-10-minutes]]
- [[2026-08-17-retry-the-request-not-the-prompt-an-error-taxonomy-for-free-coding-models]]
- [[2026-10-17-your-retry-logic-has-never-seen-a-real-429-here-is-how-to-test-it-with-a-local-fault-injecting-mock]]
- [[2026-08-19-a-practical-guide-to-the-ace-data-cloud-python-sdk]]
- [[2026-08-03-your-ai-fallback-strategy-may-be-making-things-worse]]
