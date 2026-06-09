---
title: 'QN : Ingest and transform data in a lakehouse'
date: '2026-06-09'
source: https://dev.to/pauletart/ingest-and-transform-data-in-a-lakehouse-2kcf
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tableau'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-03-how-to-publish-a-power-bi-report-and-embed-it-into-a-website-a-complete-step-by-step-guide]]'
- '[[2026-03-16-from-sql-to-power-bi-for-analysis]]'
- '[[2026-04-06-connecting-power-bi-to-sql-databases-a-complete-guide]]'
- '[[2026-03-09-connecting-power-bi-to-sql-databases-a-step-by-step-guide]]'
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
status: unread
---

> **TL;DR:** lakehouse has two storage areas ; Files and Tables Files Store structured, queryable data by sql Supports schema definitions and ACID transactions Tables Stores Raw or semi-structured data(CSV, parquet, JSON) No schema s…

## What’s new and why it matters
lakehouse has two storage areas ; Files and Tables Files Store structured, queryable data by sql Supports schema definitions and ACID transactions Tables Stores Raw or semi-structured data(CSV, parquet, JSON) No schema support Flexible for data explorations Schema allows for logical ordering of data on business functions or domain (sales,marketing etc) A dbo schema is enabled by default once a lakehouse is created Schema-enabled lakehouses also support schema-level permissions and cross-workspace queries using the four-part namespace Lakehouse mode : Lakehouse Explorer and SQL analytics endpoi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/pauletart/ingest-and-transform-data-in-a-lakehouse-2kcf

## Related notes
- [[2026-04-03-how-to-publish-a-power-bi-report-and-embed-it-into-a-website-a-complete-step-by-step-guide]]
- [[2026-03-16-from-sql-to-power-bi-for-analysis]]
- [[2026-04-06-connecting-power-bi-to-sql-databases-a-complete-guide]]
- [[2026-03-09-connecting-power-bi-to-sql-databases-a-step-by-step-guide]]
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
