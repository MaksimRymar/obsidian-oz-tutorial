---
title: 'Your RAG Has No Idea What Year It Is: A Frozen Benchmark for Version Leakage'
date: '2026-10-25'
source: https://dev.to/raihan-js/your-rag-has-no-idea-what-year-it-is-a-frozen-benchmark-for-version-leakage-1kf9
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-10-24-correct-cited-and-two-years-out-of-date-measuring-version-leakage-in-rag]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-09-03-ranking-a-two-dimensional-catalog-with-one-sql-expression]]'
- '[[2026-08-30-sqlmesh-vs-dbt-virtual-data-environments-column-level-lineage-blue-green-deploys]]'
- '[[2026-08-27-partitioning-clustering-and-bi-engine-measuring-what-each-one-saves-in-bigquery]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
status: unread
---

> **TL;DR:** I froze nine yearly revisions of federal acquisition regulations into one corpus, asked 700 questions "as of" specific dates, and watched plain hybrid RAG answer from the wrong year 80% of the time. Date handling fixes i…

## What’s new and why it matters
I froze nine yearly revisions of federal acquisition regulations into one corpus, asked 700 questions "as of" specific dates, and watched plain hybrid RAG answer from the wrong year 80% of the time. Date handling fixes it — with one honest failure mode. Scope note, first paragraph as promised: FAR/DFARS Title 48 only, year-granularity revisions 2017–2025, US public-domain text, bge-m3 + BM25 retrieval, rule-based scoring, no LLM judge, no generator trained yet. NOT legal advice — a measurement study, not counsel. Timeless corpus, wrong answers Regulations change. Between 2017 and 2025, about 9…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/raihan-js/your-rag-has-no-idea-what-year-it-is-a-frozen-benchmark-for-version-leakage-1kf9

## Related notes
- [[2026-10-24-correct-cited-and-two-years-out-of-date-measuring-version-leakage-in-rag]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-09-03-ranking-a-two-dimensional-catalog-with-one-sql-expression]]
- [[2026-08-30-sqlmesh-vs-dbt-virtual-data-environments-column-level-lineage-blue-green-deploys]]
- [[2026-08-27-partitioning-clustering-and-bi-engine-measuring-what-each-one-saves-in-bigquery]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
