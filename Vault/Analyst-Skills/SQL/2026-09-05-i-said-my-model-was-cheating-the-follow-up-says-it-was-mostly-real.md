---
title: I Said My Model Was Cheating. The Follow-up Says It Was Mostly Real.
date: '2026-09-05'
source: https://dev.to/turingrtss/i-said-my-model-was-cheating-the-follow-up-says-it-was-mostly-real-1iba
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-03-06-5-database-design-mistakes-i-keep-seeing-and-how-to-catch-them-early]]'
- '[[2026-04-20-how-my-journey-has-been-into-understanding-sql]]'
- '[[2026-08-05-3-async-python-patterns-i-wish-i-learned-sooner-with-real-code]]'
- '[[2026-08-19-final-weeks-of-gsoc]]'
status: unread
---

> **TL;DR:** Last week I published a paper claiming that a vulnerability detection model was mostly reading comments instead of code. I predicted accuracy would drop significantly after stripping comments. I ran the follow-up experim…

## What’s new and why it matters
Last week I published a paper claiming that a vulnerability detection model was mostly reading comments instead of code. I predicted accuracy would drop significantly after stripping comments. I ran the follow-up experiment. I was wrong about the magnitude. The Ablation Five conditions, same model (TF-IDF + logistic regression), same dataset: Condition Accuracy Drop Baseline (with comments) 84.7% -- Comments stripped 82.6% -2.1% Label words removed 83.9% -0.8% Both combined 82.6% -2.1% Full clean (comments + labels + identifiers) 81.1% -3.6% Only 3.6 percentage points was leakage. The model ke…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/turingrtss/i-said-my-model-was-cheating-the-follow-up-says-it-was-mostly-real-1iba

## Related notes
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-03-06-5-database-design-mistakes-i-keep-seeing-and-how-to-catch-them-early]]
- [[2026-04-20-how-my-journey-has-been-into-understanding-sql]]
- [[2026-08-05-3-async-python-patterns-i-wish-i-learned-sooner-with-real-code]]
- [[2026-08-19-final-weeks-of-gsoc]]
