---
title: 'PostgreSQL Unused Sequences: How to Find Them, and Which Ones Are Safe to
  Drop'
date: '2026-11-27'
source: https://dev.to/tbson87/postgresql-unused-sequences-how-to-find-them-and-which-ones-are-safe-to-drop-1m9f
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-11-27-postgresql-drop-column-what-it-refuses-and-what-it-drops-without-a-warning]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-09-27-postgresql-generated-column-vs-trigger-which-to-use-for-a-derived-column]]'
- '[[2026-11-27-soft-delete-vs-archive-table-which-one-keeps-your-foreign-keys-working]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: The catalog answers half the question: a sequence attached to a column, used by a column default or by a…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: The catalog answers half the question: a sequence attached to a column, used by a column default or by a BEGIN ATOMIC function cannot be dropped by accident, and PostgreSQL says so. A legacy default written as nextval('s'::text) , a function whose body is a string and application code record no dependency at all, so the drop succeeds and the next insert fails. Find those by searching defaults and function bodies, then watch last_value for a while before dropping anything. You fin…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/postgresql-unused-sequences-how-to-find-them-and-which-ones-are-safe-to-drop-1m9f

## Related notes
- [[2026-11-27-postgresql-drop-column-what-it-refuses-and-what-it-drops-without-a-warning]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-09-27-postgresql-generated-column-vs-trigger-which-to-use-for-a-derived-column]]
- [[2026-11-27-soft-delete-vs-archive-table-which-one-keeps-your-foreign-keys-working]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]
