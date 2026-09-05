---
title: Same code, same seed, different answer
date: '2026-09-05'
source: https://dev.to/farabhi/same-code-same-seed-different-answer-29f8
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-12-im-building-an-algorithmic-trading-system-in-python]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
status: unread
---

> **TL;DR:** The same code, with the same fixed seed and the same input file, gave different answers on different machines. I noticed that early, but waved it away. The differences looked cosmetic, less successful runs didn't disprov…

## What’s new and why it matters
The same code, with the same fixed seed and the same input file, gave different answers on different machines. I noticed that early, but waved it away. The differences looked cosmetic, less successful runs didn't disprove my findings, so I lulled myself with a comfortable story about a stochastic process. That ended when I tried to increase the sample size. Unexpectedly, the result I had been building on collapsed, and with it my reason for not caring. The findings were not supported by my experiment anymore, so I naturally suspected the machine-related variances were early warning signs. The…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/farabhi/same-code-same-seed-different-answer-29f8

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-12-im-building-an-algorithmic-trading-system-in-python]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
