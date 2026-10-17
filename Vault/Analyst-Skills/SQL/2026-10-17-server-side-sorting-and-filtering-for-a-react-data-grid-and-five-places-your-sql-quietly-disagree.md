---
title: Server-side sorting and filtering for a React data grid, and five places your
  SQL quietly disagree
date: '2026-10-17'
source: https://dev.to/kanunilabs/server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree-3oc6
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-15-the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-attempts]]'
- '[[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
status: unread
---

> **TL;DR:** When the data is too big for the browser, or some users may only see some of it, the grid stops sorting and filtering in the browser. It sends your server the sort, the filters and the search, asks for 100 rows at a time…

## What’s new and why it matters
When the data is too big for the browser, or some users may only see some of it, the grid stops sorting and filtering in the browser. It sends your server the sort, the filters and the search, asks for 100 rows at a time and shows what comes back. The browser then has no way to know whether those 100 rows are right. The endpoint behind it is usually written in an afternoon: turn the request into WHERE , ORDER BY , LIMIT and OFFSET , run it, return the rows and a count. This post runs that version against a real table and compares it with what the grid would have shown with the data in the brow…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kanunilabs/server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree-3oc6

## Related notes
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-15-the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-attempts]]
- [[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
