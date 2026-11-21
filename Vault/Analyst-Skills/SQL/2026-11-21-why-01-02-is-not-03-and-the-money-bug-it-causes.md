---
title: Why 0.1 + 0.2 Is Not 0.3 (and the Money Bug It Causes)
date: '2026-11-21'
source: https://dev.to/refactorly/why-01-02-is-not-03-and-the-money-bug-it-causes-872
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-31-modelling-gtus-4-backlog-detain-rule-in-15-lines-of-python]]'
- '[[2026-10-17-i-added-a-fourth-shard-in-python-and-75-of-the-keys-moved]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]'
- '[[2026-08-29-why-your-sql-server-database-is-slow-and-how-to-fix-it]]'
- '[[2026-10-28-python-google-sheets-on-autopilot-why-your-script-dies-after-7-days-and-4-more-errors]]'
status: unread
---

> **TL;DR:** Ask almost any programming language for 0.1 + 0.2 and you get this: >>> 0.1 + 0.2 0.30000000000000004 >>> 0.1 + 0.2 == 0.3 False $ node -e "console.log(0.1 + 0.2 === 0.3)" false It's not a bug in Python or JavaScript. Ja…

## What’s new and why it matters
Ask almost any programming language for 0.1 + 0.2 and you get this: >>> 0.1 + 0.2 0.30000000000000004 >>> 0.1 + 0.2 == 0.3 False $ node -e "console.log(0.1 + 0.2 === 0.3)" false It's not a bug in Python or JavaScript. Java, C, Go and others give the same answer, because they all use the same number format: IEEE 754 binary floating point. Below is why it happens, the real money bug it causes, and how to fix it. Everything here was run on Python 3.15 and Node.js 22. Video version: Why: 0.1 can't be stored exactly in binary In decimal, 1/3 is 0.3333… forever, so any finite number of digits is sli…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/refactorly/why-01-02-is-not-03-and-the-money-bug-it-causes-872

## Related notes
- [[2026-10-31-modelling-gtus-4-backlog-detain-rule-in-15-lines-of-python]]
- [[2026-10-17-i-added-a-fourth-shard-in-python-and-75-of-the-keys-moved]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]
- [[2026-08-29-why-your-sql-server-database-is-slow-and-how-to-fix-it]]
- [[2026-10-28-python-google-sheets-on-autopilot-why-your-script-dies-after-7-days-and-4-more-errors]]
