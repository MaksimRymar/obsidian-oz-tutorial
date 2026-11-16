---
title: How do I build a dataset of ChatGPT answers for research?
date: '2026-11-16'
source: https://dev.to/cloro/how-do-i-build-a-dataset-of-chatgpt-answers-for-research-5c47
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]'
- '[[2026-09-05-enforcing-data-invariants-in-odoo-model-constraints-migrations-and-tests-that-actually-cover-the-fix]]'
- '[[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-11-03-etsy-competitor-analysis-without-a-monthly-tool-what-40-pet-portrait-listings-showed-me]]'
- '[[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]'
status: unread
---

> **TL;DR:** Freeze a prompt set and a list of countries, collect every prompt several times in each country from ChatGPT's web interface, and store the raw JSON, the rendered HTML, the timestamp and the model ChatGPT used with every…

## What’s new and why it matters
Freeze a prompt set and a list of countries, collect every prompt several times in each country from ChatGPT's web interface, and store the raw JSON, the rendered HTML, the timestamp and the model ChatGPT used with every answer. A single answer per prompt is a sample of one from a system that changes between runs and between weeks. The model under your dataset changes. In our own monitoring of a fixed prompt set, gpt-5-6 produced 92% to 99.8% of ChatGPT answers each week in September. From the week of 12 October, gpt-6 produced 86% to 97%. The model field is how we saw the switch. Part of the…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/cloro/how-do-i-build-a-dataset-of-chatgpt-answers-for-research-5c47

## Related notes
- [[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]
- [[2026-09-05-enforcing-data-invariants-in-odoo-model-constraints-migrations-and-tests-that-actually-cover-the-fix]]
- [[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-11-03-etsy-competitor-analysis-without-a-monthly-tool-what-40-pet-portrait-listings-showed-me]]
- [[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]
