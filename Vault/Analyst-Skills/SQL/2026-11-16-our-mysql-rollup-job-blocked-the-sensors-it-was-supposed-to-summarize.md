---
title: Our MySQL rollup job blocked the sensors it was supposed to summarize
date: '2026-11-16'
source: https://dev.to/solutionmarket/our-mysql-rollup-job-blocked-the-sensors-it-was-supposed-to-summarize-2fe3
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-10-25-pagination-that-skips-rows-is-an-off-by-one-in-the-data-model]]'
- '[[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]'
- '[[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]'
- '[[2026-09-19-a-nullable-column-cost-me-five-years-of-branches]]'
- '[[2026-09-30-a-select-that-returned-more-rows-than-its-limit]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
status: unread
---

> **TL;DR:** InfraGuard Engineering Devlog, part 6 of 6. On November 12, five commits went into InfraGuard's rollup worker. Retention cleanup was not completing, a drain path had replayed data, and the worker blocked sensor inserts.…

## What’s new and why it matters
InfraGuard Engineering Devlog, part 6 of 6. On November 12, five commits went into InfraGuard's rollup worker. Retention cleanup was not completing, a drain path had replayed data, and the worker blocked sensor inserts. The common theme was a mismatch between database work and process lifetime. A minute-long process, a seven-minute workflow PM2 restarted the worker every minute. Database statements could outlive the client, while subsequent script steps never ran. One drain operation aggregated a detached traffic copy in a statement taking about seven minutes. MySQL could commit that statement…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/solutionmarket/our-mysql-rollup-job-blocked-the-sensors-it-was-supposed-to-summarize-2fe3

## Related notes
- [[2026-10-25-pagination-that-skips-rows-is-an-off-by-one-in-the-data-model]]
- [[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]
- [[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]
- [[2026-09-19-a-nullable-column-cost-me-five-years-of-branches]]
- [[2026-09-30-a-select-that-returned-more-rows-than-its-limit]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
