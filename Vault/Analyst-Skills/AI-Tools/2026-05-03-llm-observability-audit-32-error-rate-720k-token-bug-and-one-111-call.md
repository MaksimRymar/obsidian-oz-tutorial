---
title: 'LLM Observability Audit: 32% Error Rate, 720K-Token Bug, and One $1.11 Call'
date: '2026-05-03'
source: https://dev.to/jmolinasoler/llm-observability-audit-32-error-rate-720k-token-bug-and-one-111-call-53k8
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]'
- '[[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]'
- '[[2026-03-09-5-prompt-engineering-patterns-that-actually-work-in-production]]'
- '[[2026-04-18-your-rag-system-retrieves-the-right-data-but-still-produces-wrong-answers-heres-why-and-how-to-fix-it]]'
- '[[2026-03-27-the-real-cost-of-your-ai-agent-its-not-what-you-think]]'
status: unread
---

> **TL;DR:** A self-hosted Langfuse instance, 21 hours of production traffic, 516 traces, $2.86 in spend , and an OpenRouter-fronted LLM router shuffling 24 different models. I pulled the entire dataset through Langfuse's REST API an…

## What’s new and why it matters
A self-hosted Langfuse instance, 21 hours of production traffic, 516 traces, $2.86 in spend , and an OpenRouter-fronted LLM router shuffling 24 different models. I pulled the entire dataset through Langfuse's REST API and ran a flat audit. Below is what surfaced — the kind of findings that don't show up on a dashboard until you actually grep the data. This is a walkthrough of (1) how to extract every observable from Langfuse via the public API, and (2) the five concrete bugs the data exposed. 1. Pulling the data Langfuse's public API at /api/public/* uses HTTP Basic Auth with a project-scoped…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jmolinasoler/llm-observability-audit-32-error-rate-720k-token-bug-and-one-111-call-53k8

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]
- [[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]
- [[2026-03-09-5-prompt-engineering-patterns-that-actually-work-in-production]]
- [[2026-04-18-your-rag-system-retrieves-the-right-data-but-still-produces-wrong-answers-heres-why-and-how-to-fix-it]]
- [[2026-03-27-the-real-cost-of-your-ai-agent-its-not-what-you-think]]
