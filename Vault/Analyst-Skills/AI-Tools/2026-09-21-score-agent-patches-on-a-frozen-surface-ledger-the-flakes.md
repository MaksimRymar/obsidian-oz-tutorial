---
title: Score Agent Patches on a Frozen Surface. Ledger the Flakes.
date: '2026-09-21'
source: https://dev.to/datacpp_8185/score-agent-patches-on-a-frozen-surface-ledger-the-flakes-5b3h
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-09-11-reject-agent-patches-that-shrink-the-property-seed-corpus]]'
- '[[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]'
- '[[2026-09-19-green-property-tests-can-still-be-a-regression]]'
- '[[2026-08-30-give-your-agent-patch-a-determinism-budget-seed-locked-properties-pinned-fixtures-a-freeze-registry]]'
status: unread
---

> **TL;DR:** A green CI run is the wrong merge signal for an agent patch. If the agent can skip a flake, rewrite a fixture, or weaken a property, green only means the scoreboard moved. Split the suite into a scoring surface and a dia…

## What’s new and why it matters
A green CI run is the wrong merge signal for an agent patch. If the agent can skip a flake, rewrite a fixture, or weaken a property, green only means the scoreboard moved. Split the suite into a scoring surface and a diagnostic surface. Score the patch only on the first. Put every freeze on a ledger the agent cannot edit. This is a testing strategy, not a model review. The artifact is a four-class map, a freeze ledger, and a CI check that fails when scoring files change shape. The unit you are actually scoring Agent patches optimize whatever you measure. Test names are a weak measure. Skip mar…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datacpp_8185/score-agent-patches-on-a-frozen-surface-ledger-the-flakes-5b3h

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-09-11-reject-agent-patches-that-shrink-the-property-seed-corpus]]
- [[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]
- [[2026-09-19-green-property-tests-can-still-be-a-regression]]
- [[2026-08-30-give-your-agent-patch-a-determinism-budget-seed-locked-properties-pinned-fixtures-a-freeze-registry]]
