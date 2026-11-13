---
title: Check a narrated video source log for missing tray marks with Python
date: '2026-11-13'
source: https://dev.to/_a2923b30009c0d41b7dad/check-a-narrated-video-source-log-for-missing-tray-marks-with-python-58fn
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tutorial'
related:
- '[[2026-11-11-catch-unexpected-missing-value-codes-in-a-research-csv]]'
- '[[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]'
- '[[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]'
- '[[2026-11-07-keep-reviewer-anchors-tied-to-one-manuscript-revision]]'
- '[[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]'
- '[[2026-09-28-detect-500-errors-in-server-logs-with-python-in-10-lines]]'
status: unread
---

> **TL;DR:** This tutorial was prepared with AI assistance. A flat list of timestamps can hide a missing shot. Add a tray ID and an event to make the handoff checkable. Run the complete and missing examples. The first returns PASS, t…

## What’s new and why it matters
This tutorial was prepared with AI assistance. A flat list of timestamps can hide a missing shot. Add a tray ID and an event to make the handoff checkable. Run the complete and missing examples. The first returns PASS, the second CHECK. The script checks only events and source order. A reviewer still needs to match the picture to the tray. python check-tray-marks.py tray-complete.csv python check-tray-marks.py tray-missing.csv check-tray-marks.py import csv import sys with open ( sys . argv [ 1 ] , encoding = 'utf-8' , newline = '' ) as source : rows = list ( csv . DictReader ( source ) ) expe…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/_a2923b30009c0d41b7dad/check-a-narrated-video-source-log-for-missing-tray-marks-with-python-58fn

## Related notes
- [[2026-11-11-catch-unexpected-missing-value-codes-in-a-research-csv]]
- [[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]
- [[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]
- [[2026-11-07-keep-reviewer-anchors-tied-to-one-manuscript-revision]]
- [[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]
- [[2026-09-28-detect-500-errors-in-server-logs-with-python-in-10-lines]]
