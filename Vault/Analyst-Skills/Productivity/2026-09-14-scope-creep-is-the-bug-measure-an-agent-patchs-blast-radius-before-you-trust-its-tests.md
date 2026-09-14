---
title: 'Scope Creep Is the Bug: Measure an Agent Patch''s Blast Radius Before You
  Trust Its Tests'
date: '2026-09-14'
source: https://dev.to/datacpp_8185/scope-creep-is-the-bug-measure-an-agent-patchs-blast-radius-before-you-trust-its-tests-4fen
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
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-09-03-test-the-behavior-delta-after-an-agent-patch-not-the-whole-suite]]'
- '[[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]'
- '[[2026-09-11-reject-agent-patches-that-shrink-the-property-seed-corpus]]'
- '[[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]'
status: unread
---

> **TL;DR:** A patch that picks which tests it needs is a patch that decides how much it gets checked. That is the second half of agent-patch review, and it is the half most teams skip. Oracle independence tells you whether the check…

## What’s new and why it matters
A patch that picks which tests it needs is a patch that decides how much it gets checked. That is the second half of agent-patch review, and it is the half most teams skip. Oracle independence tells you whether the check could have failed; scope tells you whether the check was pointed at the code the diff actually touched. This is a walkthrough of a small planner that answers the second question from the diff itself, then hands the merge decision back to a human with an explicit promote-or-block verdict. The failure mode, stated concretely An agent edits app/pricing/tax.py , adds tests/test_ta…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datacpp_8185/scope-creep-is-the-bug-measure-an-agent-patchs-blast-radius-before-you-trust-its-tests-4fen

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-09-03-test-the-behavior-delta-after-an-agent-patch-not-the-whole-suite]]
- [[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]
- [[2026-09-11-reject-agent-patches-that-shrink-the-property-seed-corpus]]
- [[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]
