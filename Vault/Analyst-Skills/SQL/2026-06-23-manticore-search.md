---
title: Український лематизатор тепер вбудовано в Manticore Search
date: '2026-06-23'
source: https://dev.to/sanikolaev/ukrayinskii-liematizator-tiepier-vbudovano-v-manticore-search-5aoa
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
related:
- '[[2026-03-04-sql-cheatsheet]]'
- '[[2026-03-27-postgresql-has-a-free-relational-database-json-full-text-search-and-extensions]]'
- '[[2026-03-22-fetch-and-sort-leaderboard-by-difficulty-and-attempts]]'
- '[[2026-03-26-sqlite-can-do-more-than-you-think-full-text-search-json-window-functions-and-281tb-databases]]'
- '[[2026-05-13-understanding-sql-query-structure]]'
- '[[2026-04-03-prepared-statements-in-manticore-search]]'
status: unread
---

> **TL;DR:** Коротко починаючи з релізу 27.1.5 український лематизатор більше не потребує окремого Python-стека. Раніше потрібно було встановлювати окремий пакет, Python 3.9, pymorphy2 і українські словники. Гарна новина - тепер слов…

## What’s new and why it matters
Коротко починаючи з релізу 27.1.5 український лематизатор більше не потребує окремого Python-стека. Раніше потрібно було встановлювати окремий пакет, Python 3.9, pymorphy2 і українські словники. Гарна новина - тепер словник уже входить до Manticore. Достатньо лише ввімкнути явно морфологію: morphology = 'lemmatize_uk_all' Окремо додавати українські символи до charset_table також вже не потрібно: стандартний non_cont містить мапінги для є , і , ї , ґ . А от апостроф для української мови важливий, але тут є один важливий нюанс. Якщо просто додати його в charset_table це може зачепити данні на ан…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sanikolaev/ukrayinskii-liematizator-tiepier-vbudovano-v-manticore-search-5aoa

## Related notes
- [[2026-03-04-sql-cheatsheet]]
- [[2026-03-27-postgresql-has-a-free-relational-database-json-full-text-search-and-extensions]]
- [[2026-03-22-fetch-and-sort-leaderboard-by-difficulty-and-attempts]]
- [[2026-03-26-sqlite-can-do-more-than-you-think-full-text-search-json-window-functions-and-281tb-databases]]
- [[2026-05-13-understanding-sql-query-structure]]
- [[2026-04-03-prepared-statements-in-manticore-search]]
