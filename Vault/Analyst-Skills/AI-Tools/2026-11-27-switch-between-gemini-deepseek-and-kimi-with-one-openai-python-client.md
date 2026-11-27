---
title: Switch between Gemini, DeepSeek and Kimi with one OpenAI Python client
date: '2026-11-27'
source: https://dev.to/_f467169b51ec73738019e6/switch-between-gemini-deepseek-and-kimi-with-one-openai-python-client-1c73
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-07-16-switch-ai-models-without-rewriting-your-openai-sdk-integration]]'
- '[[2026-10-23-calling-open-models-inside-a-tee-with-the-openai-python-sdk]]'
- '[[2026-06-19-use-gpt-claude-and-gemini-with-the-openai-sdk---one-baseurl-any-language]]'
- '[[2026-10-26-a-free-model-swap-is-not-a-config-change-a-contract-probe-you-can-run]]'
- '[[2026-11-27-how-to-check-every-page-on-your-site-for-duplicate-h1-tags-with-python]]'
- '[[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]'
status: unread
---

> **TL;DR:** Disclosure: I work on ModelFold. This is a configuration walkthrough based on our public docs, not a benchmark. I didn't send a paid request to prepare it. Suppose your Python script already sends a chat message. To try…

## What’s new and why it matters
Disclosure: I work on ModelFold. This is a configuration walkthrough based on our public docs, not a benchmark. I didn't send a paid request to prepare it. Suppose your Python script already sends a chat message. To try it with a different model, you shouldn't have to edit the prompt, swap SDKs or maintain another copy of the script. Make the model ID a command-line argument and keep the client configuration in one place. Install the SDK with python -m pip install openai . Set MODELFOLD_API_KEY in your environment using your own ModelFold key; don't paste it into the script. Save this as chat.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/_f467169b51ec73738019e6/switch-between-gemini-deepseek-and-kimi-with-one-openai-python-client-1c73

## Related notes
- [[2026-07-16-switch-ai-models-without-rewriting-your-openai-sdk-integration]]
- [[2026-10-23-calling-open-models-inside-a-tee-with-the-openai-python-sdk]]
- [[2026-06-19-use-gpt-claude-and-gemini-with-the-openai-sdk---one-baseurl-any-language]]
- [[2026-10-26-a-free-model-swap-is-not-a-config-change-a-contract-probe-you-can-run]]
- [[2026-11-27-how-to-check-every-page-on-your-site-for-duplicate-h1-tags-with-python]]
- [[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]
