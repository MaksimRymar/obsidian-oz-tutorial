---
title: Your django-haystack Whoosh backend breaks on Python 3.13 — here's the one-line
  fix
date: '2026-08-22'
source: https://dev.to/priyasundaram/your-django-haystack-whoosh-backend-breaks-on-python-313-heres-the-one-line-fix-7gg
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]'
- '[[2026-04-28-fix-python-imports-in-jupyter-notebooks]]'
- '[[2026-04-13-python-314-free-threading-real-benchmarks-real-breakage-real-code]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
status: unread
---

> **TL;DR:** TL;DR: The Whoosh package Haystack installs is from 2016 and calls cgi.escape . The cgi module was removed in Python 3.13 , so highlighting (and sometimes import) blows up. Swap in the maintained fork: pip install django…

## What’s new and why it matters
TL;DR: The Whoosh package Haystack installs is from 2016 and calls cgi.escape . The cgi module was removed in Python 3.13 , so highlighting (and sometimes import) blows up. Swap in the maintained fork: pip install django-haystack whoosh3 — no code changes. Tested end-to-end on Haystack 3.4.0 + Django 6.1. If you run a Django site with django-haystack and the Whoosh backend, upgrading to Python 3.13 can hand you a surprise: ModuleNotFoundError: No module named 'cgi' It doesn't happen on import . It happens later — usually when Haystack renders a highlighted search result — which makes it extra…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/priyasundaram/your-django-haystack-whoosh-backend-breaks-on-python-313-heres-the-one-line-fix-7gg

## Related notes
- [[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]
- [[2026-04-28-fix-python-imports-in-jupyter-notebooks]]
- [[2026-04-13-python-314-free-threading-real-benchmarks-real-breakage-real-code]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
