---
title: 'Python json.dumps ensure_ascii: 24% More Claude Tokens, Wrong Kanji'
date: '2026-10-12'
source: https://dev.to/ji_ai/python-jsondumps-ensureascii-24-more-claude-tokens-wrong-kanji-4inm
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]'
- '[[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]'
- '[[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]'
- '[[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
status: unread
---

> **TL;DR:** The Python port of my support-ticket classifier used 24% more input tokens than the TypeScript version it replaced. Same model. Same system prompt. Same 2,000 tickets in the replay set. I spent an afternoon diffing promp…

## What’s new and why it matters
The Python port of my support-ticket classifier used 24% more input tokens than the TypeScript version it replaced. Same model. Same system prompt. Same 2,000 tickets in the replay set. I spent an afternoon diffing prompts before I saw it. The TypeScript prompt said 東京 . The Python prompt said 東京 . One default argument in json.dumps , ensure_ascii=True , was quietly rewriting every non-ASCII character in my prompts into hex escapes. It cost tokens, and worse, it made Claude misread Japanese customer names. TL;DR Python's json.dumps defaults to ensure_ascii=True , which turns é into é and 東 int…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ji_ai/python-jsondumps-ensureascii-24-more-claude-tokens-wrong-kanji-4inm

## Related notes
- [[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]
- [[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]
- [[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]
- [[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
