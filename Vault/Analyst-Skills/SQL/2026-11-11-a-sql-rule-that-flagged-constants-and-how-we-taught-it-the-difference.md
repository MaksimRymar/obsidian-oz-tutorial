---
title: A SQL rule that flagged constants, and how we taught it the difference
date: '2026-11-11'
source: https://dev.to/bedirhandev/a-sql-rule-that-flagged-constants-and-how-we-taught-it-the-difference-1m1i
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
related:
- '[[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]'
- '[[2026-11-11-python-just-got-a-new-kind-of-string-it-could-end-a-whole-class-of-security-bugs]]'
- '[[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]'
- '[[2026-06-07-what-a-policy-gate-catches-in-ai-generated-code-and-what-slips-through]]'
status: unread
---

> **TL;DR:** A rule that says string interpolation in SQL is an injection is right most of the time. It is also wrong in a predictable way, and the wrong cases are common in real code. This week a SQL rule in our scanner flagged code…

## What’s new and why it matters
A rule that says string interpolation in SQL is an injection is right most of the time. It is also wrong in a predictable way, and the wrong cases are common in real code. This week a SQL rule in our scanner flagged code that only ever ran with fixed values. Here is the code, what the rule saw, and what we changed. The loop over a fixed list for ( const table of [ "messages" , "threads" ] ) { await tx . execute ( `DELETE FROM ${table} WHERE account_id = ?` , [ accountId ] ) ; } Only accountId comes from outside, and it is bound as a parameter. table is one of two literals. The rule now follows…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/bedirhandev/a-sql-rule-that-flagged-constants-and-how-we-taught-it-the-difference-1m1i

## Related notes
- [[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]
- [[2026-11-11-python-just-got-a-new-kind-of-string-it-could-end-a-whole-class-of-security-bugs]]
- [[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]
- [[2026-06-07-what-a-policy-gate-catches-in-ai-generated-code-and-what-slips-through]]
