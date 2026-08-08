---
title: '# 🔬 PostgreSQL Internals: What Is Actually Inside an 8 KB Page?'
date: '2026-08-08'
source: https://dev.to/ahmedraza_fyntune/-postgresql-internals-what-is-actually-inside-an-8-kb-page-3cfg
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-06-12-indexes-quickstart-using-postgresql-15-sec-read]]'
- '[[2026-04-19-build-your-own-types-classes-explained-simply]]'
- '[[2026-05-09-how-i-built-a-real-time-postgresql-wal-reader-in-go]]'
status: unread
---

> **TL;DR:** In my previous post, I looked at what happens when PostgreSQL executes a SELECT query. One part of that journey caught my attention: PostgreSQL doesn't simply read "rows" from disk. It works with pages . So I wanted to g…

## What’s new and why it matters
In my previous post, I looked at what happens when PostgreSQL executes a SELECT query. One part of that journey caught my attention: PostgreSQL doesn't simply read "rows" from disk. It works with pages . So I wanted to go one level deeper. What is actually inside a PostgreSQL page? Today, we're going to inspect one. Not just with a diagram. We'll use PostgreSQL itself to look inside its storage. 🧠 First: What Is a PostgreSQL Page? PostgreSQL stores table and index data in fixed-size blocks called pages . In a standard PostgreSQL build, a page is: 8 KB So instead of imagining a table like this:…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ahmedraza_fyntune/-postgresql-internals-what-is-actually-inside-an-8-kb-page-3cfg

## Related notes
- [[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-06-12-indexes-quickstart-using-postgresql-15-sec-read]]
- [[2026-04-19-build-your-own-types-classes-explained-simply]]
- [[2026-05-09-how-i-built-a-real-time-postgresql-wal-reader-in-go]]
