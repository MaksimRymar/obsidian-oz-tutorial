---
title: 'MariaDB 12 Broke Our Concurrent Updates: Debugging ERROR 1020 After an Upgrade'
date: '2026-09-12'
source: https://dev.to/dkelxldk/mariadb-12-broke-our-concurrent-updates-debugging-error-1020-after-an-upgrade-56di
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-08-22-optimistic-and-pessimistic-locking-in-net-with-sql-server]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-08-17-a-finished-scraper-sat-on-a-git-branch-for-19-days-nothing-noticed]]'
- '[[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]'
- '[[2026-04-20-the-hidden-cost-of-aws-lambda-snapstart-for-python-and-how-i-fixed-it-with-durable-functions]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
status: unread
---

> **TL;DR:** We recently deployed a new environment using MariaDB 12.3 , while our older environments were still running MariaDB 10.11. Soon after deployment, some concurrent UPDATE operations started failing with: ERROR 1020 (HY000)…

## What’s new and why it matters
We recently deployed a new environment using MariaDB 12.3 , while our older environments were still running MariaDB 10.11. Soon after deployment, some concurrent UPDATE operations started failing with: ERROR 1020 (HY000): Record has changed since last read in table The interesting part: the same application logic had been running fine on MariaDB 10.11. Finding the Difference After comparing both environments, we found this: Environment MariaDB innodb_snapshot_isolation Existing 10.11.x OFF New 12.3.x ON You can check it with: SHOW VARIABLES LIKE 'innodb_snapshot_isolation' ; MariaDB changed th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/dkelxldk/mariadb-12-broke-our-concurrent-updates-debugging-error-1020-after-an-upgrade-56di

## Related notes
- [[2026-08-22-optimistic-and-pessimistic-locking-in-net-with-sql-server]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-08-17-a-finished-scraper-sat-on-a-git-branch-for-19-days-nothing-noticed]]
- [[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]
- [[2026-04-20-the-hidden-cost-of-aws-lambda-snapstart-for-python-and-how-i-fixed-it-with-durable-functions]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
