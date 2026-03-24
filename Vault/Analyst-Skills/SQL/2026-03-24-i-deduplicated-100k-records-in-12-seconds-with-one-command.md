---
title: I Deduplicated 100K Records in 12 Seconds With One Command
date: '2026-03-24'
source: https://dev.to/benzsevern/i-deduplicated-100k-records-in-12-seconds-with-one-command-5a98
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-24-two-hospitals-matched-patient-records-without-sharing-a-single-name]]'
- '[[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]'
- '[[2026-03-01-sql-joins]]'
- '[[2026-03-24-stop-manual-prospecting-how-a-3-actor-pipeline-finds-and-scores-b2b-leads]]'
- '[[2026-03-16-i-wasted-200-hours-parsing-client-csvs-so-i-built-a-library-that-does-it-in-one-line]]'
- '[[2026-03-12-my-first-public-project-on-python]]'
status: unread
---

> **TL;DR:** My CSV had duplicates. A lot of them. "John Smith" and "Jon Smith" were the same person. So were " john.smith@gmail.com " and " jsmith@gmail.com ." And "(555) 012-3456" and "5550123456." I didn't want to write 60 lines o…

## What’s new and why it matters
My CSV had duplicates. A lot of them. "John Smith" and "Jon Smith" were the same person. So were " john.smith@gmail.com " and " jsmith@gmail.com ." And "(555) 012-3456" and "5550123456." I didn't want to write 60 lines of Python to find them. So I built a tool that does it in one command. pip install goldenmatch goldenmatch dedupe customers.csv That's it. No config file. No training data. No manual labeling. GoldenMatch reads your CSV, figures out which columns are names, emails, phones, and addresses, picks the best matching algorithm for each, and clusters the duplicates. On 100,000 records,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/benzsevern/i-deduplicated-100k-records-in-12-seconds-with-one-command-5a98

## Related notes
- [[2026-03-24-two-hospitals-matched-patient-records-without-sharing-a-single-name]]
- [[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]
- [[2026-03-01-sql-joins]]
- [[2026-03-24-stop-manual-prospecting-how-a-3-actor-pipeline-finds-and-scores-b2b-leads]]
- [[2026-03-16-i-wasted-200-hours-parsing-client-csvs-so-i-built-a-library-that-does-it-in-one-line]]
- [[2026-03-12-my-first-public-project-on-python]]
