---
title: 'Julian Date Conversion in Code: YYDDD, CYYDDD, JD and MJD in Python, JavaScript,
  SQL and Excel'
date: '2026-10-21'
source: https://dev.to/ordinaldates/julian-date-conversion-in-code-yyddd-cyyddd-jd-and-mjd-in-python-javascript-sql-and-excel-29lm
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-03-pandas-secret-mini-language]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-30-your-ai-does-not-know-what-today-means]]'
- '[[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]'
status: unread
---

> **TL;DR:** "Julian date" means two different things, and both show up in real code. A batch code on a food carton, a mainframe file or a JD Edwards table usually means an ordinal date : the year plus the day of the year ( 26294 = d…

## What’s new and why it matters
"Julian date" means two different things, and both show up in real code. A batch code on a food carton, a mainframe file or a JD Edwards table usually means an ordinal date : the year plus the day of the year ( 26294 = day 294 of 2026 = October 21, 2026). An astronomer, a satellite pass predictor or a FITS header means the Julian Date (JD) : a continuous count of days since noon UTC on January 1, 4713 BC in the proleptic Julian calendar ( 2461334.5 = 00:00 UTC on October 21, 2026). Mixing the two up is a common source of bugs. This post collects the conversions for both, with a worked example…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ordinaldates/julian-date-conversion-in-code-yyddd-cyyddd-jd-and-mjd-in-python-javascript-sql-and-excel-29lm

## Related notes
- [[2026-05-03-pandas-secret-mini-language]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-30-your-ai-does-not-know-what-today-means]]
- [[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]
