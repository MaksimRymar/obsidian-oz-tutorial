---
title: Isolation
date: '2026-03-25'
source: https://dev.to/arul_selviml_7/isolation-1npn
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-03-04-the-two-sql-concepts-that-made-me-finally-understand-real-data-joins-window-functions]]'
- '[[2026-03-07-why-i-rebuilt-my-first-api-from-scratch]]'
- '[[2026-03-24-guarding-critical-operations-mastering-select-for-update-for-race-condition-prevention-in-django-postgresql]]'
- '[[2026-03-24-stop-tuning-blind-query-observability-as-the-foundation-for-database-optimization]]'
- '[[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]'
status: unread
---

> **TL;DR:** Today I tried to understand how isolation works in a database by simulating multiple users using the same account at the same time. This is very important for applications like PhonePe or GPay because many users can perf…

## What’s new and why it matters
Today I tried to understand how isolation works in a database by simulating multiple users using the same account at the same time. This is very important for applications like PhonePe or GPay because many users can perform transactions at once. I used the same accounts table where Alice has 1000 balance. Then I opened two database sessions to act like two different users. In the first session, I started a transaction and deducted money from Alice’s account but did not commit it. BEGIN; UPDATE accounts SET balance = balance - 700 WHERE name = 'Alice'; At this point, the balance is reduced insi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/arul_selviml_7/isolation-1npn

## Related notes
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-03-04-the-two-sql-concepts-that-made-me-finally-understand-real-data-joins-window-functions]]
- [[2026-03-07-why-i-rebuilt-my-first-api-from-scratch]]
- [[2026-03-24-guarding-critical-operations-mastering-select-for-update-for-race-condition-prevention-in-django-postgresql]]
- [[2026-03-24-stop-tuning-blind-query-observability-as-the-foundation-for-database-optimization]]
- [[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]
