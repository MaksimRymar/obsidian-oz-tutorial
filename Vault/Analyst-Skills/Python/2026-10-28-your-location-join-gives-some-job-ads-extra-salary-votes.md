---
title: Your location join gives some job ads extra salary votes
date: '2026-10-28'
source: https://dev.to/dataspryva/your-location-join-gives-some-job-ads-extra-salary-votes-34oe
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tableau'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-05-01-joins-combining-tables-without-losing-your-mind]]'
- '[[2026-10-24-your-salary-coverage-can-fall-before-employers-change]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
status: unread
---

> **TL;DR:** Your national salary average moved when you added regional rows. Now the market report needs an explanation for why a location transformation changed a pay statistic. The suspicious line is jobs.explode("locations") . Th…

## What’s new and why it matters
Your national salary average moved when you added regional rows. Now the market report needs an explanation for why a location transformation changed a pay statistic. The suspicious line is jobs.explode("locations") . The job location structure is a locations[] array of objects, so expanding it repeats any parent salary across its location associations. Exploding job locations changes the analytical unit from an advert to a job-location association. Calculate a national mean on those expanded rows and ads with more associations receive more weight. Keep the search population attached For Datas…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dataspryva/your-location-join-gives-some-job-ads-extra-salary-votes-34oe

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-05-01-joins-combining-tables-without-losing-your-mind]]
- [[2026-10-24-your-salary-coverage-can-fall-before-employers-change]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
