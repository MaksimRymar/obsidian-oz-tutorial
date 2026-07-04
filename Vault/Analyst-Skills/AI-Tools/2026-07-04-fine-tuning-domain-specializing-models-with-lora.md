---
title: Fine-tuning — Domain-Specializing Models with LoRA
date: '2026-07-04'
source: https://dev.to/hiroki-kameyama/fine-tuning-domain-specializing-models-with-lora-180g
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-03-08-data-engineers-what-if-your-bigquery-function-could-return-multiple-tables]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
- '[[2026-04-07-how-to-deploy-nexusquant-in-production-and-whats-missing]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]'
- '[[2026-02-22-how-to-generate-business-leads-using-google-maps-ids-and-python]]'
status: unread
---

> **TL;DR:** Introduction In Chapter 5 (MLOps) , we built a CI/CD pipeline. This chapter explores a different approach: fine-tuning — training the model itself on your own data. [RAG] Question → search DB → pass results to LLM → answ…

## What’s new and why it matters
Introduction In Chapter 5 (MLOps) , we built a CI/CD pipeline. This chapter explores a different approach: fine-tuning — training the model itself on your own data. [RAG] Question → search DB → pass results to LLM → answer → Requires documents, search costs apply [Fine-tuning] Question → Fine-tuned LLM → answer → Model carries the knowledge itself — no retrieval needed When to Use RAG vs Fine-tuning RAG Fine-tuning Best for Latest info, internal document search Specific styles, formats, specialized vocabulary Knowledge updates Just add documents Requires retraining Cost API cost + DB cost Trai…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hiroki-kameyama/fine-tuning-domain-specializing-models-with-lora-180g

## Related notes
- [[2026-03-08-data-engineers-what-if-your-bigquery-function-could-return-multiple-tables]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
- [[2026-04-07-how-to-deploy-nexusquant-in-production-and-whats-missing]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]
- [[2026-02-22-how-to-generate-business-leads-using-google-maps-ids-and-python]]
