---
title: Keep planned and reported outcomes apart in a paper extract
date: '2026-11-22'
source: https://dev.to/nanchuangresearch/keep-planned-and-reported-outcomes-apart-in-a-paper-extract-3l7l
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
related:
- '[[2026-08-20-beyond-sql-accuracy-building-evidence-chains-for-ai-data-agents]]'
- '[[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]'
- '[[2026-04-10-using-llms-with-patient-data-de-identifying-clinical-text-before-api-calls]]'
- '[[2026-09-21-build-bilingual-document-search-with-devup-ai-embeddings-reranking-and-answers-with-sources]]'
- '[[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]'
- '[[2026-09-24-should-you-pay-rs-50000-to-1-lakh-for-a-sql-course-when-free-is-available]]'
status: unread
---

> **TL;DR:** A clinical evidence-table importer should not replace a protocol outcome with the paper's outcome just because both are labelled “symptom score”. Keep both source-linked entries for review. This small Python example flag…

## What’s new and why it matters
A clinical evidence-table importer should not replace a protocol outcome with the paper's outcome just because both are labelled “symptom score”. Keep both source-linked entries for review. This small Python example flags literal differences in endpoint, time point and analysis metric. A missing protocol is a separate state. The numbers and source names below are synthetic teaching material; this code does not judge a real trial. FIELDS = ( "endpoint" , "timepoint" , "metric" ) def audit ( row ) : if not isinstance ( row , dict ) : raise ValueError ( "a record is required" ) reported = row . g…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/nanchuangresearch/keep-planned-and-reported-outcomes-apart-in-a-paper-extract-3l7l

## Related notes
- [[2026-08-20-beyond-sql-accuracy-building-evidence-chains-for-ai-data-agents]]
- [[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]
- [[2026-04-10-using-llms-with-patient-data-de-identifying-clinical-text-before-api-calls]]
- [[2026-09-21-build-bilingual-document-search-with-devup-ai-embeddings-reranking-and-answers-with-sources]]
- [[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]
- [[2026-09-24-should-you-pay-rs-50000-to-1-lakh-for-a-sql-course-when-free-is-available]]
