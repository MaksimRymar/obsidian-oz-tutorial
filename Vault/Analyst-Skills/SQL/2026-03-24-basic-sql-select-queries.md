---
title: Basic SQL Select Queries
date: '2026-03-24'
source: https://dev.to/jonah_blessy/basic-sql-select-queries-54l3
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-09-the-sql-query-that-ruined-my-weekend-and-what-i-built-to-prevent-it]]'
- '[[2026-03-04-the-two-sql-concepts-that-made-me-finally-understand-real-data-joins-window-functions]]'
- '[[2026-03-24-basic-select-sql-queries]]'
- '[[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]'
- '[[2026-03-16-my-journey-into-artificial-intelligence-why-i-chose-this-path]]'
status: unread
---

> **TL;DR:** Qn 1. This first question in SQL helped me to recollect the basics I learnt. The solution came to me almost instantly requiring not much thought. The question wants the rows in column CITY that has ID 1661. SELECT * FROM…

## What’s new and why it matters
Qn 1. This first question in SQL helped me to recollect the basics I learnt. The solution came to me almost instantly requiring not much thought. The question wants the rows in column CITY that has ID 1661. SELECT * FROM city WHERE id = 1661 ; Qn 2. This was also pretty intuitive knowing the very basics that were brushed up in class. select * from city where countrycode = 'USA' and population > 100000 ; Qn 3. Another easy query returning one column using where clause. select * from city where countrycode = 'JPN' ; Qn 4. This was a little challenging at first. I couldn't remember count so it th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jonah_blessy/basic-sql-select-queries-54l3

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-09-the-sql-query-that-ruined-my-weekend-and-what-i-built-to-prevent-it]]
- [[2026-03-04-the-two-sql-concepts-that-made-me-finally-understand-real-data-joins-window-functions]]
- [[2026-03-24-basic-select-sql-queries]]
- [[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]
- [[2026-03-16-my-journey-into-artificial-intelligence-why-i-chose-this-path]]
