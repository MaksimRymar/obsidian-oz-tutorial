---
title: Python Just Got a New Kind of String. It Could End a Whole Class of Security
  Bugs.
date: '2026-11-11'
source: https://dev.to/anas_issath/python-just-got-a-new-kind-of-string-it-could-end-a-whole-class-of-security-bugs-247h
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
status: unread
---

> **TL;DR:** t-strings (PEP 750) are the biggest change to Python string formatting since f-strings, and they exist for one reason: f-strings cannot be made safe. Here is what they are and why they matter. Every SQL injection, every…

## What’s new and why it matters
t-strings (PEP 750) are the biggest change to Python string formatting since f-strings, and they exist for one reason: f-strings cannot be made safe. Here is what they are and why they matter. Every SQL injection, every cross-site scripting hole, every shell-injection bug has the same shape at its heart. Somebody took a piece of untrusted input and glued it directly into a string that was then treated as code, as a query, as markup. The input became structure instead of data. query = f "SELECT * FROM users WHERE name = '{name}'" If name is O'Brien , the apostrophe closes the quoted value early…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/anas_issath/python-just-got-a-new-kind-of-string-it-could-end-a-whole-class-of-security-bugs-247h

## Related notes
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
