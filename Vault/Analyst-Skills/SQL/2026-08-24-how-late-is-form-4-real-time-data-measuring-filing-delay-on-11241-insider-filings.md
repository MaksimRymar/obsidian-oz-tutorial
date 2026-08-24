---
title: How late is Form 4 'real-time' data? Measuring filing delay on 11,241 insider
  filings
date: '2026-08-24'
source: https://dev.to/itsraxzey/how-late-is-form-4-real-time-data-measuring-filing-delay-on-11241-insider-filings-2e9j
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-04-11-7-free-defi-apis-every-developer-should-know-in-2026-with-code-examples]]'
- '[[2026-03-15-i-built-an-ai-that-trades-crypto-and-options-automatically-here-are-the-real-pl-numbers]]'
- '[[2026-05-05-top-50-sql-interview-questions-with-answers-2026]]'
- '[[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]'
status: unread
---

> **TL;DR:** If you backtest anything involving insider trades, there's a quiet bug waiting for you: Form 4 data is timestamped twice . Every filing carries a transaction date (when the insider actually traded) and a filing date (whe…

## What’s new and why it matters
If you backtest anything involving insider trades, there's a quiet bug waiting for you: Form 4 data is timestamped twice . Every filing carries a transaction date (when the insider actually traded) and a filing date (when EDGAR disseminated the form). If your backtest joins on the transaction date, you're trading on information that did not exist yet. How big is that gap in practice? I measured it for every Form 4 filed in July 2026 — 11,241 filings — and the answer is: usually 2 days, sometimes 8 years. (Disclosure up front: I run FilingPulse , the SEC filings API this study is built on. This…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/itsraxzey/how-late-is-form-4-real-time-data-measuring-filing-delay-on-11241-insider-filings-2e9j

## Related notes
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-04-11-7-free-defi-apis-every-developer-should-know-in-2026-with-code-examples]]
- [[2026-03-15-i-built-an-ai-that-trades-crypto-and-options-automatically-here-are-the-real-pl-numbers]]
- [[2026-05-05-top-50-sql-interview-questions-with-answers-2026]]
- [[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]
