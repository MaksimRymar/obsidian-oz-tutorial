---
title: If a list endpoint returns exactly as many rows as you asked for, you have
  a bug
date: '2026-09-25'
source: https://dev.to/frankchu/if-a-list-endpoint-returns-exactly-as-many-rows-as-you-asked-for-you-have-a-bug-21kb
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-07-my-comment-reply-script-asked-devto-for-my-articles-leaving-off-one-query-param-silently-dropped-the-newest-two]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
- '[[2026-08-13-i-tried-to-stop-paying-299-per-backing-track-the-transcription-worked-the-accompaniment-never-did]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-09-10-openai-compatible-is-a-spectrum-not-a-boolean-heres-an-11-check-conformance-suite]]'
status: unread
---

> **TL;DR:** A reader ran the numbers in one of my posts against the live API and told me they did not add up. He was right, and the tell had been sitting in my own published output for a week. 60 posts | 690 views | 3 reactions Sixt…

## What’s new and why it matters
A reader ran the numbers in one of my posts against the live API and told me they did not add up. He was right, and the tell had been sitting in my own published output for a week. 60 posts | 690 views | 3 reactions Sixty. I had asked for sixty. mine = get ( " https://dev.to/api/articles/me/published?per_page=60 " , auth = True ) per_page is a page size, not a limit. My call took the first page and stopped, because I never wrote the loop. The quality scan earlier in that same post walked the filesystem and counted 68 files. So I compared a 68-item population against a 60-item population and pr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/frankchu/if-a-list-endpoint-returns-exactly-as-many-rows-as-you-asked-for-you-have-a-bug-21kb

## Related notes
- [[2026-08-07-my-comment-reply-script-asked-devto-for-my-articles-leaving-off-one-query-param-silently-dropped-the-newest-two]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
- [[2026-08-13-i-tried-to-stop-paying-299-per-backing-track-the-transcription-worked-the-accompaniment-never-did]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-09-10-openai-compatible-is-a-spectrum-not-a-boolean-heres-an-11-check-conformance-suite]]
