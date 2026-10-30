---
title: 'The SQL NOT IN Trap: When NULL Quietly Breaks Your Query'
date: '2026-10-30'
source: https://dev.to/sinarezaei/the-sql-not-in-trap-when-null-quietly-breaks-your-query-h81
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]'
- '[[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]'
- '[[2026-09-12-what-actually-happens-when-you-run-a-database-query]]'
- '[[2026-09-29-subqueries-ctes-two-ways-to-query-inside-a-query]]'
- '[[2026-08-16-how-to-turn-plain-english-requirements-into-sql-you-can-actually-trust]]'
status: unread
---

> **TL;DR:** Some SQL bugs don't throw errors. The query runs, the tests pass, and everything looks fine until a cleanup job skips records it was supposed to catch. One of the reasons this happens is NULL inside a NOT IN query. When…

## What’s new and why it matters
Some SQL bugs don't throw errors. The query runs, the tests pass, and everything looks fine until a cleanup job skips records it was supposed to catch. One of the reasons this happens is NULL inside a NOT IN query. When NOT IN stops behaving as expected Imagine you're working on a multi-tenant platform. You have a memberships table and an identity_mappings table. Each mapping connects an external identity to a tenant. You need to find memberships that don't have a corresponding identity mapping. A first attempt might look like this: SELECT m . tenant_id , m . external_id FROM memberships m WHE…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sinarezaei/the-sql-not-in-trap-when-null-quietly-breaks-your-query-h81

## Related notes
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]
- [[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]
- [[2026-09-12-what-actually-happens-when-you-run-a-database-query]]
- [[2026-09-29-subqueries-ctes-two-ways-to-query-inside-a-query]]
- [[2026-08-16-how-to-turn-plain-english-requirements-into-sql-you-can-actually-trust]]
