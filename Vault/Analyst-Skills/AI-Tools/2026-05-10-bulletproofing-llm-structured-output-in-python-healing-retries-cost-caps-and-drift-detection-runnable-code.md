---
title: 'Bulletproofing LLM Structured Output in Python: Healing Retries, Cost Caps,
  and Drift Detection (Runnable Code)'
date: '2026-05-10'
source: https://dev.to/velsof/bulletproofing-llm-structured-output-in-python-healing-retries-cost-caps-and-drift-detection-c89
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-19-ai-agents-explained-simply-the-biggest-tech-shift-of-2026]]'
status: unread
---

> **TL;DR:** I shipped a structured-output endpoint to production in March. The schema was clean, JSON mode was on, the model was GPT-4.1, the eval suite was green. Three weeks in, the on-call channel lit up because a downstream bill…

## What’s new and why it matters
I shipped a structured-output endpoint to production in March. The schema was clean, JSON mode was on, the model was GPT-4.1, the eval suite was green. Three weeks in, the on-call channel lit up because a downstream billing job had silently skipped 4,200 records over a weekend. The output was valid JSON. It just wasn't the JSON we asked for. That was my last "JSON mode is good enough" deployment. Since then I've shipped four more LLM structured-output systems and the failures keep coming from the same places — and JSON mode catches roughly two of them. This post is the toolkit I wish I had on…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/velsof/bulletproofing-llm-structured-output-in-python-healing-retries-cost-caps-and-drift-detection-c89

## Related notes
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-19-ai-agents-explained-simply-the-biggest-tech-shift-of-2026]]
