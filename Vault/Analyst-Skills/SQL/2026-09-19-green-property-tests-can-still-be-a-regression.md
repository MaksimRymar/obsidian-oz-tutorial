---
title: Green Property Tests Can Still Be a Regression
date: '2026-09-19'
source: https://dev.to/datacpp_8185/green-property-tests-can-still-be-a-regression-15e1
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-11-reject-agent-patches-that-shrink-the-property-seed-corpus]]'
- '[[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]'
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-09-17-reject-agent-patches-that-pass-only-in-default-collection-order]]'
- '[[2026-09-07-score-the-trace-not-the-final-payload]]'
status: unread
---

> **TL;DR:** A green property test does not prove that an agent patch preserved the contract. It only proves that the current generator produced no counterexample. Shrink the generator, add a broad assume() , or rewrite the fixture t…

## What’s new and why it matters
A green property test does not prove that an agent patch preserved the contract. It only proves that the current generator produced no counterexample. Shrink the generator, add a broad assume() , or rewrite the fixture the property reads, and the suite still passes. Treat that as a merge defect. The control proposed here is a triple lock plus a freeze of the oracle, not of the test. Fingerprint the generator. Bound the assume-reject rate. Hash the fixtures the property consumes. Require an independent replay to agree. If any of those signals move, the oracle loses its vote until a human classi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datacpp_8185/green-property-tests-can-still-be-a-regression-15e1

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-11-reject-agent-patches-that-shrink-the-property-seed-corpus]]
- [[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-09-17-reject-agent-patches-that-pass-only-in-default-collection-order]]
- [[2026-09-07-score-the-trace-not-the-final-payload]]
