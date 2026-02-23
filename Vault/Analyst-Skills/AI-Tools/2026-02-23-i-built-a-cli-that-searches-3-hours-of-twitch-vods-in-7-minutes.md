---
title: I Built a CLI That Searches 3 Hours of Twitch VODs in 7 Minutes
date: '2026-02-23'
source: https://dev.to/yurukusa/i-built-a-cli-that-searches-3-hours-of-twitch-vods-in-7-minutes-514l
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#support-analytics'
- '#tool'
related:
- '[[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]'
- '[[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-02-23-5-backtesting-mistakes-that-cost-traders-thousands]]'
- '[[2026-02-22-how-to-generate-business-leads-using-google-maps-ids-and-python]]'
- '[[2026-02-22-build-a-rag-system-with-python-and-a-local-llm-no-api-costs]]'
status: unread
---

> **TL;DR:** I watch a lot of streams. And every few days, I find myself doing the same thing: scrubbing through a 3-hour VOD at 2x speed, trying to find the 30 seconds where the streamer mentioned a specific game. That's 90 minutes…

## What’s new and why it matters
I watch a lot of streams. And every few days, I find myself doing the same thing: scrubbing through a 3-hour VOD at 2x speed, trying to find the 30 seconds where the streamer mentioned a specific game. That's 90 minutes of my life to find half a minute of content. So I built a CLI tool that solves this in 7 minutes. It downloads the VOD audio, transcribes it with Whisper on my local GPU, and lets me search by keyword. No cloud. No API keys. Just timestamps. The tool is called VOD Search , and it's open source. The Problem Finding a specific moment in a stream archive is surprisingly painful. Y…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yurukusa/i-built-a-cli-that-searches-3-hours-of-twitch-vods-in-7-minutes-514l

## Related notes
- [[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]
- [[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-02-23-5-backtesting-mistakes-that-cost-traders-thousands]]
- [[2026-02-22-how-to-generate-business-leads-using-google-maps-ids-and-python]]
- [[2026-02-22-build-a-rag-system-with-python-and-a-local-llm-no-api-costs]]
