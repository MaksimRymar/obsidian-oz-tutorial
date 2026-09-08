---
title: Your Agent Will Invent Timeouts. Pin Them in a Contract Test First
date: '2026-09-08'
source: https://dev.to/devrs_9381/your-agent-will-invent-timeouts-pin-them-in-a-contract-test-first-2ni4
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]'
- '[[2026-08-15-learn-to-budget-a-free-model-tier-by-building-a-tiny-token-ledger]]'
- '[[2026-09-08-charge-wait-time-to-the-same-job]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-07-score-the-trace-not-the-final-payload]]'
status: unread
---

> **TL;DR:** When an agent writes an HTTP client, the silent bugs live in timeouts, retries, and idempotency headers you never approved. You should freeze those numbers in a checked-in policy file, then fail CI if generated code drif…

## What’s new and why it matters
When an agent writes an HTTP client, the silent bugs live in timeouts, retries, and idempotency headers you never approved. You should freeze those numbers in a checked-in policy file, then fail CI if generated code drifts. This case study walks a small billing adapter from an empty repo to a gate that rejects invented defaults. The rest of the article stays useful even if you never touch a hosted coding environment. Background: a tiny billing adapter, not a platform rewrite You are adding a payments adapter that charges a saved method through one upstream HTTP API. The public surface stays sm…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/devrs_9381/your-agent-will-invent-timeouts-pin-them-in-a-contract-test-first-2ni4

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]
- [[2026-08-15-learn-to-budget-a-free-model-tier-by-building-a-tiny-token-ledger]]
- [[2026-09-08-charge-wait-time-to-the-same-job]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-07-score-the-trace-not-the-final-payload]]
