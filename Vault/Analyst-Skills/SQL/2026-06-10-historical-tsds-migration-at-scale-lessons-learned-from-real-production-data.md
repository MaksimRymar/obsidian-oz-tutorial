---
title: 'Historical TSDS Migration At Scale: Lessons Learned From Real Production Data'
date: '2026-06-10'
source: https://dev.to/naresh_007/historical-tsds-migration-at-scale-lessons-learned-from-real-production-data-2l8h
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
- '[[2026-04-17-understanding-sql-window-functions]]'
- '[[2026-04-21-i-spent-6-months-obsessing-over-mt5-bot-logic-heres-what-finally-clicked]]'
- '[[2026-05-22-the-dark-secret-of-scale-how-our-company-hit-a-tricky-problem-with-treasure-hunt-engine-at-10000-users]]'
status: unread
---

> **TL;DR:** TL;DR Historical TSDS migration is very different from normal TSDS ingestion. After multiple failed approaches, the process that worked was: Create the ILM policy (Hot → Warm → Cold → Frozen). Create a TSDS index templat…

## What’s new and why it matters
TL;DR Historical TSDS migration is very different from normal TSDS ingestion. After multiple failed approaches, the process that worked was: Create the ILM policy (Hot → Warm → Cold → Frozen). Create a TSDS index template with start_time and end_time. Create the data stream. Reindex historical data into the data stream. Remove the start_time and end_time constraints from the template. Monitor source and destination document counts. Once migration reaches ~98–99% completion, trigger rollover manually. Attach the ILM policy only after migration completes. Allow TSDS lifecycle management and down…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/naresh_007/historical-tsds-migration-at-scale-lessons-learned-from-real-production-data-2l8h

## Related notes
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
- [[2026-04-17-understanding-sql-window-functions]]
- [[2026-04-21-i-spent-6-months-obsessing-over-mt5-bot-logic-heres-what-finally-clicked]]
- [[2026-05-22-the-dark-secret-of-scale-how-our-company-hit-a-tricky-problem-with-treasure-hunt-engine-at-10000-users]]
