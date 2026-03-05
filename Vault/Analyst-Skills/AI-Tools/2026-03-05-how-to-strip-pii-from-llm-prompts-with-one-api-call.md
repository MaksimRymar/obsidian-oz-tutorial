---
title: How to Strip PII from LLM Prompts with One API Call
date: '2026-03-05'
source: https://dev.to/tiamat/how-to-strip-pii-from-llm-prompts-with-one-api-call-5f1
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-02-22-build-a-rag-system-with-python-and-a-local-llm-no-api-costs]]'
- '[[2026-02-24-stop-writing-css-selectors-that-break---extract-web-data-with-plain-english-using-ai]]'
- '[[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]'
- '[[2026-02-25-i-built-a-free-alternative-to-langsmith-one-decorator-local-sqlite-zero-infrastructure]]'
- '[[2026-02-27-x402-payment-harness-making-x402-payments-without-a-coinbase-cdp-wallet]]'
- '[[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]'
status: unread
---

> **TL;DR:** The Problem You want to use Claude or GPT-4 to analyze customer data, but you can't send their real names, emails, or SSNs directly to OpenAI or Anthropic. Enterprise policies won't allow it. HIPAA/SOC2 compliance forbid…

## What’s new and why it matters
The Problem You want to use Claude or GPT-4 to analyze customer data, but you can't send their real names, emails, or SSNs directly to OpenAI or Anthropic. Enterprise policies won't allow it. HIPAA/SOC2 compliance forbids it. Solution? Strip the PII before it leaves your server. The API TIAMAT built a free PII scrubber that runs one curl command: curl -X POST https://tiamat.live/api/scrub \ -H "Content-Type: application/json" \ -d '{ "text": "Customer John Smith (john@acme.com, SSN 123-45-6789) bought our premium plan." }' Response: { "scrubbed" : "Customer [NAME_1] ([EMAIL_1], SSN [SSN_1]) bo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tiamat/how-to-strip-pii-from-llm-prompts-with-one-api-call-5f1

## Related notes
- [[2026-02-22-build-a-rag-system-with-python-and-a-local-llm-no-api-costs]]
- [[2026-02-24-stop-writing-css-selectors-that-break---extract-web-data-with-plain-english-using-ai]]
- [[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]
- [[2026-02-25-i-built-a-free-alternative-to-langsmith-one-decorator-local-sqlite-zero-infrastructure]]
- [[2026-02-27-x402-payment-harness-making-x402-payments-without-a-coinbase-cdp-wallet]]
- [[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]
