---
title: 'for loops and range() in Python: iterate without the busywork'
date: '2026-08-06'
source: https://dev.to/fj_palacios/for-loops-and-range-in-python-iterate-without-the-busywork-4fi9
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-22-mastering-python-lists-through-real-world-use-a-practical-developers-guide]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-07-03-why-does-a-list-change-in-two-variables]]'
- '[[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
status: unread
---

> **TL;DR:** You already know how to count from 1 to 10 with while . A counter, a condition, an increment — four lines of code where three of them exist only to serve the fourth. That works. But Python has a better tool for situation…

## What’s new and why it matters
You already know how to count from 1 to 10 with while . A counter, a condition, an increment — four lines of code where three of them exist only to serve the fourth. That works. But Python has a better tool for situations like this: # while: you manage the counter yourself counter = 1 while counter <= 10 : print ( counter ) counter += 1 # for: Python manages it for you for i in range ( 1 , 11 ): print ( i ) Same result. Half the ceremony. The difference isn't just aesthetic — it's about intent. The for loop says "I know exactly what I want to iterate over." The while says "keep going until thi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/fj_palacios/for-loops-and-range-in-python-iterate-without-the-busywork-4fi9

## Related notes
- [[2026-04-22-mastering-python-lists-through-real-world-use-a-practical-developers-guide]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-07-03-why-does-a-list-change-in-two-variables]]
- [[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
