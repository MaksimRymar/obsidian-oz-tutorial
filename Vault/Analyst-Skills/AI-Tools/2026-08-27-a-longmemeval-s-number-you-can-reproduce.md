---
title: A LongMemEval-S number you can reproduce
date: '2026-08-27'
source: https://dev.to/sovantica/a-longmemeval-s-number-you-can-reproduce-2l0n
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-08-11-code-interpreter-is-infrastructure-not-a-prompt]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
status: unread
---

> **TL;DR:** We held off on posting a benchmark for a long time. Not because we didn't have runs - because most memory benchmarks you read are a number with no way to check it. A blog says "X%", and you have no idea what reader answe…

## What’s new and why it matters
We held off on posting a benchmark for a long time. Not because we didn't have runs - because most memory benchmarks you read are a number with no way to check it. A blog says "X%", and you have no idea what reader answered the questions, what judge scored them, how much context the retriever was allowed to feed, or whether an LLM quietly did the hard part inside the "memory" layer. So the number tells you almost nothing about the memory system. Here is one we're comfortable standing behind, because you can run it yourself. The result On LongMemEval-S , the full 500-question set, Engrava 0.6.0…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/sovantica/a-longmemeval-s-number-you-can-reproduce-2l0n

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-08-11-code-interpreter-is-infrastructure-not-a-prompt]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
