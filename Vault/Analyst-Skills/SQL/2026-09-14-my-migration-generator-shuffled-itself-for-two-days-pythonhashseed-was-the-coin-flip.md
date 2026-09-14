---
title: My Migration Generator Shuffled Itself for Two Days. PYTHONHASHSEED Was the
  Coin Flip.
date: '2026-09-14'
source: https://dev.to/codepy_1473/my-migration-generator-shuffled-itself-for-two-days-pythonhashseed-was-the-coin-flip-lg0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]'
- '[[2026-08-20-build-a-50-line-harness-to-test-whether-a-free-model-endpoint-can-fix-broken-json]]'
- '[[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]'
- '[[2026-08-31-a-passing-check-is-a-claim-about-what-ran-not-whats-true]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
status: unread
---

> **TL;DR:** Two consecutive runs of the same command emitted the same SQL statements in a different order, and I did not believe my own terminal. I re-ran it four times, redirected each run into a file, and compared them the way you…

## What’s new and why it matters
Two consecutive runs of the same command emitted the same SQL statements in a different order, and I did not believe my own terminal. I re-ran it four times, redirected each run into a file, and compared them the way you check whether the fridge light really goes off. The statement set was identical, the sequence was not, and the applied-version check that consumed it failed on roughly every other run. These are my field notes from those two days: the hypotheses I burned, the reproduction I should have written in the first hour, and the seed matrix I now run before I accuse anyone's framework…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/codepy_1473/my-migration-generator-shuffled-itself-for-two-days-pythonhashseed-was-the-coin-flip-lg0

## Related notes
- [[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]
- [[2026-08-20-build-a-50-line-harness-to-test-whether-a-free-model-endpoint-can-fix-broken-json]]
- [[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]
- [[2026-08-31-a-passing-check-is-a-claim-about-what-ran-not-whats-true]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
