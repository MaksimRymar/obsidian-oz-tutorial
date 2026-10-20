---
title: 'Python Lazy Imports: How the New lazy Keyword Works in Python 3.15'
date: '2026-10-20'
source: https://dev.to/mfaysaldev/python-lazy-imports-how-the-new-lazy-keyword-works-in-python-315-4poh
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]'
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
status: unread
---

> **TL;DR:** Python 3.15 adds explicit lazy imports: write lazy import json (or lazy from pathlib import Path ) and Python won’t load the module until your code first uses that name. You keep all your imports neatly at the top of the…

## What’s new and why it matters
Python 3.15 adds explicit lazy imports: write lazy import json (or lazy from pathlib import Path ) and Python won’t load the module until your code first uses that name. You keep all your imports neatly at the top of the file, but you only pay the loading cost for modules a particular run actually needs. In my test, a script that imported a slow module started in 0.50 seconds with a normal import and 0.00 seconds with lazy import , and the module loaded later, only when it was called. Lazy imports come from PEP 810 and are one of the biggest changes in Python 3.15.0, released on 9 October 2026…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/mfaysaldev/python-lazy-imports-how-the-new-lazy-keyword-works-in-python-315-4poh

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
