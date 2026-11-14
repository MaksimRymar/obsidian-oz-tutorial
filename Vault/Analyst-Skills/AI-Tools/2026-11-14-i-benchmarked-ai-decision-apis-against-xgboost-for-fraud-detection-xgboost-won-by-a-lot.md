---
title: I benchmarked AI decision APIs against XGBoost for fraud detection. XGBoost
  won, by a lot.
date: '2026-11-14'
source: https://dev.to/jpietrus/i-benchmarked-ai-decision-apis-against-xgboost-for-fraud-detection-xgboost-won-by-a-lot-3jdh
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]'
- '[[2026-11-13-i-built-a-crypto-research-agent-in-150-lines-of-python-heres-the-code-runs-free-no-signup]]'
- '[[2026-07-03-i-ranked-30-ai-apis-by-price-and-the-results-are-wild]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-12-a-30-line-wrapper-that-tells-you-what-every-llm-call-actually-costs]]'
status: unread
---

> **TL;DR:** Between September and October, TypeSafe, OpenAI and Cloudflare all shipped "decision model" APIs: you send a case, ask one fixed question, and get a score back. They're being pitched for fraud triage, so I wanted to know…

## What’s new and why it matters
Between September and October, TypeSafe, OpenAI and Cloudflare all shipped "decision model" APIs: you send a case, ask one fixed question, and get a score back. They're being pitched for fraud triage, so I wanted to know how they compare with the boring XGBoost model most fraud teams already run. I built a small open benchmark to find out. It's MIT-licensed and runs offline in about five seconds. What I compared Same transactions, same fields, ranked by each model's score: XGBoost , trained on labelled history A hand-written rules checklist TypeSafe Jev, OpenAI Decisions, Cloudflare Clef and C…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jpietrus/i-benchmarked-ai-decision-apis-against-xgboost-for-fraud-detection-xgboost-won-by-a-lot-3jdh

## Related notes
- [[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]
- [[2026-11-13-i-built-a-crypto-research-agent-in-150-lines-of-python-heres-the-code-runs-free-no-signup]]
- [[2026-07-03-i-ranked-30-ai-apis-by-price-and-the-results-are-wild]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-12-a-30-line-wrapper-that-tells-you-what-every-llm-call-actually-costs]]
