---
title: 'Slopsquatting in Python: What 205,474 Hallucinated Package Names Mean for
  Your Supply Chain'
date: '2026-04-30'
source: https://dev.to/duriantaco/slopsquatting-in-python-what-205474-hallucinated-package-names-mean-for-your-supply-chain-12oi
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]'
- '[[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]'
- '[[2026-04-17-the-quote-as-ceiling-billing-pattern]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-13-test-your-ai-agent-like-a-senior-engineer-4-patterns-that-work]]'
- '[[2026-04-19-build-your-own-types-classes-explained-simply]]'
status: unread
---

> **TL;DR:** Your AI coding assistant wrote this line: from huggingface_cli import login It looks fine. It looks like something that should exist. You run pip install huggingface-cli , the install succeeds, your tests pass, and you m…

## What’s new and why it matters
Your AI coding assistant wrote this line: from huggingface_cli import login It looks fine. It looks like something that should exist. You run pip install huggingface-cli , the install succeeds, your tests pass, and you merge. In March 2024, that exact package was a proof-of-concept attack by Bar Lanyado at Lasso Security. He'd noticed GPT-based assistants repeatedly recommending huggingface-cli to developers — a package that didn't exist on PyPI. He registered an empty placeholder package under that name and waited. Three months later, it had been downloaded over 30,000 times. An Alibaba resea…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/duriantaco/slopsquatting-in-python-what-205474-hallucinated-package-names-mean-for-your-supply-chain-12oi

## Related notes
- [[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]
- [[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]
- [[2026-04-17-the-quote-as-ceiling-billing-pattern]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-13-test-your-ai-agent-like-a-senior-engineer-4-patterns-that-work]]
- [[2026-04-19-build-your-own-types-classes-explained-simply]]
