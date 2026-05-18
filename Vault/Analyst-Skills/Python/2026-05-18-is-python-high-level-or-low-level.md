---
title: Is Python High Level Or Low Level?
date: '2026-05-18'
source: https://dev.to/aaronmaxwell/is-python-high-level-or-low-level-d73
domain: Python
relevance: 🟡
tags:
- '#python'
- '#tool'
related:
- '[[2026-05-03-pandas-secret-mini-language]]'
- '[[2026-03-23-on-static-analysis-llm]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-04-08-understanding-python-loops-a-beginner-friendly-guide]]'
status: unread
---

> **TL;DR:** Imagine you need to fill a list with square numbers - or more complex objects, but we'll just use square numbers to keep it simple. Here's one way to do it: MAX_ROOT = 100 values = [] for x in range ( MAX_ROOT ): values…

## What’s new and why it matters
Imagine you need to fill a list with square numbers - or more complex objects, but we'll just use square numbers to keep it simple. Here's one way to do it: MAX_ROOT = 100 values = [] for x in range ( MAX_ROOT ): values . append ( x ** 2 ) print ( values ) Does the job, and much easier to follow than the C version: #include <stdio.h> #define MAX_VALUE 100 int main () { int values [ MAX_VALUE ]; for ( int i = 0 ; i < MAX_VALUE ; i ++ ) { values [ i ] = i * i ; } for ( int i = 0 ; i < MAX_VALUE ; i ++ ) { printf ( "%d %d \n " , i , values [ i ]); } return 0 ; } What makes it easier to follow? Se…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aaronmaxwell/is-python-high-level-or-low-level-d73

## Related notes
- [[2026-05-03-pandas-secret-mini-language]]
- [[2026-03-23-on-static-analysis-llm]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-04-08-understanding-python-loops-a-beginner-friendly-guide]]
