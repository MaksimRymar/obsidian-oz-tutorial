---
title: Coding Cat Oran S2 Ep5 — The Many-to-Many Disaster
date: '2026-05-15'
source: https://dev.to/syslayer/coding-cat-oran-s2-ep5-the-many-to-many-disaster-22jo
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#support-analytics'
related:
- '[[2026-05-15-coding-cat-oran-s2-ep6-the-abstract-table-and-the-gateway]]'
- '[[2026-05-10-coding-cat-oran-s2-ep1-the-excel-republic]]'
- '[[2026-05-10-coding-cat-oran-s2-ep2-the-big-customer]]'
- '[[2026-05-07-how-databricks-genie-turns-plain-english-into-sql-code]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-04-21-i-build-custom-trading-bots-for-deriv-and-mt4mt5-heres-what-that-actually-looks-like]]'
status: unread
---

> **TL;DR:** The report table is agreed. No one is responsible for it. This is a different problem. The table looked clean on the whiteboard. Seventeen columns. One row per batch. Every department's data, agreed, signed, version-numb…

## What’s new and why it matters
The report table is agreed. No one is responsible for it. This is a different problem. The table looked clean on the whiteboard. Seventeen columns. One row per batch. Every department's data, agreed, signed, version-numbered. Oran had been looking at it for three days. He had a document called Problems with this table. It had eleven items in it now. He was still finding more. Problem 1: One batch, many inspections. QA inspects at three stages: incoming material, in-process, and final. Each stage produces a separate inspection record. Each record has its own result, its own inspector, its own t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/syslayer/coding-cat-oran-s2-ep5-the-many-to-many-disaster-22jo

## Related notes
- [[2026-05-15-coding-cat-oran-s2-ep6-the-abstract-table-and-the-gateway]]
- [[2026-05-10-coding-cat-oran-s2-ep1-the-excel-republic]]
- [[2026-05-10-coding-cat-oran-s2-ep2-the-big-customer]]
- [[2026-05-07-how-databricks-genie-turns-plain-english-into-sql-code]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-04-21-i-build-custom-trading-bots-for-deriv-and-mt4mt5-heres-what-that-actually-looks-like]]
