---
title: Inventory the Test Surface Before You Score an Agent Patch
date: '2026-09-22'
source: https://dev.to/datacpp_8185/inventory-the-test-surface-before-you-score-an-agent-patch-43fb
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]'
- '[[2026-09-21-score-agent-patches-on-a-frozen-surface-ledger-the-flakes]]'
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-11-reject-agent-patches-that-shrink-the-property-seed-corpus]]'
- '[[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]'
status: unread
---

> **TL;DR:** A green pytest exit code on the pull request tree is not a score. If an agent can edit tests, fixtures, markers, or skip lists, that exit code measures agreement with the patch's own story. Score against a detached witne…

## What’s new and why it matters
A green pytest exit code on the pull request tree is not a score. If an agent can edit tests, fixtures, markers, or skip lists, that exit code measures agreement with the patch's own story. Score against a detached witness pack. Count assertions. Keep flakes in a ledger the agent cannot rewrite. The rest of this article is a concrete inventory protocol. It is not a model review. It does not claim that any gate is complete. It does claim that you can fail a patch for shrinking the test surface before you even discuss the production diff. What a green run can hide Agent patches fail in boring wa…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datacpp_8185/inventory-the-test-surface-before-you-score-an-agent-patch-43fb

## Related notes
- [[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]
- [[2026-09-21-score-agent-patches-on-a-frozen-surface-ledger-the-flakes]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-11-reject-agent-patches-that-shrink-the-property-seed-corpus]]
- [[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]
