---
title: 'SQL injection in the WHERE clause: how to reach unreleased products (PortSwigger)'
date: '2026-11-12'
source: https://dev.to/gh0stbloom/sql-injection-in-the-where-clause-how-to-reach-unreleased-products-portswigger-2089
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-07-18-building-my-first-real-database-what-a-weekend-sql-assignment-taught-me-about-postgres-and-git]]'
- '[[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]'
- '[[2026-09-08-column-must-appear-in-the-group-by-clause-why-sql-wont-let-you-do-that]]'
- '[[2026-11-11-python-just-got-a-new-kind-of-string-it-could-end-a-whole-class-of-security-bugs]]'
- '[[2026-03-07-where-clause-allowing-retrieval-of-hidden-data-sql-injection-vulnerability]]'
- '[[2026-10-27-filtering-data-in-sql-a-beginners-guide-to-where-using-and-or-like-and-friends]]'
status: unread
---

> **TL;DR:** SQL injection in the WHERE clause: how to reach unreleased products (PortSwigger) Another lab from PortSwigger Academy: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data . The goal is simple:…

## What’s new and why it matters
SQL injection in the WHERE clause: how to reach unreleased products (PortSwigger) Another lab from PortSwigger Academy: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data . The goal is simple: display one or more unreleased products via SQL injection. Starting point The shop filters products by category. In Burp I intercepted the request for opening a product description. The GET request includes the parameter productID=6 , the product number. Hypothesis Task tells us that server-side SQL query contains a released = 1 condition. If so, perhaps released = 0 would show…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/gh0stbloom/sql-injection-in-the-where-clause-how-to-reach-unreleased-products-portswigger-2089

## Related notes
- [[2026-07-18-building-my-first-real-database-what-a-weekend-sql-assignment-taught-me-about-postgres-and-git]]
- [[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]
- [[2026-09-08-column-must-appear-in-the-group-by-clause-why-sql-wont-let-you-do-that]]
- [[2026-11-11-python-just-got-a-new-kind-of-string-it-could-end-a-whole-class-of-security-bugs]]
- [[2026-03-07-where-clause-allowing-retrieval-of-hidden-data-sql-injection-vulnerability]]
- [[2026-10-27-filtering-data-in-sql-a-beginners-guide-to-where-using-and-or-like-and-friends]]
