---
title: Why Decision Trees Don't Need Feature Scaling (And Why This Matters)
date: '2026-02-24'
source: https://dev.to/moubarakmohame4/why-decision-trees-dont-need-feature-scaling-and-why-this-matters-91d
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-02-22-your-ml-model-isnt-wrong-your-sql-probably-is]]'
- '[[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]'
- '[[2026-02-24-detcting-burnout-before-it-hits-building-an-hrv-anomaly-detector-with-isolation-forest]]'
- '[[2026-02-23-distributed-locking-in-python]]'
- '[[2026-02-23-your-mac-is-now-a-personal-doctor-analyzing-5-years-of-healthkit-data-locally-with-llama-3-mlx]]'
status: unread
---

> **TL;DR:** Ever spent hours normalizing your dataset only to wonder if it was really necessary? If you're using tree-based algorithms, I've got news for you... TL;DR Decision Trees, Random Forests, XGBoost, and LightGBM don't need…

## What’s new and why it matters
Ever spent hours normalizing your dataset only to wonder if it was really necessary? If you're using tree-based algorithms, I've got news for you... TL;DR Decision Trees, Random Forests, XGBoost, and LightGBM don't need feature scaling Distance-based algorithms (k-NN, SVM, Neural Networks) absolutely do Why? Trees use threshold comparisons, not distance calculations Let's dig into why this is the case and prove it with code! Wait, What's Feature Scaling Again? Feature scaling transforms your numerical variables to a common scale. The two most popular methods: Min-Max Scaling → squashes values…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/moubarakmohame4/why-decision-trees-dont-need-feature-scaling-and-why-this-matters-91d

## Related notes
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-02-22-your-ml-model-isnt-wrong-your-sql-probably-is]]
- [[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]
- [[2026-02-24-detcting-burnout-before-it-hits-building-an-hrv-anomaly-detector-with-isolation-forest]]
- [[2026-02-23-distributed-locking-in-python]]
- [[2026-02-23-your-mac-is-now-a-personal-doctor-analyzing-5-years-of-healthkit-data-locally-with-llama-3-mlx]]
