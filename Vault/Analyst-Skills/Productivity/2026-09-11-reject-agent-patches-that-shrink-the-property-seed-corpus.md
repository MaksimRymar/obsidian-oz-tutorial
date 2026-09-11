---
title: Reject Agent Patches That Shrink the Property Seed Corpus
date: '2026-09-11'
source: https://dev.to/datacpp_8185/reject-agent-patches-that-shrink-the-property-seed-corpus-1fl9
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-03-test-the-behavior-delta-after-an-agent-patch-not-the-whole-suite]]'
- '[[2026-09-10-merge-agent-patches-only-when-two-test-world-receipts-match]]'
- '[[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]'
- '[[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]'
- '[[2026-08-30-give-your-agent-patch-a-determinism-budget-seed-locked-properties-pinned-fixtures-a-freeze-registry]]'
status: unread
---

> **TL;DR:** A green CI job after an agent patch is not evidence that behavior held. The useful signal is whether the same seed corpus still executed, whether fixture hashes stayed put, and whether the flake freeze budget did not gro…

## What’s new and why it matters
A green CI job after an agent patch is not evidence that behavior held. The useful signal is whether the same seed corpus still executed, whether fixture hashes stayed put, and whether the flake freeze budget did not grow. If any of those three ledgers moved the wrong way, the patch is not a fix. It is a quieter test suite. This article proposes a merge gate you can run as a script. It does not require a new framework. It requires treating seeds, fixture hashes, and flake slots as inventory the agent cannot restock. The failure mode a pytest-zero exit misses Agents optimize for the check in fr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datacpp_8185/reject-agent-patches-that-shrink-the-property-seed-corpus-1fl9

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-03-test-the-behavior-delta-after-an-agent-patch-not-the-whole-suite]]
- [[2026-09-10-merge-agent-patches-only-when-two-test-world-receipts-match]]
- [[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]
- [[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]
- [[2026-08-30-give-your-agent-patch-a-determinism-budget-seed-locked-properties-pinned-fixtures-a-freeze-registry]]
