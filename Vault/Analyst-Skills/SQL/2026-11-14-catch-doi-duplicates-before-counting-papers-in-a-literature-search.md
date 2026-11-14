---
title: Catch DOI duplicates before counting papers in a literature search
date: '2026-11-14'
source: https://dev.to/nanchuangresearch/catch-doi-duplicates-before-counting-papers-in-a-literature-search-33ah
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-09-create-a-serp-diff-table-for-titles-urls-and-positions]]'
- '[[2026-11-11-catch-unexpected-missing-value-codes-in-a-research-csv]]'
- '[[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]'
- '[[2026-09-21-build-bilingual-document-search-with-devup-ai-embeddings-reranking-and-answers-with-sources]]'
- '[[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]'
- '[[2026-10-26-how-to-check-your-ais-data-answers-evals-for-each-stage]]'
status: unread
---

> **TL;DR:** The same paper can arrive from one database as a bare DOI and from another as a resolver URL. Normalize the DOI before grouping those rows, and preserve the search source in the resulting record. For citations whose DOI…

## What’s new and why it matters
The same paper can arrive from one database as a bare DOI and from another as a resolver URL. Normalize the DOI before grouping those rows, and preserve the search source in the resulting record. For citations whose DOI is missing, keep the original rows for inspection. This synthetic Python example handles DOI URLs, bare DOI strings, and empty values. It removes an initial resolver prefix and uses case-insensitive comparison. import re records = [ ( "Index A" , "https://doi.org/10.5555/example.12" ) , ( "Index B" , "10.5555/EXAMPLE.12" ) , ( "Index B" , "" ) , ] by_doi = { } manual = [ ] for…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/nanchuangresearch/catch-doi-duplicates-before-counting-papers-in-a-literature-search-33ah

## Related notes
- [[2026-07-09-create-a-serp-diff-table-for-titles-urls-and-positions]]
- [[2026-11-11-catch-unexpected-missing-value-codes-in-a-research-csv]]
- [[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]
- [[2026-09-21-build-bilingual-document-search-with-devup-ai-embeddings-reranking-and-answers-with-sources]]
- [[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]
- [[2026-10-26-how-to-check-your-ais-data-answers-evals-for-each-stage]]
