---
title: How Python's rglob Silently Loses Files, and Why macOS Makes It Worse
date: '2026-07-04'
source: https://dev.to/prateek11rai/how-pythons-rglob-silently-loses-files-and-why-macos-makes-it-worse-58ap
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-06-20-i-built-a-machine-verifiable-contract-system-for-python-code-heres-how-it-works]]'
status: unread
---

> **TL;DR:** A Python service I work on did something that shouldn't be possible. It wrote a directory full of files, turned around to upload them, and found nothing. The files were right there — ls saw them from another terminal. Th…

## What’s new and why it matters
A Python service I work on did something that shouldn't be possible. It wrote a directory full of files, turned around to upload them, and found nothing. The files were right there — ls saw them from another terminal. The upload logged success. Zero files. No exception. Digging into why took me through three separate layers of the stack, each one lying just a little, and a paper trail going back to 2015 that almost nobody has read. The record of every one of these problems has been sitting in public bug trackers and mailing lists for years — some of it for two decades. This post is the story o…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/prateek11rai/how-pythons-rglob-silently-loses-files-and-why-macos-makes-it-worse-58ap

## Related notes
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-06-20-i-built-a-machine-verifiable-contract-system-for-python-code-heres-how-it-works]]
