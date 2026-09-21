---
title: A New Take on Raw SQL in Python
date: '2026-09-21'
source: https://dev.to/doekman/a-new-take-on-raw-sql-in-python-13ne
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-07-02-dont-use-not-in]]'
- '[[2026-09-14-coming-from-java-functions-are-values-in-python]]'
- '[[2026-03-07-quarks-outlines-python-emulating-callable-objects]]'
- '[[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]'
- '[[2026-08-26-python-for-data-analytics-a-hands-on-field-guide]]'
- '[[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]'
status: unread
---

> **TL;DR:** I've been using the excellent PugSQL library for some years now. It's very easy to use: just annotate your SQL queries in a text-file with a name, result-type and parameters; then load the sql file with a PugSQL module a…

## What’s new and why it matters
I've been using the excellent PugSQL library for some years now. It's very easy to use: just annotate your SQL queries in a text-file with a name, result-type and parameters; then load the sql file with a PugSQL module and you can run queries by calling a method with the name of the query. The calling in Python is handled by the __call__ -method of the module. While this is elegant by itself, you don't get to have all the standard goodness you get by using Python's native function definitions. What if you could link a Python function to a SQL query in some way? That's exactly why I made PySQLe…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/doekman/a-new-take-on-raw-sql-in-python-13ne

## Related notes
- [[2026-07-02-dont-use-not-in]]
- [[2026-09-14-coming-from-java-functions-are-values-in-python]]
- [[2026-03-07-quarks-outlines-python-emulating-callable-objects]]
- [[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]
- [[2026-08-26-python-for-data-analytics-a-hands-on-field-guide]]
- [[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]
