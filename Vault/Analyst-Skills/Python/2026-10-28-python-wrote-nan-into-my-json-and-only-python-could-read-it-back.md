---
title: Python Wrote NaN Into My JSON and Only Python Could Read It Back
date: '2026-10-28'
source: https://dev.to/superfunicular/python-wrote-nan-into-my-json-and-only-python-could-read-it-back-1n3
domain: Python
relevance: 🟡
tags:
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-17-why-did-ls-sort-clip10-before-clip1-three-orders-for-one-folder-of-numbered-clips]]'
- '[[2026-10-15-on-windows-four-processes-appending-to-one-file-lost-37-of-200-lines]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]'
status: unread
---

> **TL;DR:** I had a small Python script writing one JSON line per camera clip, with a temperature reading next to each file name. Sometimes there was no reading, so the script stored float('nan') as a placeholder. Python read the fi…

## What’s new and why it matters
I had a small Python script writing one JSON line per camera clip, with a temperature reading next to each file name. Sometimes there was no reading, so the script stored float('nan') as a placeholder. Python read the file back without a complaint. A Node dashboard reading the same file threw on two of the three lines: # write_log.py: one JSON line per clip, with a temperature reading that may be missing import json clips = [ { " clip " : " clip_0001.mp4 " , " temp_c " : 31.5 }, { " clip " : " clip_0002.mp4 " , " temp_c " : float ( " nan " )}, # sensor gave no reading { " clip " : " clip_0003.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/superfunicular/python-wrote-nan-into-my-json-and-only-python-could-read-it-back-1n3

## Related notes
- [[2026-10-17-why-did-ls-sort-clip10-before-clip1-three-orders-for-one-folder-of-numbered-clips]]
- [[2026-10-15-on-windows-four-processes-appending-to-one-file-lost-37-of-200-lines]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]
