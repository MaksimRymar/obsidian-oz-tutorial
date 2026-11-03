---
title: The Reconciliation Tool I Almost Didn't Finish
date: '2026-11-03'
source: https://dev.to/xayenuniverse/the-reconciliation-tool-i-almost-didnt-finish-5a5i
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]'
- '[[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]'
status: unread
---

> **TL;DR:** I want to tell you about the night I decided to build this. It wasn't when I sat down to write code — it was three hours into an Excel reconciliation for a client, at 11pm, when I noticed the sum of a column was off by ₦…

## What’s new and why it matters
I want to tell you about the night I decided to build this. It wasn't when I sat down to write code — it was three hours into an Excel reconciliation for a client, at 11pm, when I noticed the sum of a column was off by ₦0.02 and spent 45 minutes finding out why. The answer: floating-point arithmetic. Excel was storing ₦5,000.00 as 5000.0000000000003 because of the way it handles decimals, and my VLOOKUP was failing because the two sides of the match had slightly different underlying values. The ₦0.02 wasn't real money. It was the way Excel represented the money. I closed the spreadsheet, opene…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/xayenuniverse/the-reconciliation-tool-i-almost-didnt-finish-5a5i

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]
- [[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]
