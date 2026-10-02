---
title: 'Sidekick part 2: grounding beats instructions'
date: '2026-10-02'
source: https://dev.to/irfan_wani/sidekick-part-2-grounding-beats-instructions-4607
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-09-18-rabbitmq-vs-kafka-for-data-engineering-queues-vs-logs-when-each-wins]]'
status: unread
---

> **TL;DR:** Sidekick Part 2: grounding beats instructions — facts injected before the model sees the prompt Small local models have a habit nobody warns you about: they ignore system-prompt rules. Tell a 3B model "always check the h…

## What’s new and why it matters
Sidekick Part 2: grounding beats instructions — facts injected before the model sees the prompt Small local models have a habit nobody warns you about: they ignore system-prompt rules. Tell a 3B model "always check the hardware before recommending," and it will confidently recommend anyway — from vibes. Our eval harness still carries the scar: an early version answered a hardware question with generic LLM advice, scoring 3/10 on our own quality check. Another told a user their ~/neural-hangar directory "does not exist." It existed. A third refused to fetch a URL at all: "I can't browse." Three…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/irfan_wani/sidekick-part-2-grounding-beats-instructions-4607

## Related notes
- [[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-09-18-rabbitmq-vs-kafka-for-data-engineering-queues-vs-logs-when-each-wins]]
