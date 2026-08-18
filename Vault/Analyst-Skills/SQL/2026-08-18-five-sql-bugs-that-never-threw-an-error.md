---
title: Five SQL Bugs That Never Threw an Error
date: '2026-08-18'
source: https://dev.to/kiplangat_brian/five-sql-bugs-that-never-threw-an-error-25nc
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
status: unread
---

> **TL;DR:** A week cleaning 290 booking records taught me more about silent failure than any error message ever has Last week I cleaned a deliberately messy dataset; 290 booking records from Safari Connect, Nairobi bus platform, 21…

## What’s new and why it matters
A week cleaning 290 booking records taught me more about silent failure than any error message ever has Last week I cleaned a deliberately messy dataset; 290 booking records from Safari Connect, Nairobi bus platform, 21 columns, 23 catalogued data problems. Class exercise, but the data was built from real failure modes. The problems I'd been warned about took an afternoon. The ones that cost me were the five that ran perfectly, returned plausible output, and were wrong. Every one of these produced a result. None produced an error. 1. The date heuristic that silently dropped five bookings The d…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kiplangat_brian/five-sql-bugs-that-never-threw-an-error-25nc

## Related notes
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
