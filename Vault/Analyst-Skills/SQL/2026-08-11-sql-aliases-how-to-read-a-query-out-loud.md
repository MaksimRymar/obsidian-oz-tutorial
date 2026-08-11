---
title: 'SQL Aliases: How to Read a Query Out Loud'
date: '2026-08-11'
source: https://dev.to/michaelnocito/sql-aliases-how-to-read-a-query-out-loud-2pgm
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tableau'
- '#tool'
- '#tutorial'
related:
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-07-28-why-schema-drift-goes-undetected]]'
- '[[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]'
- '[[2026-08-10-why-senior-data-engineers-write-sql-differently]]'
status: unread
---

> **TL;DR:** After this page you can read any query out loud and know what every name in it refers to. You will also name things the way a reviewer expects. That is most of what makes a query look like the work of someone who does th…

## What’s new and why it matters
After this page you can read any query out loud and know what every name in it refers to. You will also name things the way a reviewer expects. That is most of what makes a query look like the work of someone who does this for a living. Here is what you do. Give every calculated column a name with AS . Give every table a one-letter nickname once a query touches two of them. Then put that nickname in front of each column, so a reader never has to guess which table a column came from. Three habits, and they take about a minute to learn. The short version. An alias is a name you invent. AS on a c…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/michaelnocito/sql-aliases-how-to-read-a-query-out-loud-2pgm

## Related notes
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-07-28-why-schema-drift-goes-undetected]]
- [[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]
- [[2026-08-10-why-senior-data-engineers-write-sql-differently]]
