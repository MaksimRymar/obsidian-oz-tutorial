---
title: 'Getting Started with Seal Report: Applying Dependant Filters'
date: '2026-03-29'
source: https://dev.to/vladg_dev/getting-started-with-seal-report-applying-dependant-filters-3j7a
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-03-02-joins-and-windows-function-in-sql]]'
- '[[2026-03-02-sql-joins-explained-case-example]]'
- '[[2026-03-03-sql-joins-and-window-functions-with-case-example]]'
- '[[2026-03-09-mastering-sql-joins-and-window-functions-with-real-examples]]'
- '[[2026-03-10-joins-window-functions]]'
- '[[2026-03-26-create-tables]]'
status: unread
---

> **TL;DR:** This is the fourth report in the series. So far, we’ve used different types of restrictions, but those were independent of each other. However, real-world filtering scenarios often require dependent restrictions, where o…

## What’s new and why it matters
This is the fourth report in the series. So far, we’ve used different types of restrictions, but those were independent of each other. However, real-world filtering scenarios often require dependent restrictions, where one selection affects the available values of another. Within the AdventureWorks2025 open-source database, there is a classic example of such dependency: CountryRegion → StateProvince . Applying this type of filter allows us to narrow down employees based on the province associated with one of their recorded addresses, while ensuring that only provinces belonging to the selected…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vladg_dev/getting-started-with-seal-report-applying-dependant-filters-3j7a

## Related notes
- [[2026-03-02-joins-and-windows-function-in-sql]]
- [[2026-03-02-sql-joins-explained-case-example]]
- [[2026-03-03-sql-joins-and-window-functions-with-case-example]]
- [[2026-03-09-mastering-sql-joins-and-window-functions-with-real-examples]]
- [[2026-03-10-joins-window-functions]]
- [[2026-03-26-create-tables]]
