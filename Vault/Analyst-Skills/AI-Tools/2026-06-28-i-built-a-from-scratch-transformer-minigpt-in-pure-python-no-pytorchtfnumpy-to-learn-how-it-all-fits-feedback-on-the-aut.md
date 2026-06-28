---
title: I built a from-scratch Transformer + MiniGPT in pure Python (no PyTorch/TF/NumPy)
  to learn how it all fits feedback on the autograd?
date: '2026-06-28'
source: https://dev.to/furkannarkn/i-built-a-from-scratch-transformer-minigpt-in-pure-python-no-pytorchtfnumpy-to-learn-how-it-3dgj
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-06-15-building-a-scientific-computing-platform-quantum-ml-math-in-pure-python-without-numpy]]'
- '[[2026-03-15-i-built-the-first-open-source-fp8-linear-solver-in-python-2-3x-faster-than-cublas]]'
- '[[2026-06-22-bvostfus-python-real-or-fake-truth-risks-reality-explained]]'
- '[[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]'
- '[[2026-03-17-i-built-a-cognitive-layer-for-ai-agents-that-learns-without-llm-calls]]'
- '[[2026-04-08-i-built-a-bot-that-answers-github-discussions-using-free-ai-models-heres-what-i-learned]]'
status: unread
---

> **TL;DR:** Cognitive Discovery System (CDS) a scientific computing library written in pure Python. No NumPy, no SciPy, no compiled extensions. Zero dependencies, runs anywhere. 18 modules: quantum circuit simulation, FFT/IFFT, ODE…

## What’s new and why it matters
Cognitive Discovery System (CDS) a scientific computing library written in pure Python. No NumPy, no SciPy, no compiled extensions. Zero dependencies, runs anywhere. 18 modules: quantum circuit simulation, FFT/IFFT, ODE solvers, numerical integration, linear algebra, statistics, Monte Carlo, optimization, graph algorithms, symbolic math, a from-scratch NLP stack (BPE → attention → MiniGPT + scalar autograd), and a hypothesis-generation module. The idea: pure Python can't beat C on raw loops, but it can close the gap algorithmically — O(N log N) FFT, O(N³) LU decomposition (instead of O(N!) det…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/furkannarkn/i-built-a-from-scratch-transformer-minigpt-in-pure-python-no-pytorchtfnumpy-to-learn-how-it-3dgj

## Related notes
- [[2026-06-15-building-a-scientific-computing-platform-quantum-ml-math-in-pure-python-without-numpy]]
- [[2026-03-15-i-built-the-first-open-source-fp8-linear-solver-in-python-2-3x-faster-than-cublas]]
- [[2026-06-22-bvostfus-python-real-or-fake-truth-risks-reality-explained]]
- [[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]
- [[2026-03-17-i-built-a-cognitive-layer-for-ai-agents-that-learns-without-llm-calls]]
- [[2026-04-08-i-built-a-bot-that-answers-github-discussions-using-free-ai-models-heres-what-i-learned]]
