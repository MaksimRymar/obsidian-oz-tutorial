---
title: 'UPDATE without WHERE: what MySQL''s safe-updates mode stops, and what it lets
  through'
date: '2026-11-19'
source: https://dev.to/dudko-dev/update-without-where-what-mysqls-safe-updates-mode-stops-and-what-it-lets-through-2mf7
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]'
- '[[2026-10-29-isolation-levels-how-the-last-item-in-stock-gets-sold-twice]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-11-11-setting-up-postgresql-with-docker-psql-and-pgadmin]]'
status: unread
---

> **TL;DR:** MySQL error 1175 has its own Stack Overflow question with more than three million views, and most of its answers explain how to switch safe-updates mode off. That's a shame, because the mode does catch the classic accide…

## What’s new and why it matters
MySQL error 1175 has its own Stack Overflow question with more than three million views, and most of its answers explain how to switch safe-updates mode off. That's a shame, because the mode does catch the classic accident. It just doesn't catch all of it. And it blocks a fair amount of correct SQL, which is why people switch it off in the first place. So we ran 22 write statements ( UPDATE , DELETE , a CALL and a TRUNCATE ) against MySQL 8.4 and MariaDB 11.4 with sql_safe_updates = 1 , each one against a fresh 1000-row table, and counted what actually changed. The test One table: orders (id P…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dudko-dev/update-without-where-what-mysqls-safe-updates-mode-stops-and-what-it-lets-through-2mf7

## Related notes
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]
- [[2026-10-29-isolation-levels-how-the-last-item-in-stock-gets-sold-twice]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-11-11-setting-up-postgresql-with-docker-psql-and-pgadmin]]
