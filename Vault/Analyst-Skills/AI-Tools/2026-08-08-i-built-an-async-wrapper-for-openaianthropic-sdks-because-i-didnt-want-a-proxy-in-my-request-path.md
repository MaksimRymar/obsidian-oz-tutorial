---
title: I built an async wrapper for OpenAI/Anthropic SDKs because I didn't want a
  proxy in my request path
date: '2026-08-08'
source: https://dev.to/mandarvshinde/i-built-an-async-wrapper-for-openaianthropic-sdks-because-i-didnt-want-a-proxy-in-my-request-path-1h1p
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-07-02-beyond-tryexcept-advanced-exception-handling-patterns-every-ai-engineer-should-know]]'
- '[[2026-04-02-how-i-stopped-paying-openai-to-run-my-test-suite]]'
- '[[2026-03-23-the-reason-your-live-ai-demo-spins-has-nothing-to-do-with-your-model]]'
- '[[2026-07-26-serverless-ml-deployment-from-jupyter-notebook-to-global-api-in-10-minutes-no-mlops-expert-needed]]'
- '[[2026-06-10-i-built-a-tool-that-generates-api-docs-from-your-source-code---no-annotations-no-server-running-no-swagger-config]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
status: unread
---

> **TL;DR:** I kept running into the same tradeoff building cost tooling for teams shipping LLM features. Every attribution tool in this space works the same way: you point base_url at a proxy, and it sees every call before it happen…

## What’s new and why it matters
I kept running into the same tradeoff building cost tooling for teams shipping LLM features. Every attribution tool in this space works the same way: you point base_url at a proxy, and it sees every call before it happens. That's genuinely useful if you want to block or downgrade a call before it fires. It also means the proxy's uptime is now your uptime, and you've added a network hop to every single request. I wanted the attribution without touching the request path at all. So I wrote a wrapper instead. Cognocient wraps the OpenAI and Anthropic Python clients directly. You still call client.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/mandarvshinde/i-built-an-async-wrapper-for-openaianthropic-sdks-because-i-didnt-want-a-proxy-in-my-request-path-1h1p

## Related notes
- [[2026-07-02-beyond-tryexcept-advanced-exception-handling-patterns-every-ai-engineer-should-know]]
- [[2026-04-02-how-i-stopped-paying-openai-to-run-my-test-suite]]
- [[2026-03-23-the-reason-your-live-ai-demo-spins-has-nothing-to-do-with-your-model]]
- [[2026-07-26-serverless-ml-deployment-from-jupyter-notebook-to-global-api-in-10-minutes-no-mlops-expert-needed]]
- [[2026-06-10-i-built-a-tool-that-generates-api-docs-from-your-source-code---no-annotations-no-server-running-no-swagger-config]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
