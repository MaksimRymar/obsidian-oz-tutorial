---
title: 'The Small-Files Problem: Compaction, OPTIMIZE & File-Sizing Across Engines'
date: '2026-08-15'
source: https://dev.to/gowthampotureddi/the-small-files-problem-compaction-optimize-file-sizing-across-engines-2dd5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tableau'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-06-29-bigquery-partitioning-clustering-cost-performance-tuning-playbook]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
status: unread
---

> **TL;DR:** The small files problem is the quiet tax every data lake pays as it grows: a table that should live in a few hundred right-sized files instead sprawls across hundreds of thousands of tiny ones, and every query, every lis…

## What’s new and why it matters
The small files problem is the quiet tax every data lake pays as it grows: a table that should live in a few hundred right-sized files instead sprawls across hundreds of thousands of tiny ones, and every query, every listing, and every planning step slows down in proportion to the file count rather than the data size . It is the single most common reason a pipeline that was fast at 10 GB crawls at 10 TB even though the hardware never changed — the bytes barely grew, but the number of objects exploded, and distributed engines are exquisitely sensitive to the number of things they have to track,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/the-small-files-problem-compaction-optimize-file-sizing-across-engines-2dd5

## Related notes
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-06-29-bigquery-partitioning-clustering-cost-performance-tuning-playbook]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
