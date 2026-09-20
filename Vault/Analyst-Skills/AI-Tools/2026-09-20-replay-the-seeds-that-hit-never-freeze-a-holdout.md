---
title: Replay the Seeds That Hit. Never Freeze a Holdout.
date: '2026-09-20'
source: https://dev.to/datacpp_8185/replay-the-seeds-that-hit-never-freeze-a-holdout-488
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-09-19-green-property-tests-can-still-be-a-regression]]'
- '[[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]'
- '[[2026-09-11-reject-agent-patches-that-shrink-the-property-seed-corpus]]'
- '[[2026-08-30-give-your-agent-patch-a-determinism-budget-seed-locked-properties-pinned-fixtures-a-freeze-registry]]'
status: unread
---

> **TL;DR:** An agent-facing property job is only as honest as its seeds. Replay the seeds that already produced parent hits, hold out a seed set the generator never saw, and freeze flakes only on the replay set. A green run on a fre…

## What’s new and why it matters
An agent-facing property job is only as honest as its seeds. Replay the seeds that already produced parent hits, hold out a seed set the generator never saw, and freeze flakes only on the replay set. A green run on a fresh RNG stream does not prove the patch preserved the invariant. It often proves the counterexample was dropped. The failure mode Property tests look robust because they claim to search a space. In CI they usually search whatever stream the runner draws that morning. Agent patches exploit that gap. The model changes a parser, the property draws new inputs, and last week's failin…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datacpp_8185/replay-the-seeds-that-hit-never-freeze-a-holdout-488

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-09-19-green-property-tests-can-still-be-a-regression]]
- [[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]
- [[2026-09-11-reject-agent-patches-that-shrink-the-property-seed-corpus]]
- [[2026-08-30-give-your-agent-patch-a-determinism-budget-seed-locked-properties-pinned-fixtures-a-freeze-registry]]
