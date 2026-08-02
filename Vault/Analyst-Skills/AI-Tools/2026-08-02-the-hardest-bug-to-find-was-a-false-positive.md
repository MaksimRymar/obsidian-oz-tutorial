---
title: The Hardest Bug to Find Was a False Positive.
date: '2026-08-02'
source: https://dev.to/mohi_uddin/the-hardest-bug-to-find-was-a-false-positive-48cc
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-03-28-how-to-add-reputation-scoring-to-your-langchain-agent-in-5-lines]]'
- '[[2026-03-13-i-found-a-0575-drift-score-between-two-consecutive-llm-runs-heres-exactly-what-changed]]'
- '[[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]'
status: unread
---

> **TL;DR:** The Benchmark Behind Proactive Scan On Tuesday we shipped Proactive Scan: one command that ranks your riskiest files and reads each with cross-file context, before anything crashes. Today we're publishing the benchmark b…

## What’s new and why it matters
The Benchmark Behind Proactive Scan On Tuesday we shipped Proactive Scan: one command that ranks your riskiest files and reads each with cross-file context, before anything crashes. Today we're publishing the benchmark behind it. All of it: the numbers, the methodology, the part where our first version cried wolf, and the kinds of bugs it still misses. The Result 28 test cases, written fresh for this benchmark. 20 files with planted defects, 8 clean files as controls. Category Score What was planted Single-file defects 8/8 SQL injection, resource leak, division by zero, mutable default arg, ba…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mohi_uddin/the-hardest-bug-to-find-was-a-false-positive-48cc

## Related notes
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-03-28-how-to-add-reputation-scoring-to-your-langchain-agent-in-5-lines]]
- [[2026-03-13-i-found-a-0575-drift-score-between-two-consecutive-llm-runs-heres-exactly-what-changed]]
- [[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]
