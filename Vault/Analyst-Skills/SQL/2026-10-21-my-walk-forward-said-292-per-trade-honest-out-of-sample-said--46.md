---
title: My Walk-Forward Said +29.2 Per Trade. Honest Out-of-Sample Said -4.6.
date: '2026-10-21'
source: https://dev.to/wei-backtest/my-walk-forward-said-292-per-trade-honest-out-of-sample-said-46-km2
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-10-21-after-455-parameter-sets-a-t-stat-of-218-means-nothing]]'
- '[[2026-10-15-pcad-31-02-in-code-validation-checks-and-safe-sqlite3-queries-behind-30-of-the-48-items]]'
status: unread
---

> **TL;DR:** A parameter set that won on folds 1-3 lost on folds 4-5. Same strategy, same data. I ran the standard walk-forward check. Three parameter sets, five sequential folds, about 400 trades. For each fold I picked the set that…

## What’s new and why it matters
A parameter set that won on folds 1-3 lost on folds 4-5. Same strategy, same data. I ran the standard walk-forward check. Three parameter sets, five sequential folds, about 400 trades. For each fold I picked the set that was best on the previous folds only, then scored it on the fold it had never seen. Here is the whole output: fold picked oos net oos t 2 k0.75 436.5 0.88 3 k0.75 827.9 1.56 4 k0.75 -941.2 -2.51 5 k1.00 -813.2 -1.96 Stitched out-of-sample: n=107 net=-489.99 mean=-4.58 t=-0.51 In-sample best mean : +29.17 per trade Optimism gap : 33.75 per trade The parameter set k0.75 looked be…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/wei-backtest/my-walk-forward-said-292-per-trade-honest-out-of-sample-said-46-km2

## Related notes
- [[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-10-21-after-455-parameter-sets-a-t-stat-of-218-means-nothing]]
- [[2026-10-15-pcad-31-02-in-code-validation-checks-and-safe-sqlite3-queries-behind-30-of-the-48-items]]
