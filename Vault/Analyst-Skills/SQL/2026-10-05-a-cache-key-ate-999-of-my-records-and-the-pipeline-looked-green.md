---
title: A cache key ate 99.9% of my records and the pipeline looked green
date: '2026-10-05'
source: https://dev.to/kyien/a-cache-key-ate-999-of-my-records-and-the-pipeline-looked-green-37i0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
- '[[2026-09-24-my-alert-fired-7-times-across-1963-pairs-i-assumed-the-thresholds-were-too-high-they-were-and-it-didnt-matter]]'
status: unread
---

> **TL;DR:** The worst pipeline bug I've shipped didn't throw. No stack trace, no failed job, no alert. Every run went green, finished inside its window, and wrote roughly one record out of every thousand it was handed. The job's own…

## What’s new and why it matters
The worst pipeline bug I've shipped didn't throw. No stack trace, no failed job, no alert. Every run went green, finished inside its window, and wrote roughly one record out of every thousand it was handed. The job's own metrics said it was healthy, because the job's own metrics counted runs, not rows. It took a business user asking why a campaign list looked short to surface it. This post is about that class of bug — the pipeline that succeeds at doing nothing — and the three habits that make it structurally impossible rather than merely unlikely. How you lose 99.9% of your data without notic…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kyien/a-cache-key-ate-999-of-my-records-and-the-pipeline-looked-green-37i0

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
- [[2026-09-24-my-alert-fired-7-times-across-1963-pairs-i-assumed-the-thresholds-were-too-high-they-were-and-it-didnt-matter]]
