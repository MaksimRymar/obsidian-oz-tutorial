---
title: 'Null, Zero, Absent: A Three-State Gate for AI-Drafted API Docs'
date: '2026-09-23'
source: https://dev.to/datago_7777/null-zero-absent-a-three-state-gate-for-ai-drafted-api-docs-5859
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-08-15-build-a-token-ledger-before-you-burn-through-a-free-model-tier]]'
- '[[2026-09-08-your-agent-will-invent-timeouts-pin-them-in-a-contract-test-first]]'
- '[[2026-09-07-when-not-to-host-an-agent-on-free-inference]]'
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
status: unread
---

> **TL;DR:** The typical regen failure is quiet. A /list-invoices page comes back from the model with a parameter table. The table looks complete. Then a client sends limit=0 because the table said 0 means “no cap.” The OpenAPI file…

## What’s new and why it matters
The typical regen failure is quiet. A /list-invoices page comes back from the model with a parameter table. The table looks complete. Then a client sends limit=0 because the table said 0 means “no cap.” The OpenAPI file never said that. limit was optional. The server default was 20 . Sending 0 returned an empty page. Sending a JSON null in a query string was a 400 . Three states, one collapsed sentence. This is not a tone problem. It is a contract problem. Models are good at filling tables. They are bad at preserving the difference between a missing field, an explicit null, and a numeric zero.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datago_7777/null-zero-absent-a-three-state-gate-for-ai-drafted-api-docs-5859

## Related notes
- [[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-08-15-build-a-token-ledger-before-you-burn-through-a-free-model-tier]]
- [[2026-09-08-your-agent-will-invent-timeouts-pin-them-in-a-contract-test-first]]
- [[2026-09-07-when-not-to-host-an-agent-on-free-inference]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
