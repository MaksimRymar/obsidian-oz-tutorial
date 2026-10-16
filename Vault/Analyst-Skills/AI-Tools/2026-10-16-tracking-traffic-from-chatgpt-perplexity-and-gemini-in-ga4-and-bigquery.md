---
title: Tracking Traffic From ChatGPT, Perplexity and Gemini in GA4 and BigQuery
date: '2026-10-16'
source: https://dev.to/furqank729/tracking-traffic-from-chatgpt-perplexity-and-gemini-in-ga4-and-bigquery-4nd2
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-10-12-why-does-ai-cite-their-page-and-not-yours-diff-them-with-a-script]]'
- '[[2026-10-12-where-vs-having-in-sql-a-simple-way-to-understand-the-difference]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** AI visibility metrics tell you how often assistants mention and cite you. Sooner or later someone asks the follow-up: does any of that turn into traffic? Part of the answer is already in your analytics, mixed into "Refer…

## What’s new and why it matters
AI visibility metrics tell you how often assistants mention and cite you. Sooner or later someone asks the follow-up: does any of that turn into traffic? Part of the answer is already in your analytics, mixed into "Referral" alongside every other website. This post separates it out: a custom channel group in GA4 for AI assistants, a BigQuery query over the GA4 export that pulls AI-referred sessions and landing pages, a join against citation data to compare "cited" with "clicked". It also covers the large share of AI-influenced traffic you can't see this way, because that limitation should shap…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/furqank729/tracking-traffic-from-chatgpt-perplexity-and-gemini-in-ga4-and-bigquery-4nd2

## Related notes
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-10-12-why-does-ai-cite-their-page-and-not-yours-diff-them-with-a-script]]
- [[2026-10-12-where-vs-having-in-sql-a-simple-way-to-understand-the-difference]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
