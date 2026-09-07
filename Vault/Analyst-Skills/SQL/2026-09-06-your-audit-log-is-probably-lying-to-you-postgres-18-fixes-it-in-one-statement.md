---
title: Your audit log is probably lying to you. Postgres 18 fixes it in one statement.
date: '2026-09-06'
source: https://dev.to/remdore/your-audit-log-is-probably-lying-to-you-postgres-18-fixes-it-in-one-statement-15nb
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
status: unread
---

> **TL;DR:** I've written this more times than I'd like, in four or five languages by now: SELECT balance FROM accounts WHERE id = 1 ; -- application does the arithmetic UPDATE accounts SET balance = $ new WHERE id = 1 ; INSERT INTO…

## What’s new and why it matters
I've written this more times than I'd like, in four or five languages by now: SELECT balance FROM accounts WHERE id = 1 ; -- application does the arithmetic UPDATE accounts SET balance = $ new WHERE id = 1 ; INSERT INTO audit_log ( account_id , old_balance , new_balance ) VALUES ( 1 , $ old , $ new ); Read it, do the sum, write it back. Log what happened. Nothing about that raises an eyebrow in review, and it falls apart the second two people hit it together. The annoying part is that the audit log, which you added to catch this sort of thing, is what buries it. Postgres 18 turns the whole thi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/remdore/your-audit-log-is-probably-lying-to-you-postgres-18-fixes-it-in-one-statement-15nb

## Related notes
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
