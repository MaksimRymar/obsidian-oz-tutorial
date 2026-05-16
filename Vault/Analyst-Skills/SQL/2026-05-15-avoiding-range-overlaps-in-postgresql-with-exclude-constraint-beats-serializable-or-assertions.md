---
title: Avoiding range overlaps in PostgreSQL with EXCLUDE constraint, beats serializable
  or assertions
date: '2026-05-15'
source: https://dev.to/franckpachot/postgresql-exclude-constraints-for-better-concurrency-than-serializable-pob
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-25-isolation]]'
- '[[2026-03-29-sql-assertions-ansi-join-and-ora-08697]]'
- '[[2026-04-17-postgresql-vs-mysql-which-is-better-for-your-application]]'
- '[[2026-03-26-create-tables]]'
status: unread
---

> **TL;DR:** Two groups of friends try to book seats ranges 5–8 and 7–9 in the same row, for the same show, at the same time. One of them must fail and retry. An ACID database can help enforce this rule. The question is: how much col…

## What’s new and why it matters
Two groups of friends try to book seats ranges 5–8 and 7–9 in the same row, for the same show, at the same time. One of them must fail and retry. An ACID database can help enforce this rule. The question is: how much collateral damage does your concurrency control cause for everyone else? In modern development, we tend to put the business logic in the application first. Still, enforcing business invariants in the database with integrity constraints may provide better performance when it avoids the need for the serializable isolation level required when the invariant concerns multiple rows. Thi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/franckpachot/postgresql-exclude-constraints-for-better-concurrency-than-serializable-pob

## Related notes
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-25-isolation]]
- [[2026-03-29-sql-assertions-ansi-join-and-ora-08697]]
- [[2026-04-17-postgresql-vs-mysql-which-is-better-for-your-application]]
- [[2026-03-26-create-tables]]
