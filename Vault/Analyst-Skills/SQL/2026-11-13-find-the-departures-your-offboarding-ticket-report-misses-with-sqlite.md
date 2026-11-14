---
title: Find the Departures Your Offboarding Ticket Report Misses with SQLite
date: '2026-11-13'
source: https://dev.to/manfredimarrocco/find-the-departures-your-offboarding-ticket-report-misses-with-sqlite-1l33
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
status: unread
---

> **TL;DR:** A dashboard can report that every offboarding ticket is closed while a departure never entered the ticket system. Improving the query over tickets alone will not reveal that person: the missing row is outside the query's…

## What’s new and why it matters
A dashboard can report that every offboarding ticket is closed while a departure never entered the ticket system. Improving the query over tickets alone will not reveal that person: the missing row is outside the query's starting population. Here is a small, runnable example that starts with a separate departure list and reconciles it with ticket and account records. All identifiers and circumstances below are fictional. The program creates an in-memory demonstration database; it does not connect to an employer's systems or change access permissions. Start with the population you want to check…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/manfredimarrocco/find-the-departures-your-offboarding-ticket-report-misses-with-sqlite-1l33

## Related notes
- [[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
