---
title: 'Constrained Decoding: Your JSON Schema Key Order Is a Prompt'
date: '2026-09-21'
source: https://dev.to/ji_ai/constrained-decoding-your-json-schema-key-order-is-a-prompt-34c0
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-08-19-final-weeks-of-gsoc]]'
status: unread
---

> **TL;DR:** I flipped one support-ticket classifier from free text to a strict JSON Schema and accuracy fell off a cliff. Same model. Same temperature. Same prompt. Same 300 tickets in my eval set. The only thing that changed was th…

## What’s new and why it matters
I flipped one support-ticket classifier from free text to a strict JSON Schema and accuracy fell off a cliff. Same model. Same temperature. Same prompt. Same 300 tickets in my eval set. The only thing that changed was that the output now parsed 100% of the time. That guarantee comes from constrained decoding, and constrained decoding is not a formatter that runs after the model. It runs inside the sampling loop, one token at a time, and it can quietly rewrite what the model is allowed to think. TL;DR Constrained decoding masks logits at every decode step. A grammar compiled from your JSON Sche…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ji_ai/constrained-decoding-your-json-schema-key-order-is-a-prompt-34c0

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-08-19-final-weeks-of-gsoc]]
