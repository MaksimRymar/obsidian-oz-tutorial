---
title: 'Same subject, three codes: handling syllabus versions when indexing exam papers'
date: '2026-11-04'
source: https://dev.to/offpage_prince/same-subject-three-codes-handling-syllabus-versions-when-indexing-exam-papers-fm3
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-29-a-4-hour-gtu-syllabus-unit-showed-up-in-all-9-maths-1-papers-here-is-the-data]]'
- '[[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]'
- '[[2026-10-31-modelling-gtus-4-backlog-detain-rule-in-15-lines-of-python]]'
- '[[2026-10-28-how-i-count-repeated-questions-across-44-gtu-exam-papers-and-what-broke]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-10-05-how-to-get-google-search-volume-for-a-list-of-keywords-without-a-google-ads-account]]'
status: unread
---

> **TL;DR:** I work on GTU Hero, a site that organises GTU (Gujarat Technological University) exam papers. This is a small data-modelling note from that work, and it applies to any project that indexes exam papers or course material.…

## What’s new and why it matters
I work on GTU Hero, a site that organises GTU (Gujarat Technological University) exam papers. This is a small data-modelling note from that work, and it applies to any project that indexes exam papers or course material. The problem: subject name is not a safe key GTU Maths 1 exists under three subject codes: 3110014, BE01000041 and BE01R00041. They are all "Maths 1" by name, but the modules are not the same: 3110014: calculus, sequences and series, Fourier series, multivariable calculus, multiple integrals, matrices. 5 credits. BE01000041 (w.e.f. 2024-25): no Fourier series, no matrices. 4 cr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/offpage_prince/same-subject-three-codes-handling-syllabus-versions-when-indexing-exam-papers-fm3

## Related notes
- [[2026-10-29-a-4-hour-gtu-syllabus-unit-showed-up-in-all-9-maths-1-papers-here-is-the-data]]
- [[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]
- [[2026-10-31-modelling-gtus-4-backlog-detain-rule-in-15-lines-of-python]]
- [[2026-10-28-how-i-count-repeated-questions-across-44-gtu-exam-papers-and-what-broke]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-10-05-how-to-get-google-search-volume-for-a-list-of-keywords-without-a-google-ads-account]]
