---
title: Python Metaclasses, What's Actually Happening When You Write class
date: '2026-04-29'
source: https://dev.to/shayan_holakouee/python-metaclasses-whats-actually-happening-when-you-write-class-f15
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-04-27-sql-building-blocks-how-subqueries-and-ctes-shape-your-data]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]'
status: unread
---

> **TL;DR:** Every Python developer knows that everything is an object. What fewer know is that classes are objects too, and like every other object, they are instances of something. That something is a metaclass. Understanding metac…

## What’s new and why it matters
Every Python developer knows that everything is an object. What fewer know is that classes are objects too, and like every other object, they are instances of something. That something is a metaclass. Understanding metaclasses means understanding how Python builds classes in the first place, which turns out to explain a lot of behavior that otherwise looks like magic. Classes Are Instances of type Start here: class MyClass : pass print ( type ( MyClass )) # <class 'type'> print ( type ( int )) # <class 'type'> print ( type ( str )) # <class 'type'> print ( type ( type )) # <class 'type'> type…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/shayan_holakouee/python-metaclasses-whats-actually-happening-when-you-write-class-f15

## Related notes
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-04-27-sql-building-blocks-how-subqueries-and-ctes-shape-your-data]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]
