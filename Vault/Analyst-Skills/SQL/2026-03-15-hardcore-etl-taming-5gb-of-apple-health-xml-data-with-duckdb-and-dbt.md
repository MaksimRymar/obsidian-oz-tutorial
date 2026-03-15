---
title: 'Hardcore ETL: Taming 5GB+ of Apple Health XML Data with DuckDB and dbt'
date: '2026-03-15'
source: https://dev.to/beck_moulton/hardcore-etl-taming-5gb-of-apple-health-xml-data-with-duckdb-and-dbt-2kfi
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tableau'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-11-listen-to-your-breath-building-an-offline-osa-screener-with-whisper-and-pytorch]]'
- '[[2026-03-01-stop-manually-entering-medical-data-how-to-automate-pdf-lab-reports-with-layoutparser-ocr]]'
- '[[2026-03-08-vectorizing-your-vitals-converting-10gb-of-apple-health-data-into-a-personal-rag-brain]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-02-24-detcting-burnout-before-it-hits-building-an-hrv-anomaly-detector-with-isolation-forest]]'
status: unread
---

> **TL;DR:** So, you decided to export your Apple Health data. You expected a neat CSV or a friendly JSON, but instead, you were greeted by a massive, bloated 5GB+ XML file that makes Excel cry and VS Code freeze. In this guide, we a…

## What’s new and why it matters
So, you decided to export your Apple Health data. You expected a neat CSV or a friendly JSON, but instead, you were greeted by a massive, bloated 5GB+ XML file that makes Excel cry and VS Code freeze. In this guide, we are building a high-performance ETL pipeline to transform that chaotic XML into a structured Personal Data Warehouse . We’ll be using the "Modern Data Stack for local machines": DuckDB for lightning-fast processing, dbt for modeling, and Apache Parquet for efficient storage. By the end of this, you'll be performing Data Engineering on your own heartbeat, steps, and sleep pattern…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/beck_moulton/hardcore-etl-taming-5gb-of-apple-health-xml-data-with-duckdb-and-dbt-2kfi

## Related notes
- [[2026-03-11-listen-to-your-breath-building-an-offline-osa-screener-with-whisper-and-pytorch]]
- [[2026-03-01-stop-manually-entering-medical-data-how-to-automate-pdf-lab-reports-with-layoutparser-ocr]]
- [[2026-03-08-vectorizing-your-vitals-converting-10gb-of-apple-health-data-into-a-personal-rag-brain]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-02-24-detcting-burnout-before-it-hits-building-an-hrv-anomaly-detector-with-isolation-forest]]
