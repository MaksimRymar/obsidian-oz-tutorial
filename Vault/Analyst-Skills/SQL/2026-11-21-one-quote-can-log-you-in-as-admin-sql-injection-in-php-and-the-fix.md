---
title: 'One Quote Can Log You In as Admin: SQL Injection in PHP (and the Fix)'
date: '2026-11-21'
source: https://dev.to/refactorly/one-quote-can-log-you-in-as-admin-sql-injection-in-php-and-the-fix-2jpc
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#support-analytics'
related:
- '[[2026-04-03-prepared-statements-in-manticore-search]]'
- '[[2026-11-11-python-just-got-a-new-kind-of-string-it-could-end-a-whole-class-of-security-bugs]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-04-13-typescript-knows-your-sql-is-broken-before-your-tests-even-run]]'
- '[[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]'
- '[[2026-05-29-part-13-sql-injection-and-staying-safe]]'
status: unread
---

> **TL;DR:** One quote character in a login form can log an attacker in as your admin, without the password. In this post I build a vulnerable PHP login, attack my own local test database with two classic payloads, and then fix it pr…

## What’s new and why it matters
One quote character in a login form can log an attacker in as your admin, without the password. In this post I build a vulnerable PHP login, attack my own local test database with two classic payloads, and then fix it properly. Everything below was run on PHP 8.1 with PDO and an in-memory SQLite database. Only test this on code and data you own. Video version: Spot the bug $email = $_POST [ 'email' ] ; $password = $_POST [ 'password' ] ; $sql = "SELECT * FROM users WHERE email = '$email' AND password = '$password'" ; $user = $pdo -> query ( $sql ) -> fetch ( ) ; if ( $user ) { login ( $user )…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/refactorly/one-quote-can-log-you-in-as-admin-sql-injection-in-php-and-the-fix-2jpc

## Related notes
- [[2026-04-03-prepared-statements-in-manticore-search]]
- [[2026-11-11-python-just-got-a-new-kind-of-string-it-could-end-a-whole-class-of-security-bugs]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-04-13-typescript-knows-your-sql-is-broken-before-your-tests-even-run]]
- [[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]
- [[2026-05-29-part-13-sql-injection-and-staying-safe]]
