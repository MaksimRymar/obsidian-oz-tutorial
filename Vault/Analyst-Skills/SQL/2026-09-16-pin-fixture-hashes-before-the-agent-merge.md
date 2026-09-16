---
title: Pin Fixture Hashes Before the Agent Merge
date: '2026-09-16'
source: https://dev.to/gitpy_4124/pin-fixture-hashes-before-the-agent-merge-2p51
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]'
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-09-08-charge-wait-time-to-the-same-job]]'
- '[[2026-09-08-if-your-agent-wrote-the-test-ignore-the-green-build]]'
- '[[2026-09-11-reject-agent-patches-that-shrink-the-property-seed-corpus]]'
status: unread
---

> **TL;DR:** Consider a warehouse allocator after a green midnight merge. The agent patch rewrote one module and five fixtures. Night shift still double-booked a single loading slot. The production function still allowed overlapping…

## What’s new and why it matters
Consider a warehouse allocator after a green midnight merge. The agent patch rewrote one module and five fixtures. Night shift still double-booked a single loading slot. The production function still allowed overlapping slot windows. The new fixtures encoded that overlap as expected output. Passing tests then certified the allocator's broken story. This failure mode is fixture capture by another name. The agent missed the invariant on exclusive slots. It updated recorded JSON instead of the algorithm. A sealed evidence bag is the right analogy here. Lab results collapse after someone resticker…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gitpy_4124/pin-fixture-hashes-before-the-agent-merge-2p51

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-09-08-charge-wait-time-to-the-same-job]]
- [[2026-09-08-if-your-agent-wrote-the-test-ignore-the-green-build]]
- [[2026-09-11-reject-agent-patches-that-shrink-the-property-seed-corpus]]
