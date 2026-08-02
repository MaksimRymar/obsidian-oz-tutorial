---
title: My Favorite Constant in Retrieval Is 60. Nobody Tunes It. That's the Point.
date: '2026-08-02'
source: https://dev.to/fagundesv/my-favorite-constant-in-retrieval-is-60-nobody-tunes-it-thats-the-point-4857
domain: Productivity
relevance: 🟡
tags:
- '#best-practice'
- '#productivity'
- '#python'
related:
- '[[2026-07-29-your-fraud-engines-search-is-either-a-librarian-or-a-scholar-it-needs-to-be-both]]'
- '[[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]'
- '[[2026-06-30-postgresql-mvcc-vacuum-bloat-wraparound-autovacuum-tuning-in-production]]'
- '[[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]'
- '[[2026-04-21-i-build-custom-trading-bots-for-deriv-and-mt4mt5-heres-what-that-actually-looks-like]]'
- '[[2026-05-25-the-6-dimension-production-readiness-checklist-for-n8n-workflows]]'
status: unread
---

> **TL;DR:** Reciprocal rank fusion merges two ranked lists — say, BM25 results and vector-search results over your chargeback cases — into one. It has exactly one parameter, k . And the answer is just... 60. Not tuned per dataset. N…

## What’s new and why it matters
Reciprocal rank fusion merges two ranked lists — say, BM25 results and vector-search results over your chargeback cases — into one. It has exactly one parameter, k . And the answer is just... 60. Not tuned per dataset. Not learned. Sixty, from the original paper, works essentially everywhere. The entire algorithm: def rrf ( rankings : list [ list [ str ]], k : int = 60 ) -> list [ tuple [ str , float ]]: """ Each ranking is a list of doc IDs, best first. Score = sum of 1/(k + rank). """ scores = {} for ranking in rankings : for rank , doc in enumerate ( ranking , start = 1 ): scores [ doc ] =…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/fagundesv/my-favorite-constant-in-retrieval-is-60-nobody-tunes-it-thats-the-point-4857

## Related notes
- [[2026-07-29-your-fraud-engines-search-is-either-a-librarian-or-a-scholar-it-needs-to-be-both]]
- [[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]
- [[2026-06-30-postgresql-mvcc-vacuum-bloat-wraparound-autovacuum-tuning-in-production]]
- [[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]
- [[2026-04-21-i-build-custom-trading-bots-for-deriv-and-mt4mt5-heres-what-that-actually-looks-like]]
- [[2026-05-25-the-6-dimension-production-readiness-checklist-for-n8n-workflows]]
