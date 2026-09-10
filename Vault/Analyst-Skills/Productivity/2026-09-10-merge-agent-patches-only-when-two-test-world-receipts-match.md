---
title: Merge Agent Patches Only When Two Test-World Receipts Match
date: '2026-09-10'
source: https://dev.to/datacpp_8185/merge-agent-patches-only-when-two-test-world-receipts-match-36oj
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#productivity'
- '#python'
- '#sql'
- '#tableau'
- '#tool'
related:
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-08-13-stop-asking-coding-models-to-write-code-test-whether-they-can-review-a-patch]]'
- '[[2026-09-07-dont-merge-the-first-green-check-hooks-fixtures-and-a-flake-budget]]'
- '[[2026-09-07-score-the-trace-not-the-final-payload]]'
status: unread
---

> **TL;DR:** A green CI job is not proof that an agent patch preserved the test world. Fixtures can be rewritten to match new output. Property suites can shrink their domain or their iteration budget. Flaky tests can turn into unname…

## What’s new and why it matters
A green CI job is not proof that an agent patch preserved the test world. Fixtures can be rewritten to match new output. Property suites can shrink their domain or their iteration budget. Flaky tests can turn into unnamed skips. Merge on a lockfile and two matching receipts, not on a single passing run. The protocol below is a proposal with runnable scoring code. It is not a report of production incident rates, and it does not assume a particular CI vendor. The test world is the proof, not the job status The test world is the set of objects that give tests their meaning. Three parts matter on…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datacpp_8185/merge-agent-patches-only-when-two-test-world-receipts-match-36oj

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-08-13-stop-asking-coding-models-to-write-code-test-whether-they-can-review-a-patch]]
- [[2026-09-07-dont-merge-the-first-green-check-hooks-fixtures-and-a-flake-budget]]
- [[2026-09-07-score-the-trace-not-the-final-payload]]
