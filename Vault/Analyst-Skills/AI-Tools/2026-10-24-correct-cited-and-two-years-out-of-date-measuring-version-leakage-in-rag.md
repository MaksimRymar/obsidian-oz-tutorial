---
title: 'Correct, Cited, and Two Years Out of Date: Measuring Version Leakage in RAG'
date: '2026-10-24'
source: https://dev.to/raihan-js/correct-cited-and-two-years-out-of-date-measuring-version-leakage-in-rag-5cdk
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-06-10-i-built-a-production-rag-system-on-my-m1-mac-for-0]]'
- '[[2026-09-18-how-to-build-a-rag-system-from-scratch-in-python-chunk-embed-retrieve-cite-httpsaistudybydoingin]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-08-notebooks-for-llm-work-without-the-usual-mess]]'
- '[[2026-02-24-rag-from-scratch-build-a-system-that-answers-questions-from-your-docs]]'
- '[[2026-09-27-i-built-a-registry-for-system-one-models-heres-what-i-learned-comparing-all-of-them]]'
status: unread
---

> **TL;DR:** I built RAG over nine yearly revisions of federal acquisition regulations and asked it questions "as of" specific dates. Plain RAG answers from the wrong version 80% of the time — fluently, with citations. Date handling…

## What’s new and why it matters
I built RAG over nine yearly revisions of federal acquisition regulations and asked it questions "as of" specific dates. Plain RAG answers from the wrong version 80% of the time — fluently, with citations. Date handling fixes it without hurting recall. Scope note, first paragraph as promised: FAR/DFARS only, year-granularity revisions (2017–2025), US public-domain text, one 1.8B local generator, greedy decoding, no LLM judge (containment is string matching). NOT legal advice — a measurement study, not counsel. The problem nobody benchmarks Regulations change. The micro-purchase threshold moves…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/raihan-js/correct-cited-and-two-years-out-of-date-measuring-version-leakage-in-rag-5cdk

## Related notes
- [[2026-06-10-i-built-a-production-rag-system-on-my-m1-mac-for-0]]
- [[2026-09-18-how-to-build-a-rag-system-from-scratch-in-python-chunk-embed-retrieve-cite-httpsaistudybydoingin]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-08-notebooks-for-llm-work-without-the-usual-mess]]
- [[2026-02-24-rag-from-scratch-build-a-system-that-answers-questions-from-your-docs]]
- [[2026-09-27-i-built-a-registry-for-system-one-models-heres-what-i-learned-comparing-all-of-them]]
