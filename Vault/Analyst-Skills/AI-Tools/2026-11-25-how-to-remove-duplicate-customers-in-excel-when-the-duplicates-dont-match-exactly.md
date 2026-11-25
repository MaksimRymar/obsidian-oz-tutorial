---
title: How to remove duplicate customers in Excel when the duplicates don't match
  exactly
date: '2026-11-25'
source: https://dev.to/nguyen_hiep_675b8460ca7f9/how-to-remove-duplicate-customers-in-excel-when-the-duplicates-dont-match-exactly-k8m
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-11-18-how-to-find-out-what-1000-websites-are-built-with-and-what-you-cant-see-from-outside]]'
- '[[2026-11-23-reading-pdfs-with-no-extractable-text-from-a-glyph-table-ai-drafts-it-once-then-every-run-is-free-and-identical]]'
- '[[2026-09-25-the-4-excel-jobs-i-refuse-to-do-by-hand-anymore-so-i-automated-them-in-python]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-26-26-of-45-shops-had-no-way-to-reach-them-heres-the-script-i-added]]'
- '[[2026-11-21-sql-formatting-rules-that-make-code-review-painless]]'
status: unread
---

> **TL;DR:** Excel's Remove Duplicates button works well when two rows are identical. Customer lists rarely are. The same person shows up as: Name Email Phone OLIVIA BROWN olivia.brown@example.com 07700 900101 Olivia Brown OLIVIA.BRO…

## What’s new and why it matters
Excel's Remove Duplicates button works well when two rows are identical. Customer lists rarely are. The same person shows up as: Name Email Phone OLIVIA BROWN olivia.brown@example.com 07700 900101 Olivia Brown OLIVIA.BROWN@EXAMPLE.COM ␠ james wilson james.w@example.org 07700 900102 James Wilson james.w@example.org . +44 7700 900102 To Excel these are four different rows. To you they're two customers. Here's how to fix that, from the quickest manual method to a repeatable one. 1. Normalise first, then remove duplicates (pure Excel) Duplicates hide behind capital letters, stray spaces and traili…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/nguyen_hiep_675b8460ca7f9/how-to-remove-duplicate-customers-in-excel-when-the-duplicates-dont-match-exactly-k8m

## Related notes
- [[2026-11-18-how-to-find-out-what-1000-websites-are-built-with-and-what-you-cant-see-from-outside]]
- [[2026-11-23-reading-pdfs-with-no-extractable-text-from-a-glyph-table-ai-drafts-it-once-then-every-run-is-free-and-identical]]
- [[2026-09-25-the-4-excel-jobs-i-refuse-to-do-by-hand-anymore-so-i-automated-them-in-python]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-26-26-of-45-shops-had-no-way-to-reach-them-heres-the-script-i-added]]
- [[2026-11-21-sql-formatting-rules-that-make-code-review-painless]]
