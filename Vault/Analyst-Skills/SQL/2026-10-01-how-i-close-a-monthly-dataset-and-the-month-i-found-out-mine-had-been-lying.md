---
title: How I close a monthly dataset, and the month I found out mine had been lying
date: '2026-10-01'
source: https://dev.to/juanauriti/how-i-close-a-monthly-dataset-and-the-month-i-found-out-mine-had-been-lying-168m
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-24-my-alert-fired-7-times-across-1963-pairs-i-assumed-the-thresholds-were-too-high-they-were-and-it-didnt-matter]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-05-28-before-sql-we-had-to-tell-computers-everything-then-one-idea-changed-that-forever]]'
- '[[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
status: unread
---

> **TL;DR:** I publish a monthly report from my own audit data. First of the month, one edition, findings only from the window that just closed. The rules that make it publishable are almost entirely rules about what gets thrown out…

## What’s new and why it matters
I publish a monthly report from my own audit data. First of the month, one edition, findings only from the window that just closed. The rules that make it publishable are almost entirely rules about what gets thrown out . I learned most of them the expensive way, and one of them by discovering that a number I had already published was computed from a table where the majority of rows were an artifact of a bug. The rule that came first No numerical findings before the data exists. That sounds too obvious to write down. It isn't, because the pressure runs the other way: you have a publication slo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/juanauriti/how-i-close-a-monthly-dataset-and-the-month-i-found-out-mine-had-been-lying-168m

## Related notes
- [[2026-09-24-my-alert-fired-7-times-across-1963-pairs-i-assumed-the-thresholds-were-too-high-they-were-and-it-didnt-matter]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-05-28-before-sql-we-had-to-tell-computers-everything-then-one-idea-changed-that-forever]]
- [[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
