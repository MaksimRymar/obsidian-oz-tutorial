---
title: Stop Using .iterrows(). Here's What Actually Fast Looks Like
date: '2026-05-21'
source: https://dev.to/imann_12/stop-using-iterrows-heres-what-actually-fast-looks-like-3j17
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-05-13-sql-execution-order-write-queries-that-think-like-the-database]]'
- '[[2026-04-28-arrayjoin-in-clickhouse-why-your-rows-are-duplicating-and-how-to-control-it]]'
- '[[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]'
- '[[2026-04-19-ai-agents-explained-simply-the-biggest-tech-shift-of-2026]]'
- '[[2026-04-08-if-youre-evaluating-ai-startups-at-venture-madness-ask-this-one-question]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
status: unread
---

> **TL;DR:** You're looping over a DataFrame. It feels natural. It's killing your performance. # What most tutorials say for index , row in df . iterrows (): df . at [ index , ' tax ' ] = row [ ' price ' ] * 0.17 Here's the progressi…

## What’s new and why it matters
You're looping over a DataFrame. It feels natural. It's killing your performance. # What most tutorials say for index , row in df . iterrows (): df . at [ index , ' tax ' ] = row [ ' price ' ] * 0.17 Here's the progression you should actually know: # Level 1: Vectorization — 10-100x faster df [ ' tax ' ] = df [ ' price ' ] * 0.17 # Level 2: .apply() when logic is conditional df [ ' tax ' ] = df [ ' price ' ]. apply ( lambda x : x * 0.17 if x > 0 else 0 ) # Level 3: np.where — the fastest option import numpy as np df [ ' tax ' ] = np . where ( df [ ' price ' ] > 0 , df [ ' price ' ] * 0.17 , 0…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/imann_12/stop-using-iterrows-heres-what-actually-fast-looks-like-3j17

## Related notes
- [[2026-05-13-sql-execution-order-write-queries-that-think-like-the-database]]
- [[2026-04-28-arrayjoin-in-clickhouse-why-your-rows-are-duplicating-and-how-to-control-it]]
- [[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]
- [[2026-04-19-ai-agents-explained-simply-the-biggest-tech-shift-of-2026]]
- [[2026-04-08-if-youre-evaluating-ai-startups-at-venture-madness-ask-this-one-question]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
