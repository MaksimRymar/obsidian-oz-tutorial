---
title: null=True on CharField Is Always Wrong — Here Is Why
date: '2026-04-22'
source: https://dev.to/h_coder/nulltrue-on-charfield-is-always-wrong-here-is-why-1bop
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
related:
- '[[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]'
- '[[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]'
- '[[2026-04-10-sql-case-expressions-write-smarter-queries-with-conditional-logic]]'
- '[[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]'
- '[[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]'
- '[[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]'
status: unread
---

> **TL;DR:** PROFESSIONAL DJANGO ENGINEERING SERIES #4 Two ways to represent 'no value' means every query that checks for empty strings has to handle both. The rule is simple once you know it. Django provides two separate flags for h…

## What’s new and why it matters
PROFESSIONAL DJANGO ENGINEERING SERIES #4 Two ways to represent 'no value' means every query that checks for empty strings has to handle both. The rule is simple once you know it. Django provides two separate flags for handling empty values on model fields. They are frequently confused, and conflating them leads to subtle bugs, inconsistent data, and queries that are harder to write than they should be. Here is the rule stated plainly, and then the reasoning behind it. null=True is a database directive. blank=True is a validation directive. They are independent. Think about each one separately…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/h_coder/nulltrue-on-charfield-is-always-wrong-here-is-why-1bop

## Related notes
- [[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]
- [[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]
- [[2026-04-10-sql-case-expressions-write-smarter-queries-with-conditional-logic]]
- [[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]
- [[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]
- [[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]
