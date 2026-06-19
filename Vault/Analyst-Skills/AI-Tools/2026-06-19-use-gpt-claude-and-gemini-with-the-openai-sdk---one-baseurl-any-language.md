---
title: Use GPT, Claude, and Gemini with the OpenAI SDK - one base_url, any language
date: '2026-06-19'
source: https://dev.to/chenxiao5580cmd/use-gpt-claude-and-gemini-with-the-openai-sdk-one-baseurl-any-language-475n
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#tool'
related:
- '[[2026-05-03-how-i-added-llm-fallback-to-my-openai-app-in-10-minutes]]'
- '[[2026-05-10-i-built-a-10month-claude-api-heres-the-curl-command]]'
- '[[2026-05-24-how-i-unified-14-ai-models-behind-one-openai-compatible-api]]'
- '[[2026-04-29-how-to-use-claude-api-from-python-in-15-lines-and-why-it-costs-2month]]'
- '[[2026-02-25-i-built-a-free-alternative-to-langsmith-one-decorator-local-sqlite-zero-infrastructure]]'
- '[[2026-05-02-i-built-a-2month-claude-api-wrapper-heres-the-curl-command]]'
status: unread
---

> **TL;DR:** If you're juggling separate SDKs and API keys for OpenAI, Anthropic, and Google, here's a simpler setup: point the OpenAI SDK at an OpenAI-compatible gateway and call GPT, Claude, and Gemini through one base_url and one…

## What’s new and why it matters
If you're juggling separate SDKs and API keys for OpenAI, Anthropic, and Google, here's a simpler setup: point the OpenAI SDK at an OpenAI-compatible gateway and call GPT, Claude, and Gemini through one base_url and one key — at a flat, predictable per-call price instead of three separate per-token bills. Here's the exact change in five common stacks. Python (OpenAI SDK) from openai import OpenAI client = OpenAI ( base_url = " https://modelishub.com/v1 " , api_key = " YOUR_MODELIS_KEY " , ) resp = client . chat . completions . create ( model = " gpt-4o-mini " , messages = [{ " role " : " user…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/chenxiao5580cmd/use-gpt-claude-and-gemini-with-the-openai-sdk-one-baseurl-any-language-475n

## Related notes
- [[2026-05-03-how-i-added-llm-fallback-to-my-openai-app-in-10-minutes]]
- [[2026-05-10-i-built-a-10month-claude-api-heres-the-curl-command]]
- [[2026-05-24-how-i-unified-14-ai-models-behind-one-openai-compatible-api]]
- [[2026-04-29-how-to-use-claude-api-from-python-in-15-lines-and-why-it-costs-2month]]
- [[2026-02-25-i-built-a-free-alternative-to-langsmith-one-decorator-local-sqlite-zero-infrastructure]]
- [[2026-05-02-i-built-a-2month-claude-api-wrapper-heres-the-curl-command]]
