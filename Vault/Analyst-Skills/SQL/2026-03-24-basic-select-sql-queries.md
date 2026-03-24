---
title: basic select sql queries
date: '2026-03-24'
source: https://dev.to/sharmi_sabari_09/basic-select-sql-queries-34a0
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-03-09-the-sql-query-that-ruined-my-weekend-and-what-i-built-to-prevent-it]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]'
- '[[2026-03-05-joins-and-window-functions-in-sql]]'
- '[[2026-03-06-joins-and-window-functions-ultimate-sql-playbook]]'
- '[[2026-03-08-sql-queries-asked-in-interview]]'
status: unread
---

> **TL;DR:** Query all columns for a city in CITY with the ID 1661 select * From city where id=1661; Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.…

## What’s new and why it matters
Query all columns for a city in CITY with the ID 1661 select * From city where id=1661; Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA. Select * From city where COUNTRYCODE = 'USA' and population > 100000; Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN. select * from city where countrycode = 'JPN'; Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table. select count(city) - count(distinct ci…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sharmi_sabari_09/basic-select-sql-queries-34a0

## Related notes
- [[2026-03-09-the-sql-query-that-ruined-my-weekend-and-what-i-built-to-prevent-it]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]
- [[2026-03-05-joins-and-window-functions-in-sql]]
- [[2026-03-06-joins-and-window-functions-ultimate-sql-playbook]]
- [[2026-03-08-sql-queries-asked-in-interview]]
