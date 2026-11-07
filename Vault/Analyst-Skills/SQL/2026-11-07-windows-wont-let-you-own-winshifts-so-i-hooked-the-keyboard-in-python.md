---
title: Windows won't let you own Win+Shift+S. So I hooked the keyboard in Python.
date: '2026-11-07'
source: https://dev.to/akhourianmolkumar/windows-wont-let-you-own-winshifts-so-i-hooked-the-keyboard-in-python-248c
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-11-04-are-you-a-python-developer-or-a-python-expert-8-tests-i-failed-hijacking-winshifts-in-one-7600-line-file]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]'
- '[[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]'
status: unread
---

> **TL;DR:** I wanted one small thing: press Win+Shift+S and get my own screenshot tool instead of Snipping Tool. That turned into a 7,600-line Python project, and a pile of Windows internals that I couldn't find explained in one pla…

## What’s new and why it matters
I wanted one small thing: press Win+Shift+S and get my own screenshot tool instead of Snipping Tool. That turned into a 7,600-line Python project, and a pile of Windows internals that I couldn't find explained in one place. Here are the four that cost me the most hair. 1. RegisterHotKey can't claim Win+Shift+S Every tutorial says to use RegisterHotKey . It works for Ctrl+Alt+D . It silently fails for Win+Shift+S , because the shell reserves that combo. The way around it is a low-level keyboard hook ( WH_KEYBOARD_LL , id 13 ), which sees the key before the shell does: HOOKPROC = ctypes . WINFUN…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/akhourianmolkumar/windows-wont-let-you-own-winshifts-so-i-hooked-the-keyboard-in-python-248c

## Related notes
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-11-04-are-you-a-python-developer-or-a-python-expert-8-tests-i-failed-hijacking-winshifts-in-one-7600-line-file]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]
- [[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]
