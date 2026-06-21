---
title: How I improved my fact-checker from F1 0.655 0.813 — what actually changed
date: '2026-06-21'
source: https://dev.to/ashg2099/how-i-improved-my-fact-checker-from-f1-0655-0813-what-actually-changed-455a
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]'
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
status: unread
---

> **TL;DR:** I built a multilingual fact-checker using XLM-RoBERTa fine-tuned on the FEVER dataset. The first version hit F1 0.655. Not bad, but it kept misfiring on obvious real-world claims. Earth being the third planet from the Su…

## What’s new and why it matters
I built a multilingual fact-checker using XLM-RoBERTa fine-tuned on the FEVER dataset. The first version hit F1 0.655. Not bad, but it kept misfiring on obvious real-world claims. Earth being the third planet from the Sun returned FALSE at 76% confidence. Something was fundamentally wrong. A commenter identified the issue immediately: I was training the model on claims alone, with no evidence. FEVER is not a claim classification task. It's a Natural Language Inference task — the model is supposed to verify a claim against evidence, not guess from the claim text alone. I had been training it wr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashg2099/how-i-improved-my-fact-checker-from-f1-0655-0813-what-actually-changed-455a

## Related notes
- [[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
