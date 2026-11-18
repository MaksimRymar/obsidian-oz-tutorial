---
title: 'Your Prompt Change Needs a Number: A Zero-Cost LLM Eval Gate in Pure Python'
date: '2026-11-18'
source: https://dev.to/yuya_ai_lab/your-prompt-change-needs-a-number-a-zero-cost-llm-eval-gate-in-pure-python-1bk4
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-10-26-how-to-check-your-ais-data-answers-evals-for-each-stage]]'
- '[[2026-11-18-two-hallucination-tests-you-can-run-before-you-pay-for-a-judge-model]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** For a few weeks I improved my prompts the way most people do: I changed a sentence, ran three examples I liked, and decided it was better. Then one "harmless" wording tweak quietly broke JSON extraction in a nightly auto…

## What’s new and why it matters
For a few weeks I improved my prompts the way most people do: I changed a sentence, ran three examples I liked, and decided it was better. Then one "harmless" wording tweak quietly broke JSON extraction in a nightly automation. It ran for three days against a slightly renamed key before I noticed anything was wrong — not through an alert, but by scrolling a log for an unrelated reason. That is the whole argument for this post. A prompt edit is a code change, and you cannot review a code change by feeling. You need a number that goes up or down, and you need the build to stop when the number go…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yuya_ai_lab/your-prompt-change-needs-a-number-a-zero-cost-llm-eval-gate-in-pure-python-1bk4

## Related notes
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-10-26-how-to-check-your-ais-data-answers-evals-for-each-stage]]
- [[2026-11-18-two-hallucination-tests-you-can-run-before-you-pay-for-a-judge-model]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
