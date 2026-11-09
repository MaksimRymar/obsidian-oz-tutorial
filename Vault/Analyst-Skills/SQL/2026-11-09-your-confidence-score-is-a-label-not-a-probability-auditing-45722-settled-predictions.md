---
title: 'Your confidence score is a label, not a probability: auditing 45,722 settled
  predictions'
date: '2026-11-09'
source: https://dev.to/soccerdream_ai/your-confidence-score-is-a-label-not-a-probability-auditing-45722-settled-predictions-2o72
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-08-23-sql-window-frames-explained-how-unbounded-preceding-creates-a-running-total]]'
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
status: unread
---

> **TL;DR:** Most prediction systems ship two numbers: a call, and a confidence. The confidence is usually an integer — 1 to 10, 60 to 95, whatever reads well in a UI. Everyone downstream then treats it as a probability, because it i…

## What’s new and why it matters
Most prediction systems ship two numbers: a call, and a confidence. The confidence is usually an integer — 1 to 10, 60 to 95, whatever reads well in a UI. Everyone downstream then treats it as a probability, because it is a number between 0 and 100 and probabilities are numbers between 0 and 100. That inference is where audits die. In our production table, confidence is an integer from 1 to 10 assigned at call time. It is not a probability, it never was, and the table below is the proof. The dataset The numbers come from one PostgreSQL table, ai_predictions , joined to matches for settlement f…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/soccerdream_ai/your-confidence-score-is-a-label-not-a-probability-auditing-45722-settled-predictions-2o72

## Related notes
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-08-23-sql-window-frames-explained-how-unbounded-preceding-creates-a-running-total]]
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
