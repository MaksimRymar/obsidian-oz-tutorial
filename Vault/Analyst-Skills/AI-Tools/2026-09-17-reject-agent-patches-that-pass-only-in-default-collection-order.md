---
title: Reject Agent Patches That Pass Only in Default Collection Order
date: '2026-09-17'
source: https://dev.to/datacpp_8185/reject-agent-patches-that-pass-only-in-default-collection-order-2m2h
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]'
- '[[2026-08-30-give-your-agent-patch-a-determinism-budget-seed-locked-properties-pinned-fixtures-a-freeze-registry]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
status: unread
---

> **TL;DR:** An agent patch that is green under default pytest collection order has not been tested for isolation. Reject the merge if a shuffle seed fails while the default order passes. That failure is deterministic order coupling,…

## What’s new and why it matters
An agent patch that is green under default pytest collection order has not been tested for isolation. Reject the merge if a shuffle seed fails while the default order passes. That failure is deterministic order coupling, not a flake, and it does not belong on a freeze list. Default order measures one path: the discovery sequence the agent happened to write. It does not measure whether production code still holds after a cold import, a reversed file order, or a parallel worker. Treat collection order as a runner detail. Do not treat it as an oracle. What default-order green actually encodes Pyt…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datacpp_8185/reject-agent-patches-that-pass-only-in-default-collection-order-2m2h

## Related notes
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]
- [[2026-08-30-give-your-agent-patch-a-determinism-budget-seed-locked-properties-pinned-fixtures-a-freeze-registry]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
