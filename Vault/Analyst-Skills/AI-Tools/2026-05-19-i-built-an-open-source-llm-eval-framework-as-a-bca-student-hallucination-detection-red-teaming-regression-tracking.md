---
title: I built an open-source LLM eval framework as a BCA student — hallucination
  detection, red-teaming, regression tracking
date: '2026-05-19'
source: https://dev.to/ayushkhatidev/i-built-an-open-source-llm-eval-framework-as-a-bca-student-hallucination-detection-red-teaming-5hj5
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]'
- '[[2026-04-08-i-built-a-bot-that-answers-github-discussions-using-free-ai-models-heres-what-i-learned]]'
- '[[2026-05-10-i-built-a-self-updating-seo-brain-inspired-by-andrej-karpathys-llm-wiki]]'
- '[[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]'
- '[[2026-03-14-the-ai-engineering-stack-in-2026-what-to-learn-first]]'
- '[[2026-04-11-how-i-built-a-defi-yield-dashboard-in-50-lines-of-python]]'
status: unread
---

> **TL;DR:** ## The Problem Every company building AI products needs to know if their LLM is actually working — or getting worse over time. This is harder than it sounds. I built an open-source evaluation framework to solve this. Wha…

## What’s new and why it matters
## The Problem Every company building AI products needs to know if their LLM is actually working — or getting worse over time. This is harder than it sounds. I built an open-source evaluation framework to solve this. What It Does Runs a 27-test suite covering factual accuracy, safety refusals, hallucination resistance, adversarial prompts, and reasoning Scores outputs using a 3-tier judge chain: semantic similarity → LLM judge → regex fallback Auto-generates adversarial prompt attacks to red-team any endpoint Tracks regressions across model versions Live dashboard with pass/fail rates and per-…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ayushkhatidev/i-built-an-open-source-llm-eval-framework-as-a-bca-student-hallucination-detection-red-teaming-5hj5

## Related notes
- [[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]
- [[2026-04-08-i-built-a-bot-that-answers-github-discussions-using-free-ai-models-heres-what-i-learned]]
- [[2026-05-10-i-built-a-self-updating-seo-brain-inspired-by-andrej-karpathys-llm-wiki]]
- [[2026-03-01-building-multi-model-ai-agents-with-openai-ollama-groq-and-gemini]]
- [[2026-03-14-the-ai-engineering-stack-in-2026-what-to-learn-first]]
- [[2026-04-11-how-i-built-a-defi-yield-dashboard-in-50-lines-of-python]]
