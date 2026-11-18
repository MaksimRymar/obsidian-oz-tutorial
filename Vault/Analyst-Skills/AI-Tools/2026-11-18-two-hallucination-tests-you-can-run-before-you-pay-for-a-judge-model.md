---
title: Two Hallucination Tests You Can Run Before You Pay for a Judge Model
date: '2026-11-18'
source: https://dev.to/zain_qa_automation/two-hallucination-tests-you-can-run-before-you-pay-for-a-judge-model-70
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]'
- '[[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]'
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]'
status: unread
---

> **TL;DR:** Most hallucination testing guides start with "install DeepEval, set your OpenAI key, pick a threshold." That is a fine place to end up. It is a poor place to start, because on day one you do not yet know what kind of wro…

## What’s new and why it matters
Most hallucination testing guides start with "install DeepEval, set your OpenAI key, pick a threshold." That is a fine place to end up. It is a poor place to start, because on day one you do not yet know what kind of wrong answers your app gives, and every judge call costs money. So this post goes the other way round. Below are two checks that need no API key and no judge model: a grounding check for numbers and a self-consistency check. Both are plain Python and pytest. I ran them before writing this (Python 3.13, pytest 9.2.0): 4 passed. They will not catch every hallucination. They will cat…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/zain_qa_automation/two-hallucination-tests-you-can-run-before-you-pay-for-a-judge-model-70

## Related notes
- [[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]
- [[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]
