---
title: 'Why Your Concordance DAT File Won''t Parse: The þ Delimiter Encoding Trap'
date: '2026-03-31'
source: https://dev.to/frisk55frisk/why-your-concordance-dat-file-wont-parse-the-th-delimiter-encoding-trap-20mj
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-03-11-i-built-a-zero-friction-sqlite-playground-for-my-students]]'
- '[[2026-03-16-real-time-sql-analysis-in-vs-code-catch-dangerous-queries-before-you-save-the-file]]'
- '[[2026-03-09-mastering-sql-joins-and-window-functions-with-real-examples]]'
status: unread
---

> **TL;DR:** If you work with eDiscovery load files, you've probably hit this: you receive a Concordance DAT file, try to import it into your review platform, and it fails silently or produces garbled data. No useful error message. J…

## What’s new and why it matters
If you work with eDiscovery load files, you've probably hit this: you receive a Concordance DAT file, try to import it into your review platform, and it fails silently or produces garbled data. No useful error message. Just broken records. There's a good chance the problem is the þ character. What makes Concordance DAT files special Concordance DAT is the most common load file format in eDiscovery. It uses two unusual delimiter characters: Field separator : þ (thorn, Unicode U+00FE) Quote character : ® (registered sign, Unicode U+00AE) These were chosen decades ago specifically because they al…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/frisk55frisk/why-your-concordance-dat-file-wont-parse-the-th-delimiter-encoding-trap-20mj

## Related notes
- [[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-03-11-i-built-a-zero-friction-sqlite-playground-for-my-students]]
- [[2026-03-16-real-time-sql-analysis-in-vs-code-catch-dangerous-queries-before-you-save-the-file]]
- [[2026-03-09-mastering-sql-joins-and-window-functions-with-real-examples]]
