---
title: How I stopped paying OpenAI to run my test suite
date: '2026-04-02'
source: https://dev.to/airupt/how-i-stopped-paying-openai-to-run-my-test-suite-1i7e
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#tool'
related:
- '[[2026-03-26-how-i-gave-an-llm-persistent-emotions-dreams-and-theory-of-mind-with-11k-lines-of-python]]'
- '[[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]'
- '[[2026-03-28-soul-engine]]'
- '[[2026-04-02-i-built-pytest-for-ai-agents-heres-what-i-learned]]'
- '[[2026-02-25-i-built-a-free-alternative-to-langsmith-one-decorator-local-sqlite-zero-infrastructure]]'
- '[[2026-03-09-building-a-resilient-multi-model-ai-router-in-python]]'
status: unread
---

> **TL;DR:** I was building an AI project and ran into something that kept bothering me. Every test that touched my LLM code was making a real API call. To OpenAI. Every single time. Tests were slow — 3 to 5 seconds each just waiting…

## What’s new and why it matters
I was building an AI project and ran into something that kept bothering me. Every test that touched my LLM code was making a real API call. To OpenAI. Every single time. Tests were slow — 3 to 5 seconds each just waiting for a response. Every CI run cost real money in tokens, for code that hadn't even shipped yet. And the tests were flaky : same code, same input, different output. Language models are non-deterministic, so I'd get a passing run, then a failing run, with no way to tell if my code was broken or if the model just felt like responding differently. The existing options aren't great…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/airupt/how-i-stopped-paying-openai-to-run-my-test-suite-1i7e

## Related notes
- [[2026-03-26-how-i-gave-an-llm-persistent-emotions-dreams-and-theory-of-mind-with-11k-lines-of-python]]
- [[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]
- [[2026-03-28-soul-engine]]
- [[2026-04-02-i-built-pytest-for-ai-agents-heres-what-i-learned]]
- [[2026-02-25-i-built-a-free-alternative-to-langsmith-one-decorator-local-sqlite-zero-infrastructure]]
- [[2026-03-09-building-a-resilient-multi-model-ai-router-in-python]]
