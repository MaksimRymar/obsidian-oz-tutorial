---
title: Merging job postings from ten ATS platforms into one schema, and the four fields
  that fight back
date: '2026-08-08'
source: https://dev.to/glitchbound/merging-job-postings-from-ten-ats-platforms-into-one-schema-and-the-four-fields-that-fight-back-1g72
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-24-long-running-sql-queries-a-sample-exploration]]'
- '[[2026-07-02-dont-use-not-in]]'
- '[[2026-07-27-i-tested-42-large-employers-to-see-which-ones-you-can-actually-scrape-only-7-worked]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
status: unread
---

> **TL;DR:** Reading one ATS job board API is easy. Every one of them is public JSON with no key. Reading ten and getting rows you can actually query together is a different job, and it is almost entirely about four fields. I run an…

## What’s new and why it matters
Reading one ATS job board API is easy. Every one of them is public JSON with no key. Reading ten and getting rows you can actually query together is a different job, and it is almost entirely about four fields. I run an index across Greenhouse, Ashby, Workable, Workday, BambooHR, Breezy, Teamtailor, Personio, Recruitee and Rippling. Here is what actually broke, with the measurements. 1. Remote is not a boolean, and one API will lie to you about it Ashby postings carry isRemote . It looks like exactly the field you want. Measured on Ramp's board, 1 August 2026: isRemote was true for 117 of 126…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/glitchbound/merging-job-postings-from-ten-ats-platforms-into-one-schema-and-the-four-fields-that-fight-back-1g72

## Related notes
- [[2026-07-24-long-running-sql-queries-a-sample-exploration]]
- [[2026-07-02-dont-use-not-in]]
- [[2026-07-27-i-tested-42-large-employers-to-see-which-ones-you-can-actually-scrape-only-7-worked]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
