---
title: How I Built a Python Compiler That Runs in Your Browser, With Real input()
date: '2026-11-12'
source: https://dev.to/durim255/how-i-built-a-python-compiler-that-runs-in-your-browser-with-real-input-kj0
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
- '[[2026-11-06-generic-sql-formatters-dont-know-postgresql-and-it-shows-tags-postgres-sql-tooling-webdev]]'
- '[[2026-10-15-see-every-google-ad-a-competitor-runs-from-just-their-domain-curl-python-n8n]]'
- '[[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]'
- '[[2026-04-19-build-your-own-types-classes-explained-simply]]'
- '[[2026-10-29-ef-core-isnt-slow-these-5-query-patterns-are]]'
status: unread
---

> **TL;DR:** Originally published on Medium . I'm Durim, and I build HTML Suite , a set of free developer tools that run entirely in the browser: an HTML editor, JSON and YAML formatters, converters and a Python online compiler . The…

## What’s new and why it matters
Originally published on Medium . I'm Durim, and I build HTML Suite , a set of free developer tools that run entirely in the browser: an HTML editor, JSON and YAML formatters, converters and a Python online compiler . The Python compiler runs real Python 3.13 on your own device using Pyodide (CPython compiled to WebAssembly). No server executes your code, nothing is uploaded, and you don't need an account. That part was surprisingly easy. The hard part was one tiny built-in function: input() . Why input() breaks in the browser In normal Python, input() simply pauses the program until you type a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/durim255/how-i-built-a-python-compiler-that-runs-in-your-browser-with-real-input-kj0

## Related notes
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
- [[2026-11-06-generic-sql-formatters-dont-know-postgresql-and-it-shows-tags-postgres-sql-tooling-webdev]]
- [[2026-10-15-see-every-google-ad-a-competitor-runs-from-just-their-domain-curl-python-n8n]]
- [[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]
- [[2026-04-19-build-your-own-types-classes-explained-simply]]
- [[2026-10-29-ef-core-isnt-slow-these-5-query-patterns-are]]
