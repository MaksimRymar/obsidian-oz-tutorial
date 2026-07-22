---
title: We Pushed One Postgres Box to 2 Million Writes/Sec. The Disk Lied to Us.
date: '2026-07-22'
source: https://medium.com/@speed_enginner/we-pushed-one-postgres-box-to-2-million-writes-sec-the-disk-lied-to-us-3cb7ac026145?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-07-12-why-were-my-pbi-visuals-taking-60-seconds-to-render-a-dax-formula-engine-deep-dive]]'
- '[[2026-06-09-why-a-single-where-clause-can-make-a-query-1000x-slower]]'
- '[[2026-03-31-the-data-quality-check-that-fits-in-one-line]]'
- '[[2026-05-12-part-2-memory-store-on-disk-ddl-dml-and-the-catalog-tree]]'
- '[[2026-07-12-why-were-my-pbi-visuals-taking-60-seconds-to-render-a-dax-formula-engine-deep-dive]]'
- '[[2026-03-11-from-disliking-calculations-to-using-power-bi]]'
status: unread
---

> **TL;DR:** Two million a second was real. Durable? Not one row from the last few seconds survived a power cut, and a single config line was why. Continue reading on Medium »

## What’s new and why it matters
Two million a second was real. Durable? Not one row from the last few seconds survived a power cut, and a single config line was why. Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/@speed_enginner/we-pushed-one-postgres-box-to-2-million-writes-sec-the-disk-lied-to-us-3cb7ac026145?source=rss------sql-5

## Related notes
- [[2026-07-12-why-were-my-pbi-visuals-taking-60-seconds-to-render-a-dax-formula-engine-deep-dive]]
- [[2026-06-09-why-a-single-where-clause-can-make-a-query-1000x-slower]]
- [[2026-03-31-the-data-quality-check-that-fits-in-one-line]]
- [[2026-05-12-part-2-memory-store-on-disk-ddl-dml-and-the-catalog-tree]]
- [[2026-07-12-why-were-my-pbi-visuals-taking-60-seconds-to-render-a-dax-formula-engine-deep-dive]]
- [[2026-03-11-from-disliking-calculations-to-using-power-bi]]
