---
title: 'Python Day 7: Positional-Only, Keyword-Only Arguments and Return Statement'
date: '2026-11-21'
source: https://dev.to/vasanthakumari_n/python-day-7-positional-only-keyword-only-arguments-and-return-statement-1j3k
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-07-29-python-part-2]]'
- '[[2026-07-02-a-complete-guide-to-function-arguments-in-python]]'
- '[[2026-10-02-a-pythonic-guide-to-functions]]'
- '[[2026-08-06-functions-in-python]]'
- '[[2026-08-12-can-you-run-hybrid-search-on-one-database-yes-heres-how-cratedb-does-it]]'
- '[[2026-07-29-keywords-and-data-types-in-python]]'
status: unread
---

> **TL;DR:** 1. Positional-Only Arguments (/) In Python, / is used as a positional-only argument separator. It means that the parameters written before / must be passed using their position. We cannot pass them using parameter names…

## What’s new and why it matters
1. Positional-Only Arguments (/) In Python, / is used as a positional-only argument separator. It means that the parameters written before / must be passed using their position. We cannot pass them using parameter names (keyword arguments). Example: def calculate ( a , b , / ) : print ( a + b ) calculate ( 10 , 20 ) # 30 calculate ( a = 10 , b = 20 ) # TypeError TypeError: calculate() got some positional-only arguments passed as keyword arguments Here, a and b must be passed as positional arguments. 2. Keyword-Only Arguments (*) In Python, * can be used as a keyword-only argument separator. It…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vasanthakumari_n/python-day-7-positional-only-keyword-only-arguments-and-return-statement-1j3k

## Related notes
- [[2026-07-29-python-part-2]]
- [[2026-07-02-a-complete-guide-to-function-arguments-in-python]]
- [[2026-10-02-a-pythonic-guide-to-functions]]
- [[2026-08-06-functions-in-python]]
- [[2026-08-12-can-you-run-hybrid-search-on-one-database-yes-heres-how-cratedb-does-it]]
- [[2026-07-29-keywords-and-data-types-in-python]]
