---
title: PostgreSQL Had 200 GB of Free Disk. One Table Still Stopped Accepting Writes
date: '2026-11-13'
source: https://medium.com/engineering-playbook/postgresql-had-200-gb-of-free-disk-one-table-still-stopped-accepting-writes-e1b549f33cb5?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
related:
- '[[2026-10-26-the-postgresql-decision-i-defended-for-years-became-our-biggest-scaling-problem]]'
- '[[2026-11-08-the-postgresql-query-took-11-seconds-the-database-wasnt-the-problem]]'
- '[[2026-11-04-postgresql-vs-mongodb-we-built-the-same-backend-twice-one-design-failed-under-load]]'
- '[[2026-11-13-we-deployed-one-new-column-postgresql-froze-27-application-pods]]'
- '[[2026-10-31-a-senior-backend-engineer-asked-for-180k-one-postgresql-question-changed-the-interview]]'
- '[[2026-10-02-our-database-wasnt-slow-one-select-was-quietly-costing-us-4800-a-month]]'
status: unread
---

> **TL;DR:** The API was timing out, database CPU looked normal, and storage wasn’t full. The problem was hiding inside PostgreSQL’s transaction ID… Continue reading on Engineering Under Pressure »

## What’s new and why it matters
The API was timing out, database CPU looked normal, and storage wasn’t full. The problem was hiding inside PostgreSQL’s transaction ID… Continue reading on Engineering Under Pressure »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/engineering-playbook/postgresql-had-200-gb-of-free-disk-one-table-still-stopped-accepting-writes-e1b549f33cb5?source=rss------sql-5

## Related notes
- [[2026-10-26-the-postgresql-decision-i-defended-for-years-became-our-biggest-scaling-problem]]
- [[2026-11-08-the-postgresql-query-took-11-seconds-the-database-wasnt-the-problem]]
- [[2026-11-04-postgresql-vs-mongodb-we-built-the-same-backend-twice-one-design-failed-under-load]]
- [[2026-11-13-we-deployed-one-new-column-postgresql-froze-27-application-pods]]
- [[2026-10-31-a-senior-backend-engineer-asked-for-180k-one-postgresql-question-changed-the-interview]]
- [[2026-10-02-our-database-wasnt-slow-one-select-was-quietly-costing-us-4800-a-month]]
