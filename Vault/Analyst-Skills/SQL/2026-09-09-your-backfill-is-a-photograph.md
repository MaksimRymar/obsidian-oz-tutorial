---
title: Your backfill is a photograph
date: '2026-09-09'
source: https://dev.to/enderyentar/your-backfill-is-a-photograph-2kgj
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-28-how-to-actually-measure-whether-your-text-to-sql-is-any-good]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
status: unread
---

> **TL;DR:** We were getting ready to make a column NOT NULL . Standard preparation: count the rows that would violate it. The count was not zero. Seven API keys had no owning organization. That looked like a key problem, so we went…

## What’s new and why it matters
We were getting ready to make a column NOT NULL . Standard preparation: count the rows that would violate it. The count was not zero. Seven API keys had no owning organization. That looked like a key problem, so we went looking at how keys are created. It was not a key problem. The keys were innocent All seven belonged to the same account. And that account had no organization either. Widening the query, two accounts were in that state. Both had signed up recently, within the same three week window. That reframed the question. Keys read organization_id off the user who owns them. If the user ha…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enderyentar/your-backfill-is-a-photograph-2kgj

## Related notes
- [[2026-08-28-how-to-actually-measure-whether-your-text-to-sql-is-any-good]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
