---
title: 'Shadow Replay or Read-Only Canary: Two Ways to Ship Agent-Written SQL'
date: '2026-10-27'
source: https://dev.to/dataio_4921/shadow-replay-or-read-only-canary-two-ways-to-ship-agent-written-sql-597k
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-22-advisory-locks-or-skip-locked-a-debate-for-agent-sql-workers]]'
status: unread
---

> **TL;DR:** A rewrite that passed every gate and still moved the number Imagine a team approving an agent-drafted rewrite of a fourteen-table revenue query. The parser gate passed, the read-only guard passed, and the dashboard still…

## What’s new and why it matters
A rewrite that passed every gate and still moved the number Imagine a team approving an agent-drafted rewrite of a fourteen-table revenue query. The parser gate passed, the read-only guard passed, and the dashboard still drifted by three percent overnight. The defect was one LEFT JOIN that the draft had promoted into an inner join, which is invisible to syntax checks and obvious to anyone comparing rows. That gap defines the real shipping problem. Getting an agent to produce syntactically valid SQL is a solved loop; proving the draft returns the same answers as the query it replaces is the par…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dataio_4921/shadow-replay-or-read-only-canary-two-ways-to-ship-agent-written-sql-597k

## Related notes
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-22-advisory-locks-or-skip-locked-a-debate-for-agent-sql-workers]]
