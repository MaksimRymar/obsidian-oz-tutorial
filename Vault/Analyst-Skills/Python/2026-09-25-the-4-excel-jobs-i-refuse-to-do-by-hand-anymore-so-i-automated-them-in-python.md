---
title: The 4 Excel jobs I refuse to do by hand anymore (so I automated them in Python)
date: '2026-09-25'
source: https://dev.to/weilidev2026/the-4-excel-jobs-i-refuse-to-do-by-hand-anymore-so-i-automated-them-in-python-4poh
domain: Python
relevance: 🟡
tags:
- '#python'
- '#tool'
related:
- '[[2026-08-31-how-i-made-sql-run-inside-a-single-offline-html-file-no-wasm]]'
- '[[2026-08-10-build-a-gst-invoice-data-extractor-in-45-lines-of-python]]'
- '[[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-09-06-the-julius-ai-free-plan-what-the-free-credits-actually-get-you]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
status: unread
---

> **TL;DR:** Excel work has a way of eating entire afternoons: twelve monthly workbooks to merge, a sheet per month to split back out, formulas that break the moment the file touches pandas or a BI tool. These four command-line tools…

## What’s new and why it matters
Excel work has a way of eating entire afternoons: twelve monthly workbooks to merge, a sheet per month to split back out, formulas that break the moment the file touches pandas or a BI tool. These four command-line tools (openpyxl is the only dependency) do the boring versions of those jobs. 1. Summarize a workbook before opening it python xlsx_summary.py report.xlsx Prints rows, columns and a header preview per sheet. For a folder of workbooks, it's the fastest "what am I even looking at" pass. 2. Merge monthly workbooks — with a header contract xlsx_merge.py refuses files whose columns don't…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/weilidev2026/the-4-excel-jobs-i-refuse-to-do-by-hand-anymore-so-i-automated-them-in-python-4poh

## Related notes
- [[2026-08-31-how-i-made-sql-run-inside-a-single-offline-html-file-no-wasm]]
- [[2026-08-10-build-a-gst-invoice-data-extractor-in-45-lines-of-python]]
- [[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-09-06-the-julius-ai-free-plan-what-the-free-credits-actually-get-you]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
