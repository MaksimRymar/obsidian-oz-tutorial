---
title: Record One Nested Decision, Then Extract a Single Predicate
date: '2026-09-23'
source: https://dev.to/webx_2736/record-one-nested-decision-then-extract-a-single-predicate-17lp
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-08-hash-the-side-effect-ledger-before-you-accept-a-cleanup-refactor]]'
- '[[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]'
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]'
status: unread
---

> **TL;DR:** A pricing function still folds region rules, bulk surcharges, and coupon stacking into one nested block. A teammate asks an assistant to tidy that module before a tax change lands next week. The first generated patch rew…

## What’s new and why it matters
A pricing function still folds region rules, bulk surcharges, and coupon stacking into one nested block. A teammate asks an assistant to tidy that module before a tax change lands next week. The first generated patch rewrites four helpers, renames two exceptions, and flips a surcharge for twelve-item carts. Review then spends more time reconstructing prior behavior than evaluating the one extract that was actually needed. This walkthrough treats that failure as a process problem rather than a taste debate about clean code. The useful unit of work is one nested decision on one hot path, recorde…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/webx_2736/record-one-nested-decision-then-extract-a-single-predicate-17lp

## Related notes
- [[2026-09-08-hash-the-side-effect-ledger-before-you-accept-a-cleanup-refactor]]
- [[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]
