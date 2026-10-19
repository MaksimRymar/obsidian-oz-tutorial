---
title: I Built a Frozen-Scan Detector. A Week Later It Fires Daily — and Nothing Consumes
  It
date: '2026-10-19'
source: https://dev.to/felixwang007/i-built-a-frozen-scan-detector-a-week-later-it-fires-daily-and-nothing-consumes-it-31fe
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-17-i-added-a-fourth-shard-in-python-and-75-of-the-keys-moved]]'
- '[[2026-08-31-a-passing-check-is-a-claim-about-what-ran-not-whats-true]]'
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]'
- '[[2026-08-20-build-a-50-line-harness-to-test-whether-a-free-model-endpoint-can-fix-broken-json]]'
- '[[2026-08-10-my-fix-commit-cited-a-bugsmd-entry-that-didnt-exist-yet]]'
status: unread
---

> **TL;DR:** This is the verdict my detector printed ten minutes ago, verbatim: $ python tools/scanfresh/scan_freshness_guard.py check \ --ledger recommendations/signal_history.jsonl \ --verify recommendations/signal_verify_log.jsonl…

## What’s new and why it matters
This is the verdict my detector printed ten minutes ago, verbatim: $ python tools/scanfresh/scan_freshness_guard.py check \ --ledger recommendations/signal_history.jsonl \ --verify recommendations/signal_verify_log.jsonl \ --panel-dir history_ext --today 2026-10-19 verdict: FROZEN ! panel newest bar 2026-09-28 is 15 business days behind 2026-10-19 ! trailing identical run of 15 entries ( 2026-09-28 -> 2026-10-16, fp = 4c29e76725 ) ! 2 verification transition ( s ) advanced target_date without changing any measured detail Exit code 2 . Three numbers: 15 consecutive sessions whose ledger entries…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/felixwang007/i-built-a-frozen-scan-detector-a-week-later-it-fires-daily-and-nothing-consumes-it-31fe

## Related notes
- [[2026-10-17-i-added-a-fourth-shard-in-python-and-75-of-the-keys-moved]]
- [[2026-08-31-a-passing-check-is-a-claim-about-what-ran-not-whats-true]]
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]
- [[2026-08-20-build-a-50-line-harness-to-test-whether-a-free-model-endpoint-can-fix-broken-json]]
- [[2026-08-10-my-fix-commit-cited-a-bugsmd-entry-that-didnt-exist-yet]]
