---
title: 'GLiNER2 vs an LLM: I tested both on 640 labelled examples'
date: '2026-11-02'
source: https://dev.to/ahmad_dogar_7d098f5e48f72/gliner2-vs-an-llm-i-tested-both-on-640-labelled-examples-1998
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]'
- '[[2026-11-01-getting-only-the-new-dois-from-the-crossref-api-every-day-dates-cursors-and-rate-limits]]'
- '[[2026-09-07-bloom-filters-for-data-engineers-cheap-membership-tests]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** My comparison of LLMs, Jev and CDMs was all reading: docs, papers and vendor numbers. It left me wanting something I could run myself. GLiNER2 is that thing. It is an Apache-2.0 extraction model from Fastino that runs on…

## What’s new and why it matters
My comparison of LLMs, Jev and CDMs was all reading: docs, papers and vendor numbers. It left me wanting something I could run myself. GLiNER2 is that thing. It is an Apache-2.0 extraction model from Fastino that runs on a CPU, and you give it a schema, not a prompt. So I ran it on this laptop against Claude Haiku 5.5, with 640 labelled examples. I could not find an independent head-to-head for JSON extraction, which is the part I care about most. The short version: GLiNER2 is very fast and fine when the answer is written plainly in the text. Haiku was more accurate on every test but one, and…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ahmad_dogar_7d098f5e48f72/gliner2-vs-an-llm-i-tested-both-on-640-labelled-examples-1998

## Related notes
- [[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]
- [[2026-11-01-getting-only-the-new-dois-from-the-crossref-api-every-day-dates-cursors-and-rate-limits]]
- [[2026-09-07-bloom-filters-for-data-engineers-cheap-membership-tests]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
