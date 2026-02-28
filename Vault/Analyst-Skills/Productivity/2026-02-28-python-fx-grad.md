---
title: Python f(x) & grad
date: '2026-02-28'
source: https://dev.to/slackman/python-fx-grad-158m
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#support-analytics'
- '#tool'
related:
- '[[2026-02-23-distributed-locking-in-python]]'
- '[[2026-02-26-build-a-production-rest-api-with-python-fastapi-in-10-minutes]]'
- '[[2026-01-30-the-real-python-podcast-episode-282-testing-python-code-for-scalability-whats-new-in-pandas-30]]'
- '[[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-02-24-beginner-friendly-guide-sum-of-root-to-leaf-binary-numbers---problem-1022-c-python-javascript]]'
status: unread
---

> **TL;DR:** s = [10.0] for _ in range(5): s.append(s[-1] * 0.98) s = [10.0, 9.8, 9.6] loss = lambda x: (x**2) + 20 grad = lambda x: x*2 w = 9.8 print(loss(w), grad(w)) 极值点, 导数为0, grad递减 At the extremum point, the derivative is zero,…

## What’s new and why it matters
s = [10.0] for _ in range(5): s.append(s[-1] * 0.98) s = [10.0, 9.8, 9.6] loss = lambda x: (x**2) + 20 grad = lambda x: x*2 w = 9.8 print(loss(w), grad(w)) 极值点, 导数为0, grad递减 At the extremum point, the derivative is zero, and the gradient is decreasing import matplotlib.pyplot as plt import numpy as np w = [10.0] for _ in range(100): w.append(w[-1] * 0.98) x = np.array(w) y = np.pow(x,2) + 20 y_grad = x * 2 plt.figure(figsize=(10, 6)) plt.xlim(10,0) plt.scatter(x, y, label = 'f(x)', color='blue') plt.scatter(x, y_grad, label = "grad(x)", color='red') plt.grid() plt.legend() plt.tight_layout() p…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/slackman/python-fx-grad-158m

## Related notes
- [[2026-02-23-distributed-locking-in-python]]
- [[2026-02-26-build-a-production-rest-api-with-python-fastapi-in-10-minutes]]
- [[2026-01-30-the-real-python-podcast-episode-282-testing-python-code-for-scalability-whats-new-in-pandas-30]]
- [[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-02-24-beginner-friendly-guide-sum-of-root-to-leaf-binary-numbers---problem-1022-c-python-javascript]]
