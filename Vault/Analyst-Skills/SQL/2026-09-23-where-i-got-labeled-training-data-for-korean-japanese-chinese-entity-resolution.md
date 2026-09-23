---
title: Where I got labeled training data for Korean-Japanese-Chinese entity resolution
date: '2026-09-23'
source: https://dev.to/hannune/where-i-got-labeled-training-data-for-korean-japanese-chinese-entity-resolution-1j5d
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-08-11-code-interpreter-is-infrastructure-not-a-prompt]]'
- '[[2026-07-03-i-ranked-30-ai-apis-by-price-and-the-results-are-wild]]'
- '[[2026-08-12-im-building-an-algorithmic-trading-system-in-python]]'
- '[[2026-04-22-i-kept-forgetting-to-delete-my-venvs-so-i-built-a-gui-for-it]]'
status: unread
---

> **TL;DR:** Around pair 400 of the manual annotation batch, I got to a Korean holding company and its Japanese parent. The Japanese database had the company listed as a joint venture, the Korean filing described it as a wholly-owned…

## What’s new and why it matters
Around pair 400 of the manual annotation batch, I got to a Korean holding company and its Japanese parent. The Japanese database had the company listed as a joint venture, the Korean filing described it as a wholly-owned subsidiary. Same entity, but the ownership description was genuinely different between sources. I marked it as a match since the names clearly referred to the same company, but I wrote a note that I still don't know what to do with. That was about a month in. I ended up reviewing around 2,000 pairs by hand before I had enough coverage to feel reasonably confident in the KR-JP…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hannune/where-i-got-labeled-training-data-for-korean-japanese-chinese-entity-resolution-1j5d

## Related notes
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-08-11-code-interpreter-is-infrastructure-not-a-prompt]]
- [[2026-07-03-i-ranked-30-ai-apis-by-price-and-the-results-are-wild]]
- [[2026-08-12-im-building-an-algorithmic-trading-system-in-python]]
- [[2026-04-22-i-kept-forgetting-to-delete-my-venvs-so-i-built-a-gui-for-it]]
