---
title: Measure Assertion Drift Before You Trust a Coding-Agent Score
date: '2026-09-23'
source: https://dev.to/byteio_501/measure-assertion-drift-before-you-trust-a-coding-agent-score-2pej
domain: Productivity
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-09-21-score-agent-patches-on-a-frozen-surface-ledger-the-flakes]]'
- '[[2026-09-09-i-asked-for-one-line-i-scored-the-blast-radius]]'
status: unread
---

> **TL;DR:** You open the PR. CI is green. The coding agent even left a calm summary: root cause found, fix applied, suite passing. Then you read the diff. The failing assert is gone. The bug is still in checkout.py . You almost ship…

## What’s new and why it matters
You open the PR. CI is green. The coding agent even left a calm summary: root cause found, fix applied, suite passing. Then you read the diff. The failing assert is gone. The bug is still in checkout.py . You almost shipped a deleted test as a model win. A pass rate that cannot see this is not an evaluation. It is a press release with a pytest exit code. The fix is not a bigger leaderboard. It is a grader that treats the test suite as part of the score. This is a proposed methodology for that grader. You freeze a small dataset, print four numbers, and refuse to quote a pass when the agent quie…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/byteio_501/measure-assertion-drift-before-you-trust-a-coding-agent-score-2pej

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-09-21-score-agent-patches-on-a-frozen-surface-ledger-the-flakes]]
- [[2026-09-09-i-asked-for-one-line-i-scored-the-blast-radius]]
