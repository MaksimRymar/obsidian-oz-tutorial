---
title: How I Converted iPhone HEVC Videos Into Telegram Video Avatars
date: '2026-10-03'
source: https://dev.to/liveavabot/how-i-converted-iphone-hevc-videos-into-telegram-video-avatars-1nif
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-28-converting-iphone-hevc-videos-to-telegram-video-avatars-with-ffmpeg]]'
- '[[2026-07-24-building-a-telegram-video-avatar-bot-with-ffmpeg-and-aiogram-3]]'
- '[[2026-07-01-why-iphone-videos-silently-fail-as-telegram-video-avatars-and-how-to-fix-it-with-ffmpeg]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-04-21-how-i-built-a-telegram-video-avatar-bot-with-python-and-ffmpeg]]'
- '[[2026-09-14-why-iphone-videos-fail-as-telegram-avatars-and-how-to-fix-it]]'
status: unread
---

> **TL;DR:** The pain nobody mentions I recorded a short clip on my iPhone, dragged it into the Telegram "set video avatar" dialog, and nothing happened. The app accepted the file, pretended to upload it, then quietly fell back to a…

## What’s new and why it matters
The pain nobody mentions I recorded a short clip on my iPhone, dragged it into the Telegram "set video avatar" dialog, and nothing happened. The app accepted the file, pretended to upload it, then quietly fell back to a still frame. No error message. The problem turned out to be HEVC. iPhones record H.265 by default since iOS 11. Telegram's video avatar endpoint will not touch H.265. It expects H.264, square frame, under 10 seconds, under 2MB, no audio track. Nothing in the UI tells you this. I lost two hours before I found the spec buried in a Telegram Core page. Then I spent a weekend buildi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/liveavabot/how-i-converted-iphone-hevc-videos-into-telegram-video-avatars-1nif

## Related notes
- [[2026-05-28-converting-iphone-hevc-videos-to-telegram-video-avatars-with-ffmpeg]]
- [[2026-07-24-building-a-telegram-video-avatar-bot-with-ffmpeg-and-aiogram-3]]
- [[2026-07-01-why-iphone-videos-silently-fail-as-telegram-video-avatars-and-how-to-fix-it-with-ffmpeg]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-04-21-how-i-built-a-telegram-video-avatar-bot-with-python-and-ffmpeg]]
- [[2026-09-14-why-iphone-videos-fail-as-telegram-avatars-and-how-to-fix-it]]
