---
title: 'SQLazy: Get the Latest Closed Before ConfirmationStarted'
date: '2026-09-04'
source: https://dev.to/esproc_spl/sqlazy-get-the-latest-closed-before-confirmationstarted-ha5
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-08-26-sqlazy-search-for-adjacent-records-at-a-specified-offset-within-groups]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-04-sqlazymerge-multiple-tables-into-single-rows-by-common-id]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
status: unread
---

> **TL;DR:** Problem Description Database table mytable stores the status NewStatus of multiple IDs at different timestamps CreatedAt. Each ID has exactly one ConfirmationStarted and one or more Closed statuses. The task is: within e…

## What’s new and why it matters
Problem Description Database table mytable stores the status NewStatus of multiple IDs at different timestamps CreatedAt. Each ID has exactly one ConfirmationStarted and one or more Closed statuses. The task is: within each ID, among all the Closed records before ConfirmationStarted, find the one closest to ConfirmationStarted, and take the record's ID and time fields. Source Data Expected Result Take ID=147 as an example: ConfirmationStarted occurs on 2022-07-13; before it, the three Closed records happen on 05-28, 06-18 and 06-25, and the one closest to it is 2022-06-25 05:59:01, which is ex…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/esproc_spl/sqlazy-get-the-latest-closed-before-confirmationstarted-ha5

## Related notes
- [[2026-08-26-sqlazy-search-for-adjacent-records-at-a-specified-offset-within-groups]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-04-sqlazymerge-multiple-tables-into-single-rows-by-common-id]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
