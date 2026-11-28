---
title: Add long-term memory to a LangChain chatbot in Python (15 lines, no vector
  DB)
date: '2026-11-28'
source: https://dev.to/belcore/add-long-term-memory-to-a-langchain-chatbot-in-python-15-lines-no-vector-db-i3i
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]'
- '[[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]'
- '[[2026-11-01-getting-only-the-new-dois-from-the-crossref-api-every-day-dates-cursors-and-rate-limits]]'
- '[[2026-03-15-why-ai-agents-forget-everything-and-how-we-fixed-it]]'
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
status: unread
---

> **TL;DR:** Most chat apps already store the conversation in their own database. The hard part is deciding which old messages to send to the model when the history gets long. Here is a small Python setup that keeps your history wher…

## What’s new and why it matters
Most chat apps already store the conversation in their own database. The hard part is deciding which old messages to send to the model when the history gets long. Here is a small Python setup that keeps your history where it is and lets Belcore pick the turns that matter. What you need Python 3.10+ A free Belcore API key (5,000 calls, no card): https://belcore.xyz/developers/signup pip install langchain-belcore export BELCORE_API_KEY = sk_... The code ChatBelcore is a normal LangChain chat model. You send the full history you keep; it returns the reply plus a small emotion state you save and s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/belcore/add-long-term-memory-to-a-langchain-chatbot-in-python-15-lines-no-vector-db-i3i

## Related notes
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]
- [[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]
- [[2026-11-01-getting-only-the-new-dois-from-the-crossref-api-every-day-dates-cursors-and-rate-limits]]
- [[2026-03-15-why-ai-agents-forget-everything-and-how-we-fixed-it]]
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
