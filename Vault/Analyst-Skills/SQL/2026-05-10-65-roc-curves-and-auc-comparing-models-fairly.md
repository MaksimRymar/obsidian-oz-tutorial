---
title: '65. ROC Curves and AUC: Comparing Models Fairly'
date: '2026-05-10'
source: https://dev.to/yakhilesh/65-roc-curves-and-auc-comparing-models-fairly-59j1
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-04-22-i-priced-18-million-spy-put-spreads-across-8-years-every-bucket-was--ev-every-year-made-money]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
- '[[2026-03-04-predict-house-prices-with-python-a-beginners-machine-learning-guide]]'
- '[[2026-03-10-calculating-npv-and-irr-in-python-without-numpy-or-scipy]]'
status: unread
---

> **TL;DR:** You have two models. Model A has F1 of 0.82. Model B has F1 of 0.79. Model A wins, right? Not necessarily. F1 is calculated at one specific threshold. Maybe Model B is much better at other thresholds. Maybe on your actua…

## What’s new and why it matters
You have two models. Model A has F1 of 0.82. Model B has F1 of 0.79. Model A wins, right? Not necessarily. F1 is calculated at one specific threshold. Maybe Model B is much better at other thresholds. Maybe on your actual deployment threshold, B beats A. ROC curves show you the full picture. They plot model performance across every possible threshold at once. AUC collapses that into one number you can compare. It's the right way to compare classifiers when you haven't committed to a threshold yet. What You'll Learn Here What the ROC curve actually plots and how to read it What AUC means in pla…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yakhilesh/65-roc-curves-and-auc-comparing-models-fairly-59j1

## Related notes
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-04-22-i-priced-18-million-spy-put-spreads-across-8-years-every-bucket-was--ev-every-year-made-money]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
- [[2026-03-04-predict-house-prices-with-python-a-beginners-machine-learning-guide]]
- [[2026-03-10-calculating-npv-and-irr-in-python-without-numpy-or-scipy]]
