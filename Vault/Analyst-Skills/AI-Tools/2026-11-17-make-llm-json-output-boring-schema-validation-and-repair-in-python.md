---
title: 'Make LLM JSON Output Boring: Schema Validation and Repair in Python'
date: '2026-11-17'
source: https://dev.to/tamer_kalla/make-llm-json-output-boring-schema-validation-and-repair-in-python-86
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-11-08-48-hour-field-notes-same-prompt-two-json-shapes-and-a-validator-that-passed-both]]'
- '[[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-10-24-a-budget-guard-for-llm-agents-in-40-lines-of-python-written-by-an-agent-that-dies-at-0]]'
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]'
status: unread
---

> **TL;DR:** The problem Every LLM feature I have shipped that returns JSON has failed in the same unglamorous ways. The model wraps the object in markdown fences even though the prompt said not to. It leaves a trailing comma after t…

## What’s new and why it matters
The problem Every LLM feature I have shipped that returns JSON has failed in the same unglamorous ways. The model wraps the object in markdown fences even though the prompt said not to. It leaves a trailing comma after the last field. It writes strings with single quotes, Python-style. It invents an enum value ("urgent", when the allowed set is low, medium, high) or returns a confidence of 1.4 on a zero-to-one scale. Then json.loads throws, or worse, nothing throws and a bad value flows downstream. None of this is exotic, and none of it is really a model problem. It is a trust problem. Raw mod…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tamer_kalla/make-llm-json-output-boring-schema-validation-and-repair-in-python-86

## Related notes
- [[2026-11-08-48-hour-field-notes-same-prompt-two-json-shapes-and-a-validator-that-passed-both]]
- [[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-10-24-a-budget-guard-for-llm-agents-in-40-lines-of-python-written-by-an-agent-that-dies-at-0]]
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]
