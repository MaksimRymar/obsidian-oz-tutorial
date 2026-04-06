---
title: I built an open-source FinOps layer for GenAI APIs real-time USD cost per OTel
  span, multi-tenant isolation, zero prompt logging
date: '2026-04-06'
source: https://dev.to/skarl007/i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-26m5
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
- '[[2026-04-02-how-i-stopped-paying-openai-to-run-my-test-suite]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-03-23-how-http-402-is-turning-apis-into-vending-machines]]'
- '[[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]'
status: unread
---

> **TL;DR:** I opened my LLM invoice and had no idea where the money went. So I built LumenAI. Last month I opened my cloud bill and saw $4,847.23 in LLM API costs. For a single week. I had no idea which tenant caused the spike. No i…

## What’s new and why it matters
I opened my LLM invoice and had no idea where the money went. So I built LumenAI. Last month I opened my cloud bill and saw $4,847.23 in LLM API costs. For a single week. I had no idea which tenant caused the spike. No idea which agent ran 11,000 times. No idea whether claude-opus-4-6 at $15/M tokens was firing in places where claude-haiku-4-5 at $0.25/M would have worked just as well. My logs said "LLM call completed". That was all. Standard observability tools were not built for the economics of generative AI. OTel gives you traces but no USD cost. Logging gives you messages but no token acc…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/skarl007/i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-26m5

## Related notes
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
- [[2026-04-02-how-i-stopped-paying-openai-to-run-my-test-suite]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-03-23-how-http-402-is-turning-apis-into-vending-machines]]
- [[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]
