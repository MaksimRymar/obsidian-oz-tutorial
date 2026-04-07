---
title: 'Causal inference for credit risk: why prediction alone isn''t enough'
date: '2026-04-07'
source: https://dev.to/claire_dubois/causal-inference-for-credit-risk-why-prediction-alone-isnt-enough-1j3e
domain: Python
relevance: 🟡
tags:
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-10-calculating-npv-and-irr-in-python-without-numpy-or-scipy]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]'
- '[[2026-03-20-pandas-vs-sql-vs-polars-first-data-job-tool-choice]]'
- '[[2026-03-18-building-cddbs-part-3-scoring-llm-output-without-another-llm]]'
- '[[2026-04-06-want-to-learn-python-for-free-but-dont-know-where-to-start]]'
status: unread
---

> **TL;DR:** There's a pattern I've seen repeatedly in financial ML: a model achieves excellent predictive performance — AUC above 0.80, stable on holdout — and the team ships it. Then, six months later, someone asks "but why is the…

## What’s new and why it matters
There's a pattern I've seen repeatedly in financial ML: a model achieves excellent predictive performance — AUC above 0.80, stable on holdout — and the team ships it. Then, six months later, someone asks "but why is the model denying more applicants from this postal code?" and nobody has a good answer. Prediction and causation are different things, and conflating them is expensive in credit risk specifically. The core issue When you train a credit risk model, you're typically predicting P(default | features). This is a conditional probability — it tells you what tends to be true about people w…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/claire_dubois/causal-inference-for-credit-risk-why-prediction-alone-isnt-enough-1j3e

## Related notes
- [[2026-03-10-calculating-npv-and-irr-in-python-without-numpy-or-scipy]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]
- [[2026-03-20-pandas-vs-sql-vs-polars-first-data-job-tool-choice]]
- [[2026-03-18-building-cddbs-part-3-scoring-llm-output-without-another-llm]]
- [[2026-04-06-want-to-learn-python-for-free-but-dont-know-where-to-start]]
