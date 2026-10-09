---
title: x & (x - 1) and three other bit tricks, and the one that lies about negative
  numbers
date: '2026-10-09'
source: https://dev.to/jackson_s_33a25dbcc9fc24e/x-x-1-and-three-other-bit-tricks-and-the-one-that-lies-about-negative-numbers-30i7
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#tool'
related:
- '[[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
status: unread
---

> **TL;DR:** Bit manipulation questions look like trivia until you see that almost all of them come from four facts. Here they are, why each one works, and the shortcut that gives the wrong answer on negative numbers. 1. x & 1 tells…

## What’s new and why it matters
Bit manipulation questions look like trivia until you see that almost all of them come from four facts. Here they are, why each one works, and the shortcut that gives the wrong answer on negative numbers. 1. x & 1 tells you if a number is odd The lowest bit is the 1s column. It's 1 for every odd number and 0 for every even one, so x & 1 is the parity without a division. def is_odd ( x ): return ( x & 1 ) == 1 2. x & (x - 1) clears the lowest set bit Subtracting 1 flips the lowest 1 bit to 0 and every 0 below it to 1. ANDing with the original keeps everything above that bit and zeroes the rest:…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jackson_s_33a25dbcc9fc24e/x-x-1-and-three-other-bit-tricks-and-the-one-that-lies-about-negative-numbers-30i7

## Related notes
- [[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
