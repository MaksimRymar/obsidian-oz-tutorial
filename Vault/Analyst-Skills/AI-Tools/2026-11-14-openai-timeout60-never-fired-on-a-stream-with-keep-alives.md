---
title: OpenAI timeout=60 Never Fired on a Stream With Keep-Alives
date: '2026-11-14'
source: https://dev.to/acemeridian/openai-timeout60-never-fired-on-a-stream-with-keep-alives-10o7
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
- '[[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]'
- '[[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]'
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
status: unread
---

> **TL;DR:** The openai Python SDK's timeout=60 limits each socket read, not the request, so a streamed completion that receives an SSE keep-alive comment every 15 seconds never times out, even though your loop never sees an event. P…

## What’s new and why it matters
The openai Python SDK's timeout=60 limits each socket read, not the request, so a streamed completion that receives an SSE keep-alive comment every 15 seconds never times out, even though your loop never sees an event. Put a wall clock around the whole attempt instead: with AsyncOpenAI , asyncio.timeout(30) ended the same stalled stream at 30.0 to 30.1 seconds in every run. This story was written with the assistance of an AI writing program. The numbers come from openai 2.43.0 and httpx 0.28.1 on Python 3.14.4, run against a local fake OpenAI-compatible endpoint over plain HTTP and TLS. I did…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/acemeridian/openai-timeout60-never-fired-on-a-stream-with-keep-alives-10o7

## Related notes
- [[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
- [[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]
- [[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
