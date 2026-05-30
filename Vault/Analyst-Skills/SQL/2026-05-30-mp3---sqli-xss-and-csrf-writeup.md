---
title: MP3 - SQLi, XSS, and CSRF WriteUp
date: '2026-05-30'
source: https://dev.to/acchanli/mp3-sqli-xss-and-csrf-writeup-2npd
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]'
- '[[2026-05-29-part-13-sql-injection-and-staying-safe]]'
- '[[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-04-03-prepared-statements-in-manticore-search]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
status: unread
---

> **TL;DR:** Introduction For Machine Problem 3, our group — Aki, Lark, and Carl — was tasked with finding and fixing security vulnerabilities in a sample web application written in Python (Flask) with sqlite3 as its database. The ap…

## What’s new and why it matters
Introduction For Machine Problem 3, our group — Aki, Lark, and Carl — was tasked with finding and fixing security vulnerabilities in a sample web application written in Python (Flask) with sqlite3 as its database. The application has a login page and a posts page where users can view and create their own posts. Our scope was limited to SQL injection, CSRF, and XSS, though we also fixed related issues we came across. Going through the code, we found seven SQL injection vulnerabilities, two CSRF vulnerabilities, and one XSS vulnerability. Each one is documented below along with the fix we applie…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/acchanli/mp3-sqli-xss-and-csrf-writeup-2npd

## Related notes
- [[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]
- [[2026-05-29-part-13-sql-injection-and-staying-safe]]
- [[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-04-03-prepared-statements-in-manticore-search]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
