---
title: Calling open models inside a TEE with the OpenAI Python SDK
date: '2026-10-23'
source: https://dev.to/voltagegpu/calling-open-models-inside-a-tee-with-the-openai-python-sdk-18k5
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
related:
- '[[2026-06-19-use-gpt-claude-and-gemini-with-the-openai-sdk---one-baseurl-any-language]]'
- '[[2026-09-21-i-ran-a-contract-check-against-the-swagger-petstore-here-is-what-came-back]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-10-12-one-api-key-for-claude-gpt-gemini-grok-deepseek-flux-and-veo]]'
- '[[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
status: unread
---

> **TL;DR:** If you already call OpenAI from Python, switching to an open model that runs in a trusted execution environment (TEE) is two lines: the base URL and the key. Here is what that looks like, with real output captured on 23…

## What’s new and why it matters
If you already call OpenAI from Python, switching to an open model that runs in a trusted execution environment (TEE) is two lines: the base URL and the key. Here is what that looks like, with real output captured on 23 October 2026. The two lines that change from openai import OpenAI import os client = OpenAI ( base_url = " https://api.voltagegpu.com/v1 " , api_key = os . environ [ " VOLTAGEGPU_API_KEY " ], # a vgpu_... key, never commit it ) resp = client . chat . completions . create ( model = " google/gemma-4-31B-turbo-TEE " , messages = [{ " role " : " user " , " content " : " In one sent…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/voltagegpu/calling-open-models-inside-a-tee-with-the-openai-python-sdk-18k5

## Related notes
- [[2026-06-19-use-gpt-claude-and-gemini-with-the-openai-sdk---one-baseurl-any-language]]
- [[2026-09-21-i-ran-a-contract-check-against-the-swagger-petstore-here-is-what-came-back]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-10-12-one-api-key-for-claude-gpt-gemini-grok-deepseek-flux-and-veo]]
- [[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
