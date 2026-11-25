---
title: 'Don''t Hard-Code Your Statuses: A Practical Common-Codes Table Design'
date: '2026-11-25'
source: https://dev.to/truerows/dont-hard-code-your-statuses-a-practical-common-codes-table-design-24dg
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]'
- '[[2026-09-15-sql-joins-explained]]'
status: unread
---

> **TL;DR:** Order status, payment method, gender, document type: almost every business screen has a field where the user picks one value from a fixed list. It is tempting to put those values in an enum, a CHECK constraint, or a swit…

## What’s new and why it matters
Order status, payment method, gender, document type: almost every business screen has a field where the user picks one value from a fixed list. It is tempting to put those values in an enum, a CHECK constraint, or a switch in the application. That works until someone asks for a new status, or the same list starts to drift across screens. A common-codes table moves those values into data. An administrator can add, rename, or deactivate a code on a screen, and dropdowns, radio buttons, and search filters all read from the same place. The design looks simple. What usually goes wrong later is how…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/truerows/dont-hard-code-your-statuses-a-practical-common-codes-table-design-24dg

## Related notes
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]
- [[2026-09-15-sql-joins-explained]]
