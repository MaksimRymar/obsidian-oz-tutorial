---
title: How I Built a Telegram Video Avatar Bot With Python and FFmpeg
date: '2026-04-21'
source: https://dev.to/liveavabot/how-i-built-a-telegram-video-avatar-bot-with-python-and-ffmpeg-o9p
domain: SQL
relevance: 🔴
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]'
- '[[2026-04-21-i-build-custom-trading-bots-for-deriv-and-mt4mt5-heres-what-that-actually-looks-like]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-03-14-i-was-tired-of-parsing-xbrl-so-i-built-a-sec-edgar-api]]'
status: unread
---

> **TL;DR:** I tried to set a video avatar on Telegram last month. Recorded a short clip on my iPhone, uploaded it, and nothing happened. No error message. No toast notification. Telegram just silently rejected it. Turns out iPhone r…

## What’s new and why it matters
I tried to set a video avatar on Telegram last month. Recorded a short clip on my iPhone, uploaded it, and nothing happened. No error message. No toast notification. Telegram just silently rejected it. Turns out iPhone records in HEVC (H.265) by default since the iPhone 7. Telegram's video avatar system only accepts H.264. When you upload HEVC, the server validates it, fails, and tells you absolutely nothing. I spent two hours thinking my internet connection was broken before I figured this out. What Telegram Video Avatars Actually Require The documentation is sparse, so I had to reverse-engin…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/liveavabot/how-i-built-a-telegram-video-avatar-bot-with-python-and-ffmpeg-o9p

## Related notes
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]
- [[2026-04-21-i-build-custom-trading-bots-for-deriv-and-mt4mt5-heres-what-that-actually-looks-like]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-03-14-i-was-tired-of-parsing-xbrl-so-i-built-a-sec-edgar-api]]
