---
title: The same SEC filing has two acceptance times, depending on which EDGAR file
  you read
date: '2026-10-12'
source: https://dev.to/arhancanli/the-same-sec-filing-has-two-acceptance-times-depending-on-which-edgar-file-you-read-371
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-09-14-agents-for-humans-an-agent-that-refuses-to-guess-what-your-letter-says]]'
- '[[2026-09-28-i-built-an-api-that-checks-whether-sec-financial-data-adds-up]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]'
status: unread
---

> **TL;DR:** If you pull filings from SEC's submissions API ( data.sec.gov/submissions/CIK##########.json ), each one comes with an acceptanceDateTime like 2026-07-14T14:30:38.000Z . The Z says UTC. For a large share of companies tha…

## What’s new and why it matters
If you pull filings from SEC's submissions API ( data.sec.gov/submissions/CIK##########.json ), each one comes with an acceptanceDateTime like 2026-07-14T14:30:38.000Z . The Z says UTC. For a large share of companies that is not true, and which companies depends on the file you read, not on the filing. That matters whenever the time of day matters: whether results came out before the open or after the close, which trading day an insider purchase belongs to, or an event study's day 0. What I measured On 2026-10-11 I took 25 companies' submissions files: the 12 newest filings in each, plus 6 fro…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/arhancanli/the-same-sec-filing-has-two-acceptance-times-depending-on-which-edgar-file-you-read-371

## Related notes
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-09-14-agents-for-humans-an-agent-that-refuses-to-guess-what-your-letter-says]]
- [[2026-09-28-i-built-an-api-that-checks-whether-sec-financial-data-adds-up]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]
