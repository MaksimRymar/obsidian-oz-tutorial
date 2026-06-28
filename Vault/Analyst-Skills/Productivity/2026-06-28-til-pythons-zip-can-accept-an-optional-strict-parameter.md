---
title: 'TIL: Python''s `zip()` can accept an optional `strict` parameter'
date: '2026-06-28'
source: https://dev.to/qingluan/til-pythons-zip-can-accept-an-optional-strict-parameter-4e9h
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-06-14-mastering-python-decorators-a-practical-guide-for-cleaner-code]]'
- '[[2026-03-11-what-is-snowflake-a-beginners-guide-to-the-cloud-data-warehouse-everyones-talking-about]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-06-02-lists-in-python]]'
- '[[2026-03-20-valid-anagram]]'
- '[[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]'
status: unread
---

> **TL;DR:** TIL: Python's zip() can accept an optional strict parameter If you're like me, you've probably used Python's built-in zip() function countless times to iterate over multiple lists in parallel. However, have you ever stop…

## What’s new and why it matters
TIL: Python's zip() can accept an optional strict parameter If you're like me, you've probably used Python's built-in zip() function countless times to iterate over multiple lists in parallel. However, have you ever stopped to think about what happens when the lists are of different lengths? Prior to Python 3.10, zip() would simply stop at the end of the shortest list, potentially leading to silent data loss. As of Python 3.10, zip() now accepts an optional strict parameter, which defaults to False . When set to True , zip() will raise a ValueError if the input lists are of different lengths.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/qingluan/til-pythons-zip-can-accept-an-optional-strict-parameter-4e9h

## Related notes
- [[2026-06-14-mastering-python-decorators-a-practical-guide-for-cleaner-code]]
- [[2026-03-11-what-is-snowflake-a-beginners-guide-to-the-cloud-data-warehouse-everyones-talking-about]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-06-02-lists-in-python]]
- [[2026-03-20-valid-anagram]]
- [[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]
