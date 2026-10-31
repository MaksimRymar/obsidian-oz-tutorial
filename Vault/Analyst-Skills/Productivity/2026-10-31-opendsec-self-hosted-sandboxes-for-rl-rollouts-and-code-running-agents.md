---
title: 'OpenDsec: self-hosted sandboxes for RL rollouts and code-running agents'
date: '2026-10-31'
source: https://dev.to/kernflux/opendsec-self-hosted-sandboxes-for-rl-rollouts-and-code-running-agents-g
domain: Productivity
relevance: 🟡
tags:
- '#career'
- '#library'
- '#productivity'
- '#python'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-22-ollama-run-llms-locally-and-swap-them-into-your-app-with-one-baseurl-change]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-02-23-getting-started-with-trinity-pattern-in-10-minutes]]'
- '[[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-07-15-give-your-chatbot-a-memory-in-google-colab-before-your-next-ai-interview]]'
status: unread
---

> **TL;DR:** If you train a model with agentic reinforcement learning, every rollout needs somewhere to run code: install a package, run the tests, hit the network, write files. Thousands of those run at once. When the training job i…

## What’s new and why it matters
If you train a model with agentic reinforcement learning, every rollout needs somewhere to run code: install a package, run the tests, hit the network, write files. Thousands of those run at once. When the training job is preempted they all have to stop together and come back later. And when you want to explore one state several ways, you want copies of the environment as it is right now, memory included, not fresh ones from the image. Hosted sandbox services cover part of this. We wanted all of it on our own machines, so we built OpenDsec and published it under the AGPL. This is the first pos…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kernflux/opendsec-self-hosted-sandboxes-for-rl-rollouts-and-code-running-agents-g

## Related notes
- [[2026-10-22-ollama-run-llms-locally-and-swap-them-into-your-app-with-one-baseurl-change]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-02-23-getting-started-with-trinity-pattern-in-10-minutes]]
- [[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-07-15-give-your-chatbot-a-memory-in-google-colab-before-your-next-ai-interview]]
