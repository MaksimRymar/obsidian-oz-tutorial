---
title: 'Debug Log #1 — The Pipeline That Looked Broken'
date: '2026-05-26'
source: https://dev.to/thompson_jovann_4fae7e88d/debug-log-1-the-pipeline-that-looked-broken-23f8
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-03-19-i-used-ai-to-build-my-project-but-then-i-had-to-actually-understand-it]]'
- '[[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]'
- '[[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]'
- '[[2026-04-22-subqueries-vs-ctes-in-sql-a-practical-guide-for-data-analysts]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]'
status: unread
---

> **TL;DR:** I had been building a local ETL pipeline designed to process long conversational PDFs into structured datasets. The system extracted dialogue, cleaned it, generated QA artifacts, and loaded the results into SQLite for do…

## What’s new and why it matters
I had been building a local ETL pipeline designed to process long conversational PDFs into structured datasets. The system extracted dialogue, cleaned it, generated QA artifacts, and loaded the results into SQLite for downstream analysis. By the time this debugging process started, the core extract-transform-load flow already worked. Data could move end-to-end through the system successfully. The problems started showing up once I added the QA and diagnostics stages around it. During development, parts of those systems seemed to work. But when I came back and reran the full pipeline, execution…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/thompson_jovann_4fae7e88d/debug-log-1-the-pipeline-that-looked-broken-23f8

## Related notes
- [[2026-03-19-i-used-ai-to-build-my-project-but-then-i-had-to-actually-understand-it]]
- [[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]
- [[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]
- [[2026-04-22-subqueries-vs-ctes-in-sql-a-practical-guide-for-data-analysts]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]
