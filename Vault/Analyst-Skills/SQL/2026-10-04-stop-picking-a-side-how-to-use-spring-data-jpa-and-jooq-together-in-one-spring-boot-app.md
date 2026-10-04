---
title: 'Stop Picking a Side: How to Use Spring Data JPA and jOOQ Together in One Spring
  Boot App'
date: '2026-10-04'
source: https://dev.to/jamilxt/stop-picking-a-side-how-to-use-spring-data-jpa-and-jooq-together-in-one-spring-boot-app-4mi1
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#feature'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
status: unread
---

> **TL;DR:** Every few months the same argument flares up again: Spring Data JPA or jOOQ, which one should a Spring Boot app use? The debate is alive enough that Spring I/O 2026 ran it as a literal boxing match, a talk called "The Pe…

## What’s new and why it matters
Every few months the same argument flares up again: Spring Data JPA or jOOQ, which one should a Spring Boot app use? The debate is alive enough that Spring I/O 2026 ran it as a literal boxing match, a talk called "The Persistence Heavyweight Championship: JPA vs. jOOQ," with one speaker championing Hibernate and the other championing type-safe SQL while the audience judged the rounds. I think the framing is wrong. JPA and jOOQ are not two contenders for the same belt. One is an object-relational mapper that manages entity state for you. The other is a type-safe SQL query builder that generates…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jamilxt/stop-picking-a-side-how-to-use-spring-data-jpa-and-jooq-together-in-one-spring-boot-app-4mi1

## Related notes
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
