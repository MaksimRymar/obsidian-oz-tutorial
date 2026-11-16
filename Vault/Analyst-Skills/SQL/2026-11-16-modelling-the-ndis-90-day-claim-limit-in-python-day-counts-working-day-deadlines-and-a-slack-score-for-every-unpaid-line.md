---
title: 'Modelling the NDIS 90-day claim limit in Python: day counts, working-day deadlines
  and a slack score for every unpaid line'
date: '2026-11-16'
source: https://dev.to/rostery/modelling-the-ndis-90-day-claim-limit-in-python-day-counts-working-day-deadlines-and-a-slack-4mpc
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tableau'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
status: unread
---

> **TL;DR:** Originally based on our guide to the NDIS 90-day claim rule on rostery.com.au. This version is rewritten for developers, finance analysts and anyone who builds the reports behind NDIS claiming. General information only,…

## What’s new and why it matters
Originally based on our guide to the NDIS 90-day claim rule on rostery.com.au. This version is rewritten for developers, finance analysts and anyone who builds the reports behind NDIS claiming. General information only, not legal or financial advice. The day count and some edge cases below are our reading of the Act; the NDIA hasn't published guidance on them. Australia's National Disability Insurance Scheme (NDIS) pays providers for supports delivered to participants under their plans. Until 30 November 2026, a claim for a support can be made up to 2 years after the support. From 1 December 2…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rostery/modelling-the-ndis-90-day-claim-limit-in-python-day-counts-working-day-deadlines-and-a-slack-4mpc

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
