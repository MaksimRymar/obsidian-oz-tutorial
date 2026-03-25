---
title: Select Queries from DVD Rental database Pt-2
date: '2026-03-24'
source: https://dev.to/s_a_r_a/select-queries-from-dvd-rental-database-1m51
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
related:
- '[[2026-03-24-select-queries-from-dvd-rental-database-pt-3]]'
- '[[2026-03-04-sql-cheatsheet]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-02-database-indexing-explained-how-to-make-your-queries-1000x-faster]]'
- '[[2026-03-10-sql-joins-and-window-functions]]'
- '[[2026-02-24-countcolumn-vs-count-in-sql-with-inner-left-right-full-join-explained]]'
status: unread
---

> **TL;DR:** 5) List all unique replacement costs from the film table cmd: SELECT DISTINCT replacement_cost FROM film; SAMPLE OP: replacement_cost 19.99 25.99 13.99 10.99 23.99 18.99 20.99 6) List all films' title and length in minut…

## What’s new and why it matters
5) List all unique replacement costs from the film table cmd: SELECT DISTINCT replacement_cost FROM film; SAMPLE OP: replacement_cost 19.99 25.99 13.99 10.99 23.99 18.99 20.99 6) List all films' title and length in minutes. Alias length as "Duration (min)". cmd: SELECT title, length AS "Duration (min)" FROM film; SAMPLE OP: title | Duration (min) -----------------------------+---------------- Chamber Italian | 117 Grosse Wonderful | 49 Airport Pollock | 54 Bright Encounters | 73 Academy Dinosaur | 86 Ace Goldfinger | 48 Adaptation Holes | 50 Affair Prejudice | 117 7) Retrieve customer first an…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/s_a_r_a/select-queries-from-dvd-rental-database-1m51

## Related notes
- [[2026-03-24-select-queries-from-dvd-rental-database-pt-3]]
- [[2026-03-04-sql-cheatsheet]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-02-database-indexing-explained-how-to-make-your-queries-1000x-faster]]
- [[2026-03-10-sql-joins-and-window-functions]]
- [[2026-02-24-countcolumn-vs-count-in-sql-with-inner-left-right-full-join-explained]]
