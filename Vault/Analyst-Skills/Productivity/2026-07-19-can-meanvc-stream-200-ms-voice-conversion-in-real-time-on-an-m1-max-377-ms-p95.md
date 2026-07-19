---
title: Can MeanVC Stream 200 ms Voice Conversion in Real Time on an M1 Max? 37.7 ms
  p95
date: '2026-07-19'
source: https://dev.to/kiarina/can-meanvc-stream-200-ms-voice-conversion-in-real-time-on-an-m1-max-377-ms-p95-1l9b
domain: Productivity
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#productivity'
- '#sql'
- '#tool'
related:
- '[[2026-07-17-can-yamnet-detect-unseen-sudden-sounds-in-real-time-a-48-stream-evaluation]]'
- '[[2026-06-15-a-40-line-llm-based-bash-command-executor-in-python]]'
- '[[2026-05-30-simple-sql-tool]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]'
status: unread
---

> **TL;DR:** Hello, everyone. It would be interesting if a Mac could keep what I say while changing only the characteristics of my voice, all locally and in real time. Today, I am testing MeanVC's 200 ms streaming model on an Apple M…

## What’s new and why it matters
Hello, everyone. It would be interesting if a Mac could keep what I say while changing only the characteristics of my voice, all locally and in real time. Today, I am testing MeanVC's 200 ms streaming model on an Apple M1 Max. I will measure processing speed, the shift in speaker characteristics, and discontinuities between audio chunks. The short answer is that one CPU thread converted a 200 ms audio chunk in 37.7 ms at p95 . All 99 measured chunks finished before the next chunk arrived, and the converted voice became more similar to the target reference than to the source speaker. However, e…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kiarina/can-meanvc-stream-200-ms-voice-conversion-in-real-time-on-an-m1-max-377-ms-p95-1l9b

## Related notes
- [[2026-07-17-can-yamnet-detect-unseen-sudden-sounds-in-real-time-a-48-stream-evaluation]]
- [[2026-06-15-a-40-line-llm-based-bash-command-executor-in-python]]
- [[2026-05-30-simple-sql-tool]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]
