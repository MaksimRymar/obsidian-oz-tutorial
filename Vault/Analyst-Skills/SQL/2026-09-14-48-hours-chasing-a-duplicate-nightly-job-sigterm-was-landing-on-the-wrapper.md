---
title: '48 Hours Chasing a Duplicate Nightly Job: SIGTERM Was Landing on the Wrapper'
date: '2026-09-14'
source: https://dev.to/codepy_1473/48-hours-chasing-a-duplicate-nightly-job-sigterm-was-landing-on-the-wrapper-c2b
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-20-build-a-50-line-harness-to-test-whether-a-free-model-endpoint-can-fix-broken-json]]'
- '[[2026-08-19-i-ran-a-nightly-ai-digest-on-free-infrastructure-for-a-week]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-08-15-learn-to-budget-a-free-model-tier-by-building-a-tiny-token-ledger]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
status: unread
---

> **TL;DR:** Two consumers were draining the same queue, and neither of them knew the other existed. My nightly job usually takes eleven minutes, so when the metrics showed the same batch processed twice, I assumed the queue had dupl…

## What’s new and why it matters
Two consumers were draining the same queue, and neither of them knew the other existed. My nightly job usually takes eleven minutes, so when the metrics showed the same batch processed twice, I assumed the queue had duplicate messages. It took 48 hours to accept that my deploy script had been killing the wrong process for months. This is a field note, not a tutorial about signal theory. I want to show you what I tried, what actually broke, and which parts of the workflow I would repeat tomorrow. The symptom: double processing after every deploy The duplicate always appeared within fifteen minu…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/codepy_1473/48-hours-chasing-a-duplicate-nightly-job-sigterm-was-landing-on-the-wrapper-c2b

## Related notes
- [[2026-08-20-build-a-50-line-harness-to-test-whether-a-free-model-endpoint-can-fix-broken-json]]
- [[2026-08-19-i-ran-a-nightly-ai-digest-on-free-infrastructure-for-a-week]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-08-15-learn-to-budget-a-free-model-tier-by-building-a-tiny-token-ledger]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
