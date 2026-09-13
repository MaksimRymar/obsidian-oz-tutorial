---
title: A Frozen Test That Turns Green Is a Merge Blocker
date: '2026-09-13'
source: https://dev.to/datacpp_8185/a-frozen-test-that-turns-green-is-a-merge-blocker-32ii
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]'
- '[[2026-09-11-reject-agent-patches-that-shrink-the-property-seed-corpus]]'
- '[[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
status: unread
---

> **TL;DR:** Green CI is the wrong merge signal for an agent patch. A frozen flake that starts passing is a contract break, not a win. Score the diff with three AND-gated columns: human-owned properties, hashed fixtures, and a freeze…

## What’s new and why it matters
Green CI is the wrong merge signal for an agent patch. A frozen flake that starts passing is a contract break, not a win. Score the diff with three AND-gated columns: human-owned properties, hashed fixtures, and a freeze file the agent is forbidden to graduate. That rule is the whole strategy. Properties say what must stay true. Fixtures say which bytes are the world. The freeze file says which tests are not evidence. If any column is incomplete, the merge score is zero. A green check from a test the freeze still owns does not raise it. Why a passing flake is the failure Agent patches optimize…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datacpp_8185/a-frozen-test-that-turns-green-is-a-merge-blocker-32ii

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]
- [[2026-09-11-reject-agent-patches-that-shrink-the-property-seed-corpus]]
- [[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
