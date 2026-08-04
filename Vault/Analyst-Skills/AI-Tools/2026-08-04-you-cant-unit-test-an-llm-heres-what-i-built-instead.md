---
title: You Can't Unit-Test an LLM. Here's What I Built Instead.
date: '2026-08-04'
source: https://dev.to/amirmarcel/you-cant-unit-test-an-llm-heres-what-i-built-instead-m6g
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]'
- '[[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]'
- '[[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]'
- '[[2026-06-25-openai-compatible-apis-are-great-until-streaming-breaks-what-i-check-before-switching-providers]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]'
status: unread
---

> **TL;DR:** Every team shipping an LLM feature eventually hits the same wall: the thing you built is non-deterministic, and your whole testing culture assumes it isn't. assertEqual(output, expected) is meaningless when the output is…

## What’s new and why it matters
Every team shipping an LLM feature eventually hits the same wall: the thing you built is non-deterministic, and your whole testing culture assumes it isn't. assertEqual(output, expected) is meaningless when the output is a paragraph of generated prose that will be slightly different next time. The usual responses are both bad. One is to shrug and ship it with no verification at all: "it looked good when I tried it." The other is to test the model itself, chasing a moving target that changes every time the prompt or the weights do. I built an internal tool recently that leans on an LLM for exac…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/amirmarcel/you-cant-unit-test-an-llm-heres-what-i-built-instead-m6g

## Related notes
- [[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]
- [[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]
- [[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]
- [[2026-06-25-openai-compatible-apis-are-great-until-streaming-breaks-what-i-check-before-switching-providers]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]
