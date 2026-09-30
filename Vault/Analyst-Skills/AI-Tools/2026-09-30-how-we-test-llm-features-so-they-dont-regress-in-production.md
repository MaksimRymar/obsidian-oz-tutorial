---
title: How We Test LLM Features So They Don't Regress in Production
date: '2026-09-30'
source: https://dev.to/lycore/how-we-test-llm-features-so-they-dont-regress-in-production-56io
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-14-a-free-server-regression-job-for-llm-generated-sql]]'
- '[[2026-05-10-bulletproofing-llm-structured-output-in-python-healing-retries-cost-caps-and-drift-detection-runnable-code]]'
- '[[2026-06-20-i-built-a-machine-verifiable-contract-system-for-python-code-heres-how-it-works]]'
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
status: unread
---

> **TL;DR:** We shipped an LLM-powered classification feature for a client last year. It worked well. Three weeks later, after a routine prompt tweak, it started miscategorising a specific edge case — one that the team had explicitly…

## What’s new and why it matters
We shipped an LLM-powered classification feature for a client last year. It worked well. Three weeks later, after a routine prompt tweak, it started miscategorising a specific edge case — one that the team had explicitly tested for during development. Nobody noticed for four days. The problem was not the prompt change. The problem was that we had no automated check that would have caught it. Our test suite confirmed that the endpoint returned a 200 and that the response was valid JSON. It said nothing about whether the classification was actually correct. This post is about how we fixed that,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/lycore/how-we-test-llm-features-so-they-dont-regress-in-production-56io

## Related notes
- [[2026-08-14-a-free-server-regression-job-for-llm-generated-sql]]
- [[2026-05-10-bulletproofing-llm-structured-output-in-python-healing-retries-cost-caps-and-drift-detection-runnable-code]]
- [[2026-06-20-i-built-a-machine-verifiable-contract-system-for-python-code-heres-how-it-works]]
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
