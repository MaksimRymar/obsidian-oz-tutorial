---
title: 'SQL CTEs: How to Build a Query in Steps You Can Check'
date: '2026-08-12'
source: https://dev.to/michaelnocito/sql-ctes-how-to-build-a-query-in-steps-you-can-check-3po
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tableau'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-08-12-group-by-and-having-how-to-summarize-rows-without-getting-a-fake-answer]]'
status: unread
---

> **TL;DR:** By the end of this page you can take a question that needs four decisions and write it as four named steps, each one testable on its own. You will know the WITH syntax, how to stack one step on the next, how to check a s…

## What’s new and why it matters
By the end of this page you can take a question that needs four decisions and write it as four named steps, each one testable on its own. You will know the WITH syntax, how to stack one step on the next, how to check a step's row count before you build on it, and when a CTE is the wrong tool. It is about twenty-five minutes. Here is what to actually do with it. Next time a query gets long enough that you have to scroll to understand it, stop and give its first step a name. Then run that step alone and look at the row count. Almost every query that produced a wrong number would have been caught…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/michaelnocito/sql-ctes-how-to-build-a-query-in-steps-you-can-check-3po

## Related notes
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-08-12-group-by-and-having-how-to-summarize-rows-without-getting-a-fake-answer]]
