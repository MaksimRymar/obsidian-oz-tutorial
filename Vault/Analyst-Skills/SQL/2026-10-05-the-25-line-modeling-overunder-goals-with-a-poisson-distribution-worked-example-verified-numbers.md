---
title: 'The 2.5 line: modeling over/under goals with a Poisson distribution (worked
  example, verified numbers)'
date: '2026-10-05'
source: https://dev.to/mystiqueracing/the-25-line-modeling-overunder-goals-with-a-poisson-distribution-worked-example-verified-17ba
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-18-how-we-grade-hundreds-of-sports-picks-a-day-in-public]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]'
- '[[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]'
- '[[2026-08-27-how-accurately-can-complex-option-trades-be-signed-first-grading-against-exchange-truth]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
status: unread
---

> **TL;DR:** One of the highest-turnover football markets is deceptively simple: will the total goals in a match go over or under 2.5 ? Where does that line come from, and what is the "fair" probability of each side? Here's the full…

## What’s new and why it matters
One of the highest-turnover football markets is deceptively simple: will the total goals in a match go over or under 2.5 ? Where does that line come from, and what is the "fair" probability of each side? Here's the full derivation, with numbers you can reproduce from one formula. Step 1: goals are (approximately) Poisson A team's goal count in a match can be approximated by a Poisson distribution: P(X = k) = λ ^ k · e ^ (−λ) / k! where λ is the team's expected goals (estimated from recent attack strength, opponent defense, home/away). Two independent Poisson variables sum to a Poisson with λ =…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mystiqueracing/the-25-line-modeling-overunder-goals-with-a-poisson-distribution-worked-example-verified-17ba

## Related notes
- [[2026-09-18-how-we-grade-hundreds-of-sports-picks-a-day-in-public]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]
- [[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]
- [[2026-08-27-how-accurately-can-complex-option-trades-be-signed-first-grading-against-exchange-truth]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
