---
title: Why my dashboard tool checks its own numbers (and why I wrote it in Rust)
date: '2026-11-11'
source: https://dev.to/refaeldakar/why-my-dashboard-tool-checks-its-own-numbers-and-why-i-wrote-it-in-rust-3ecm
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-09-28-your-dashboard-is-green-and-the-number-is-wrong-the-sql-checks-i-schedule-next-to-every-metric]]'
- '[[2026-09-24-sql-database-projects-and-ai-a-match-made-in-heaven]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]'
- '[[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]'
- '[[2026-10-13-snowflake-sql-patterns-for-revenue-reporting]]'
status: unread
---

> **TL;DR:** I build arcodash, so read this with that in mind. It's an open-source dashboard tool (AGPL-3.0), v0.1.0 went out on Nov 8, and it's early beta. The thing that made me start: a dashboard that's wrong because a table quiet…

## What’s new and why it matters
I build arcodash, so read this with that in mind. It's an open-source dashboard tool (AGPL-3.0), v0.1.0 went out on Nov 8, and it's early beta. The thing that made me start: a dashboard that's wrong because a table quietly stopped loading. Nothing errors. The chart renders, the number looks plausible, and you find out when someone asks why Tuesday looks odd. The tool that draws the chart and the tool that watches the data are usually two different tools, set up by two different people, with two different schedules. So the watching tends to lag behind the drawing, or never gets set up. What I d…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/refaeldakar/why-my-dashboard-tool-checks-its-own-numbers-and-why-i-wrote-it-in-rust-3ecm

## Related notes
- [[2026-09-28-your-dashboard-is-green-and-the-number-is-wrong-the-sql-checks-i-schedule-next-to-every-metric]]
- [[2026-09-24-sql-database-projects-and-ai-a-match-made-in-heaven]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]
- [[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]
- [[2026-10-13-snowflake-sql-patterns-for-revenue-reporting]]
