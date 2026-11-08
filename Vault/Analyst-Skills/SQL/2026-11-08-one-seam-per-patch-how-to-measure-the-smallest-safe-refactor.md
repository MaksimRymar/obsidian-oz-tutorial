---
title: 'One Seam Per Patch: How to Measure the Smallest Safe Refactor'
date: '2026-11-08'
source: https://dev.to/hackrs_6393/one-seam-per-patch-how-to-measure-the-smallest-safe-refactor-135
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-09-14-characterization-tests-first-record-the-behavior-then-make-one-safe-change]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
status: unread
---

> **TL;DR:** The smallest safe change is measurable, not a feeling. Three numbers define it. seams — outside-world calls the patch moves, per entry point. surface — exported names and signatures. undo — commands needed to reverse the…

## What’s new and why it matters
The smallest safe change is measurable, not a feeling. Three numbers define it. seams — outside-world calls the patch moves, per entry point. surface — exported names and signatures. undo — commands needed to reverse the patch. A patch qualifies when seams move by exactly one row, surface stays compatible, and undo is one command. Anything else is a rewrite wearing a small patch's clothes. The counts below come from a five-order recording in a messy Python billing module. Your numbers will differ. The method does not. 0. Pin behavior before counting anything Characterization tests come first.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hackrs_6393/one-seam-per-patch-how-to-measure-the-smallest-safe-refactor-135

## Related notes
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-09-14-characterization-tests-first-record-the-behavior-then-make-one-safe-change]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
