---
title: Which TV IDs came back? A SQL check inspired by Mayfly
date: '2026-11-24'
source: https://dev.to/aleksuix/which-tv-ids-came-back-a-sql-check-inspired-by-mayfly-1pen
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-09-20-window-functions-vs-aggregate-functions-in-sql-a-beginner-friendly-guide]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-11-18-google-maps-rank-tracker-check-your-google-maps-ranking-from-every-street-around-you]]'
status: unread
---

> **TL;DR:** If a streaming campaign tells me it reached a record number of new TVs, I want to see yesterday's IDs. In Pixalate's Mayfly investigation, more than 60% of the home IP addresses in the flagged traffic returned the next d…

## What’s new and why it matters
If a streaming campaign tells me it reached a record number of new TVs, I want to see yesterday's IDs. In Pixalate's Mayfly investigation, more than 60% of the home IP addresses in the flagged traffic returned the next day. The reported next-day return rate for flagged device IDs was 0%. Pixalate used turnover to select suspicious traffic, so reproducing a low return rate gives me a lead to investigate. It doesn't establish fraud on its own. Pixalate's investigation Count devices that had a chance to return Suppose six distinct address and device-ID pairs appear on Saturday. Two belong to addr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aleksuix/which-tv-ids-came-back-a-sql-check-inspired-by-mayfly-1pen

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-09-20-window-functions-vs-aggregate-functions-in-sql-a-beginner-friendly-guide]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-11-18-google-maps-rank-tracker-check-your-google-maps-ranking-from-every-street-around-you]]
