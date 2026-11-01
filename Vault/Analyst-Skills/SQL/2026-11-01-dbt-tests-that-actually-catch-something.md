---
title: dbt tests that actually catch something
date: '2026-11-01'
source: https://dev.to/mira_lund/dbt-tests-that-actually-catch-something-4pc1
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
related:
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-09-07-bloom-filters-for-data-engineers-cheap-membership-tests]]'
- '[[2026-03-11-what-is-snowflake-a-beginners-guide-to-the-cloud-data-warehouse-everyones-talking-about]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-08-13-i-tried-to-stop-paying-299-per-backing-track-the-transcription-worked-the-accompaniment-never-did]]'
status: unread
---

> **TL;DR:** Most dbt test suites I've seen are a wall of not_null checks that pass forever. The useful ones are a handful of tests that fail when the data changes shape. My short list: uniqueness on the grain. If a model is one row…

## What’s new and why it matters
Most dbt test suites I've seen are a wall of not_null checks that pass forever. The useful ones are a handful of tests that fail when the data changes shape. My short list: uniqueness on the grain. If a model is one row per order, test that. When it fails, you have a fan-out join. relationships on foreign keys. Cheap, and they catch the missing row before the dashboard does. freshness on sources. A stale source that nobody notices is worse than a failed pipeline. one singular test per business rule. "Refund amount must be ≤ original amount" is worth more than 40 not_null checks. The pattern: t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mira_lund/dbt-tests-that-actually-catch-something-4pc1

## Related notes
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-09-07-bloom-filters-for-data-engineers-cheap-membership-tests]]
- [[2026-03-11-what-is-snowflake-a-beginners-guide-to-the-cloud-data-warehouse-everyones-talking-about]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-08-13-i-tried-to-stop-paying-299-per-backing-track-the-transcription-worked-the-accompaniment-never-did]]
