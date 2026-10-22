---
title: Your average response time is lying to you (use p95 and p99)
date: '2026-10-22'
source: https://dev.to/elvinaqalarov99/your-average-response-time-is-lying-to-you-use-p95-and-p99-4o0g
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-12-a-30-line-wrapper-that-tells-you-what-every-llm-call-actually-costs]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]'
- '[[2026-06-19-oracle-ora-00934-error-causes-and-solutions-complete-guide]]'
- '[[2026-08-30-funnel-conversion-in-sql-and-the-step-that-shows-100]]'
- '[[2026-09-18-the-dialect-trap-why-ai-writes-sql-your-database-refuses-to-run]]'
status: unread
---

> **TL;DR:** Your dashboard says average response time: 180 ms. Looks healthy. Meanwhile one in ten users waits almost a second. Here's why averages hide that, and what to use instead. The math trick hiding in your dashboard 100 requ…

## What’s new and why it matters
Your dashboard says average response time: 180 ms. Looks healthy. Meanwhile one in ten users waits almost a second. Here's why averages hide that, and what to use instead. The math trick hiding in your dashboard 100 requests: 90 take 100 ms 10 take 900 ms average = (90 × 100 + 10 × 900) / 100 = 180 ms Nobody experienced 180 ms. Most people got a fast answer, some got a slow one, and the average describes neither group. Now double the slow group to 20 requests: the average only moves to 260 ms . Still "fine" on a dashboard, while 1 in 5 users is having a bad time. Percentiles say what users act…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/elvinaqalarov99/your-average-response-time-is-lying-to-you-use-p95-and-p99-4o0g

## Related notes
- [[2026-09-12-a-30-line-wrapper-that-tells-you-what-every-llm-call-actually-costs]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]
- [[2026-06-19-oracle-ora-00934-error-causes-and-solutions-complete-guide]]
- [[2026-08-30-funnel-conversion-in-sql-and-the-step-that-shows-100]]
- [[2026-09-18-the-dialect-trap-why-ai-writes-sql-your-database-refuses-to-run]]
