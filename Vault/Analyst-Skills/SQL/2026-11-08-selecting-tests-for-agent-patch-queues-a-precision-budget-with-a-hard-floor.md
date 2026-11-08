---
title: 'Selecting Tests for Agent Patch Queues: A Precision Budget With a Hard Floor'
date: '2026-11-08'
source: https://dev.to/datacpp_8185/selecting-tests-for-agent-patch-queues-a-precision-budget-with-a-hard-floor-4m46
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]'
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
status: unread
---

> **TL;DR:** Selecting Tests for Agent Patch Queues: A Precision Budget With a Hard Floor Conclusion first: when model-generated patches arrive faster than your suite can run, do not choose between "run everything" and "run something…

## What’s new and why it matters
Selecting Tests for Agent Patch Queues: A Precision Budget With a Hard Floor Conclusion first: when model-generated patches arrive faster than your suite can run, do not choose between "run everything" and "run something random". Build a test selector, give it a hard floor of always-run tests, and track a single number — how many real failures the selector lets escape. The selector is only trustworthy after you have measured that number on your own replay history. This post is about the selection layer, not the gate. Gating logic decides whether a patch is acceptable . Selection decides which…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datacpp_8185/selecting-tests-for-agent-patch-queues-a-precision-budget-with-a-hard-floor-4m46

## Related notes
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
