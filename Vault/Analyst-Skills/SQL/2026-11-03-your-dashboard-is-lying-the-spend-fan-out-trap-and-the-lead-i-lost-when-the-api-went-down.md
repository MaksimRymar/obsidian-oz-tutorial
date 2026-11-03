---
title: 'Your Dashboard Is Lying: The Spend Fan-Out Trap and the Lead I Lost When the
  API Went Down'
date: '2026-11-03'
source: https://dev.to/emadaed/your-dashboard-is-lying-the-spend-fan-out-trap-and-the-lead-i-lost-when-the-api-went-down-19ci
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tableau'
- '#tool'
related:
- '[[2026-09-28-group-by-aggregate-functions-explained-the-where-vs-having-mistake-almost-everyone-makes]]'
- '[[2026-06-04-summing-platform-roas-overstates-your-ad-results-use-mer-instead-2026]]'
- '[[2026-09-26-why-your-join-doubled-your-totals-theres-no-error-just-the-wrong-number]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
status: unread
---

> **TL;DR:** The Problem That Costs Real Budget Marketing attribution is broken. Not because the math is hard, but because the plumbing is fragile. A CMO looks at a dashboard showing "Cost per Booking: $41" for Meta and "Cost per Boo…

## What’s new and why it matters
The Problem That Costs Real Budget Marketing attribution is broken. Not because the math is hard, but because the plumbing is fragile. A CMO looks at a dashboard showing "Cost per Booking: $41" for Meta and "Cost per Booking: $82" for Google, and shifts budget. But if only 49% of those Meta bookings actually show up for their appointments, the real cost per occurred appointment is $87—barely cheaper than Google's $106 . The gap between "booking" and "showing up" is where money disappears. I built a synthetic-data pipeline to trace this end-to-end: ad spend → lead → booking → occurred appointme…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/emadaed/your-dashboard-is-lying-the-spend-fan-out-trap-and-the-lead-i-lost-when-the-api-went-down-19ci

## Related notes
- [[2026-09-28-group-by-aggregate-functions-explained-the-where-vs-having-mistake-almost-everyone-makes]]
- [[2026-06-04-summing-platform-roas-overstates-your-ad-results-use-mer-instead-2026]]
- [[2026-09-26-why-your-join-doubled-your-totals-theres-no-error-just-the-wrong-number]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
