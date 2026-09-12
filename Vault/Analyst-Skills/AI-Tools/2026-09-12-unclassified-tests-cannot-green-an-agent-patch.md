---
title: Unclassified Tests Cannot Green an Agent Patch
date: '2026-09-12'
source: https://dev.to/datacpp_8185/unclassified-tests-cannot-green-an-agent-patch-5dd3
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-11-reject-agent-patches-that-shrink-the-property-seed-corpus]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-09-03-test-the-behavior-delta-after-an-agent-patch-not-the-whole-suite]]'
- '[[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]'
- '[[2026-08-13-stop-asking-coding-models-to-write-code-test-whether-they-can-review-a-patch]]'
status: unread
---

> **TL;DR:** An agent patch is not green because a runner printed green. It is green only when every passing test it cites already has a class in a ledger: locked fixture, property check, or quarantine. Unclassified tests are not evi…

## What’s new and why it matters
An agent patch is not green because a runner printed green. It is green only when every passing test it cites already has a class in a ledger: locked fixture, property check, or quarantine. Unclassified tests are not evidence. They are unlabeled noise the model can reshape until the suite agrees. That rule is the whole merge policy. The rest of this article is a concrete ledger, a gate script, and a decision table you can run before git merge . Agent patches fail this policy in a narrow way. They do not need to delete assertions. They only need to move a test from "unknown" to "passed" by rewr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datacpp_8185/unclassified-tests-cannot-green-an-agent-patch-5dd3

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-11-reject-agent-patches-that-shrink-the-property-seed-corpus]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-09-03-test-the-behavior-delta-after-an-agent-patch-not-the-whole-suite]]
- [[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]
- [[2026-08-13-stop-asking-coding-models-to-write-code-test-whether-they-can-review-a-patch]]
