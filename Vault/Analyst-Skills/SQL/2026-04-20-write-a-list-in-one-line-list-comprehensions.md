---
title: Write a List in One Line (List Comprehensions)
date: '2026-04-20'
source: https://dev.to/yakhilesh/write-a-list-in-one-line-list-comprehensions-3f1a
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-23-build-your-first-ai-agent-with-python-and-langchain-in-2026]]'
- '[[2026-04-19-build-your-own-types-classes-explained-simply]]'
- '[[2026-04-08-understanding-python-loops-a-beginner-friendly-guide]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-03-24-control-statements-in-python-if-else-loops]]'
status: unread
---

> **TL;DR:** You have been building lists the long way. numbers = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ] squares = [] for n in numbers : squares . append ( n * n ) print ( squares ) Output: [ 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 ,…

## What’s new and why it matters
You have been building lists the long way. numbers = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ] squares = [] for n in numbers : squares . append ( n * n ) print ( squares ) Output: [ 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100 ] Four lines. A variable, a loop, an operation, an append. This works perfectly. Nothing wrong with it. But Python has a shorter way. One line instead of four. numbers = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ] squares = [ n * n for n in numbers ] print ( squares ) Output: [ 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100 ] Same result. One line. This is a list compreh…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yakhilesh/write-a-list-in-one-line-list-comprehensions-3f1a

## Related notes
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-23-build-your-first-ai-agent-with-python-and-langchain-in-2026]]
- [[2026-04-19-build-your-own-types-classes-explained-simply]]
- [[2026-04-08-understanding-python-loops-a-beginner-friendly-guide]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-03-24-control-statements-in-python-if-else-loops]]
