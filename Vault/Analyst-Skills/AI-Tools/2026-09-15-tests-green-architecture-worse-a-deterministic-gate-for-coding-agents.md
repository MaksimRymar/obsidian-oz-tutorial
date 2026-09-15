---
title: 'Tests green, architecture worse: a deterministic gate for coding agents'
date: '2026-09-15'
source: https://dev.to/ake2l/tests-green-architecture-worse-a-deterministic-gate-for-coding-agents-4jhi
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]'
- '[[2026-08-10-my-ai-agent-found-a-5-sigma-result-on-day-one-i-deleted-it]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
status: unread
---

> **TL;DR:** My coding agents kept the tests green. The architecture still got worse. In the DATAMIMIC EE core the agents didn't break the build. They broke the structure. Utilities landed in whatever module was closest, not where th…

## What’s new and why it matters
My coding agents kept the tests green. The architecture still got worse. In the DATAMIMIC EE core the agents didn't break the build. They broke the structure. Utilities landed in whatever module was closest, not where they belonged. Code imported past the public interface of another component. And the one that hurt most: clients got imported in places that had no business touching them, above all in the communication between data sources and tasks. In a small task a reviewer catches that. In a large, nested task it hides in a diff that looks reasonable, with every test green. The problem has t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ake2l/tests-green-architecture-worse-a-deterministic-gate-for-coding-agents-4jhi

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]
- [[2026-08-10-my-ai-agent-found-a-5-sigma-result-on-day-one-i-deleted-it]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
