---
title: Put a Write Boundary Between the Agent Patch and the Oracle
date: '2026-09-06'
source: https://dev.to/datacpp_8185/put-a-write-boundary-between-the-agent-patch-and-the-oracle-j43
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-03-test-the-behavior-delta-after-an-agent-patch-not-the-whole-suite]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-08-18-shadow-test-free-model-endpoint-changes-before-you-rely-on-them]]'
- '[[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]'
- '[[2026-08-30-give-your-agent-patch-a-determinism-budget-seed-locked-properties-pinned-fixtures-a-freeze-registry]]'
status: unread
---

> **TL;DR:** An agent patch that can edit its own tests is not under test. Green CI then records agreement with a rewritten oracle, not preservation of the behavior you meant to keep. The practical fix is a write boundary: the model…

## What’s new and why it matters
An agent patch that can edit its own tests is not under test. Green CI then records agreement with a rewritten oracle, not preservation of the behavior you meant to keep. The practical fix is a write boundary: the model may change production code, and it may add tests in a sandbox directory, but it cannot own the property checks, the fixtures, or the flake freeze that decide merge. The failure is oracle capture Agent patches fail in a different way than human patches. They often make the suite green by moving the goalposts. A skipped test, a loosened assertion, a regenerated golden file, and a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datacpp_8185/put-a-write-boundary-between-the-agent-patch-and-the-oracle-j43

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-03-test-the-behavior-delta-after-an-agent-patch-not-the-whole-suite]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-08-18-shadow-test-free-model-endpoint-changes-before-you-rely-on-them]]
- [[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]
- [[2026-08-30-give-your-agent-patch-a-determinism-budget-seed-locked-properties-pinned-fixtures-a-freeze-registry]]
