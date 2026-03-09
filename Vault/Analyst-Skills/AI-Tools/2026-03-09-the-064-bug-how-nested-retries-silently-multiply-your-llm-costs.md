---
title: 'The $0.64 bug: how nested retries silently multiply your LLM costs'
date: '2026-03-09'
source: https://dev.to/amabito/the-064-bug-how-nested-retries-silently-multiply-your-llm-costs-3g0p
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-03-02-i-built-a-trade-pricing-api-that-covers-5-countries-so-ai-agents-stop-hallucinating-contractor-costs]]'
- '[[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]'
- '[[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]'
status: unread
---

> **TL;DR:** One user click. One document. My LangChain agent made 64 API calls to GPT-4o before it finally returned a result. At typical GPT-4o pricing, that turns a one-cent task into a sixty-cent task. With longer prompts, worse.…

## What’s new and why it matters
One user click. One document. My LangChain agent made 64 API calls to GPT-4o before it finally returned a result. At typical GPT-4o pricing, that turns a one-cent task into a sixty-cent task. With longer prompts, worse. The agent wasn't broken. The bug was in how the retries multiply . The problem: retries stack, and nobody tracks the total This pattern shows up in most LLM agent stacks I've looked at: Your application code retries 3 times on failure calls a LangChain chain retries 3 times on failure which calls a tool retries 3 times on failure which calls the LLM API Each layer is reasonable…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/amabito/the-064-bug-how-nested-retries-silently-multiply-your-llm-costs-3g0p

## Related notes
- [[2026-03-02-i-built-a-trade-pricing-api-that-covers-5-countries-so-ai-agents-stop-hallucinating-contractor-costs]]
- [[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]
- [[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]
