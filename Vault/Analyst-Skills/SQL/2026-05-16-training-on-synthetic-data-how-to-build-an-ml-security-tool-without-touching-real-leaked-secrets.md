---
title: 'Training on Synthetic Data: How to Build an ML Security Tool Without Touching
  Real Leaked Secrets'
date: '2026-05-16'
source: https://dev.to/pgmpofu/training-on-synthetic-data-how-to-build-an-ml-security-tool-without-touching-real-leaked-secrets-33o5
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
- '[[2026-05-16-blocking-secrets-before-they-hit-the-repository-building-a-pre-commit-hook-with-ml]]'
- '[[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]'
- '[[2026-04-08-building-a-codebase-qa-bot-a-practical-guide-with-openai-and-langchain]]'
- '[[2026-04-11-7-free-defi-apis-every-developer-should-know-in-2026-with-code-examples]]'
- '[[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]'
status: unread
---

> **TL;DR:** Before I wrote a single line of model training code, I made a decision that constrained everything that followed. I would not train on real leaked credentials. The alternative was straightforward. GitHub's public commit…

## What’s new and why it matters
Before I wrote a single line of model training code, I made a decision that constrained everything that followed. I would not train on real leaked credentials. The alternative was straightforward. GitHub's public commit history contains millions of accidentally committed secrets — API keys, passwords, connection strings, private keys — that have been scraped, indexed, and catalogued by security researchers. Datasets of this material exist. Using them as positive training examples would produce a model trained on exactly the kind of data it needs to recognise. I chose not to do that. And the re…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/pgmpofu/training-on-synthetic-data-how-to-build-an-ml-security-tool-without-touching-real-leaked-secrets-33o5

## Related notes
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
- [[2026-05-16-blocking-secrets-before-they-hit-the-repository-building-a-pre-commit-hook-with-ml]]
- [[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]
- [[2026-04-08-building-a-codebase-qa-bot-a-practical-guide-with-openai-and-langchain]]
- [[2026-04-11-7-free-defi-apis-every-developer-should-know-in-2026-with-code-examples]]
- [[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]
