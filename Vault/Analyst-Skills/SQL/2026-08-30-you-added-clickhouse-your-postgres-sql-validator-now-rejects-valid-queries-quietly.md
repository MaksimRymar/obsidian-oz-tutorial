---
title: You added ClickHouse. Your Postgres SQL validator now rejects valid queries
  — quietly.
date: '2026-08-30'
source: https://dev.to/omer_hochman/you-added-clickhouse-your-postgres-sql-validator-now-rejects-valid-queries-quietly-2okd
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
status: unread
---

> **TL;DR:** Originally published at nlqdb.com/blog We generate SQL from plain English, and before any of it touches a database we validate it. So when we added a second engine — ClickHouse alongside Postgres — the tempting move was…

## What’s new and why it matters
Originally published at nlqdb.com/blog We generate SQL from plain English, and before any of it touches a database we validate it. So when we added a second engine — ClickHouse alongside Postgres — the tempting move was obvious: reuse the validator we already trust. It ran clean, the tests were green, and a class of real user questions started coming back parse_failed for no reason anyone could see. The validator wasn't broken. It was doing exactly what it was told, on the wrong engine. One parser, pinned to one dialect Our validator is an AST parse — node-sql-parser , configured database: "Po…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/omer_hochman/you-added-clickhouse-your-postgres-sql-validator-now-rejects-valid-queries-quietly-2okd

## Related notes
- [[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
