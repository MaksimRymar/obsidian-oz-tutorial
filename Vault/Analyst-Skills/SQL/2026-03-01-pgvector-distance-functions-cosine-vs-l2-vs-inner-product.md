---
title: 'pgvector Distance Functions: Cosine vs L2 vs Inner Product'
date: '2026-03-01'
source: https://dev.to/philip_mcclarence_2ef9475/pgvector-distance-functions-cosine-vs-l2-vs-inner-product-57pd
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-02-22-5-most-asked-sql-interview-questions]]'
- '[[2026-02-24-detcting-burnout-before-it-hits-building-an-hrv-anomaly-detector-with-isolation-forest]]'
- '[[2026-02-24-countcolumn-vs-count-in-sql-with-inner-left-right-full-join-explained]]'
- '[[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]'
status: unread
---

> **TL;DR:** pgvector Distance Functions: Cosine vs L2 vs Inner Product If you're using pgvector for similarity search, you've probably seen the three distance operators -- <=> , <-> , and <#> -- and picked one based on whatever tuto…

## What’s new and why it matters
pgvector Distance Functions: Cosine vs L2 vs Inner Product If you're using pgvector for similarity search, you've probably seen the three distance operators -- <=> , <-> , and <#> -- and picked one based on whatever tutorial you followed first. That works until it doesn't. Using the wrong distance function produces subtly wrong results: your queries return rows, ordered by some number, but the ranking doesn't match what your application actually needs. And the most common mistake isn't even picking the wrong function -- it's building an index with one operator class while your queries use a di…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/philip_mcclarence_2ef9475/pgvector-distance-functions-cosine-vs-l2-vs-inner-product-57pd

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-02-22-5-most-asked-sql-interview-questions]]
- [[2026-02-24-detcting-burnout-before-it-hits-building-an-hrv-anomaly-detector-with-isolation-forest]]
- [[2026-02-24-countcolumn-vs-count-in-sql-with-inner-left-right-full-join-explained]]
- [[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]
