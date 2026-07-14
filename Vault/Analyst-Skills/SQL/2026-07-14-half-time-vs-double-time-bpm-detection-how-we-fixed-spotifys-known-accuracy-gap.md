---
title: 'Half-Time vs Double-Time BPM Detection: How We Fixed Spotify''s Known Accuracy
  Gap'
date: '2026-07-14'
source: https://dev.to/birrings/half-time-vs-double-time-bpm-detection-how-we-fixed-spotifys-known-accuracy-gap-3fi6
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-07-02-dont-use-not-in]]'
- '[[2026-06-19-vector-databases-are-not-magic-heres-whats-actually-happening-under-the-hood]]'
- '[[2026-06-10-your-database-is-fast-your-queries-are-slow]]'
- '[[2026-04-11-7-free-defi-apis-every-developer-should-know-in-2026-with-code-examples]]'
status: unread
---

> **TL;DR:** Run Blinding Lights by The Weeknd through Essentia's RhythmExtractor2013 . It returns 85.4 BPM. The track is famously 171 BPM — one of the most-played tracks of the last decade, peer-reviewed by literally every DJ in the…

## What’s new and why it matters
Run Blinding Lights by The Weeknd through Essentia's RhythmExtractor2013 . It returns 85.4 BPM. The track is famously 171 BPM — one of the most-played tracks of the last decade, peer-reviewed by literally every DJ in the world. This isn't a bug. It's a known property of beat-tracking algorithms: they pick the wrong tactus level for tracks where the perceived beat doesn't match the dominant onset rate. Spotify's deprecated audio_features had the same problem — entire genres came back at half their actual tempo. This article unpicks why that happens and shows the 30-line heuristic we use to dete…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/birrings/half-time-vs-double-time-bpm-detection-how-we-fixed-spotifys-known-accuracy-gap-3fi6

## Related notes
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-07-02-dont-use-not-in]]
- [[2026-06-19-vector-databases-are-not-magic-heres-whats-actually-happening-under-the-hood]]
- [[2026-06-10-your-database-is-fast-your-queries-are-slow]]
- [[2026-04-11-7-free-defi-apis-every-developer-should-know-in-2026-with-code-examples]]
