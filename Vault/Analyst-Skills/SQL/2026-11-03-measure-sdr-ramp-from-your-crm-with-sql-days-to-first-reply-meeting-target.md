---
title: Measure SDR ramp from your CRM with SQL (days to first reply, meeting, target)
date: '2026-11-03'
source: https://dev.to/noelmartin/measure-sdr-ramp-from-your-crm-with-sql-days-to-first-reply-meeting-target-2fi0
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-10-13-snowflake-sql-patterns-for-revenue-reporting]]'
- '[[2026-10-24-sql-find-the-customers-who-stopped-ordering-with-a-left-join-and-why-a-plain-join-hides-the-one-you-most-need-to-call]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]'
status: unread
---

> **TL;DR:** "How long does it take a new SDR to ramp?" usually gets one number: about three months, the median in Bridge Group's 2025 study of 351 B2B companies. That is a useful benchmark. It says nothing about your team, or which…

## What’s new and why it matters
"How long does it take a new SDR to ramp?" usually gets one number: about three months, the median in Bridge Group's 2025 study of 351 B2B companies. That is a useful benchmark. It says nothing about your team, or which part of ramp is slow. Ramp is not one number. It is a series of firsts: the first reply from someone who owns the problem, the first meeting held with someone who decides, the first month at target. If you log activities in a CRM, you can measure each of those per rep with a few queries. The tables Most CRMs export something close to this: create table rep ( rep_id int primary…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/noelmartin/measure-sdr-ramp-from-your-crm-with-sql-days-to-first-reply-meeting-target-2fi0

## Related notes
- [[2026-10-13-snowflake-sql-patterns-for-revenue-reporting]]
- [[2026-10-24-sql-find-the-customers-who-stopped-ordering-with-a-left-join-and-why-a-plain-join-hides-the-one-you-most-need-to-call]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]
