---
title: Ten of our tests changed what their score means, and the cut-over is a metric
  key rather than a date
date: '2026-11-22'
source: https://dev.to/daniel_pertu/ten-of-our-tests-changed-what-their-score-means-and-the-cut-over-is-a-metric-key-rather-than-a-date-223j
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]'
- '[[2026-09-21-percentilecont-a-20000-row-window-and-the-difference-between-skipped-and-failed]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-10-17-i-added-a-fourth-shard-in-python-and-75-of-the-keys-moved]]'
- '[[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]'
status: unread
---

> **TL;DR:** CogniPrep has 491 practice tests across 77 assessment providers. Every one of them ends with a percentile, and that percentile is not invented per sitting: a nightly job aggregates the recent scores for each test and sto…

## What’s new and why it matters
CogniPrep has 491 practice tests across 77 assessment providers. Every one of them ends with a percentile, and that percentile is not invented per sitting: a nightly job aggregates the recent scores for each test and stores a mean, a median, a standard deviation and nine percentile cut points. The scoring code then reads that row. Last weekend we rebuilt ten of those tests to match the real instruments more closely. Different mechanics, different clocks, in four cases a different answer format. And with that, raw_score stopped meaning what it used to mean. Several of them had been storing some…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/daniel_pertu/ten-of-our-tests-changed-what-their-score-means-and-the-cut-over-is-a-metric-key-rather-than-a-date-223j

## Related notes
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]
- [[2026-09-21-percentilecont-a-20000-row-window-and-the-difference-between-skipped-and-failed]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-10-17-i-added-a-fourth-shard-in-python-and-75-of-the-keys-moved]]
- [[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]
