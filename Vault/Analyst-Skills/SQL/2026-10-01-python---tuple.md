---
title: PYTHON - TUPLE
date: '2026-10-01'
source: https://dev.to/keerti_sadanas_d3bbb8924/python-tuple-4b7c
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-14-the-right-container-for-the-job-python-data-structures]]'
- '[[2026-06-02-lists-in-python]]'
- '[[2026-06-04-python---set]]'
- '[[2026-07-29-python]]'
- '[[2026-07-29-keywords-and-data-types-in-python]]'
- '[[2026-06-14-agent-series-20-harness-in-production-from-single-file-to-reusable-package]]'
status: unread
---

> **TL;DR:** -> A tuple in Python is a built-in collection data type used to store multiple items in a single variable. -> It is characterised by being ordered, immutable (unchangeable), and allowing duplicate values -> Similar to Li…

## What’s new and why it matters
-> A tuple in Python is a built-in collection data type used to store multiple items in a single variable. -> It is characterised by being ordered, immutable (unchangeable), and allowing duplicate values -> Similar to List -> Insertion Order is maintained -> Duplicate elements are allowed -> Performance - Tuple is good t = ( 10 , 20 , 30 , 40 , 50 ) t2 = () print ( type ( t2 )) t3 = ( 10 ) print ( type ( t3 )) t4 = ( 10 ,) print ( type ( t4 )) Output: t1 = ( 10 , 20 , 30 ) t2 = ( 40 , 50 , 60 ) t3 = t1 + t2 print ( t3 ) print ( t1 * 2 ) print ( 100 in t1 ) print ( 100 not in t1 ) Output: (10,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/keerti_sadanas_d3bbb8924/python-tuple-4b7c

## Related notes
- [[2026-09-14-the-right-container-for-the-job-python-data-structures]]
- [[2026-06-02-lists-in-python]]
- [[2026-06-04-python---set]]
- [[2026-07-29-python]]
- [[2026-07-29-keywords-and-data-types-in-python]]
- [[2026-06-14-agent-series-20-harness-in-production-from-single-file-to-reusable-package]]
