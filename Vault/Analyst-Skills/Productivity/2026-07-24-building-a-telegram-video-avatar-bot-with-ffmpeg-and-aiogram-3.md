---
title: Building a Telegram Video Avatar Bot with ffmpeg and Aiogram 3
date: '2026-07-24'
source: https://dev.to/liveavabot/building-a-telegram-video-avatar-bot-with-ffmpeg-and-aiogram-3-49h
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-05-28-converting-iphone-hevc-videos-to-telegram-video-avatars-with-ffmpeg]]'
- '[[2026-05-24-why-your-iphone-video-avatar-silently-fails-in-telegram]]'
- '[[2026-07-01-why-iphone-videos-silently-fail-as-telegram-video-avatars-and-how-to-fix-it-with-ffmpeg]]'
- '[[2026-04-21-how-i-built-a-telegram-video-avatar-bot-with-python-and-ffmpeg]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
status: unread
---

> **TL;DR:** The problem: iPhone videos silently fail as Telegram avatars Try setting a video as your Telegram profile picture from an iPhone. It just... doesn't work. No error, no explanation. The upload dialog closes, your avatar s…

## What’s new and why it matters
The problem: iPhone videos silently fail as Telegram avatars Try setting a video as your Telegram profile picture from an iPhone. It just... doesn't work. No error, no explanation. The upload dialog closes, your avatar stays the same. I hit this myself last month. Recorded a short clip on my iPhone, tried to set it as my TG avatar, nothing happened. Turns out iOS records in HEVC (H.265) by default, and Telegram's video avatar spec only accepts H.264. There's no warning. The client just refuses silently. So I built a bot that fixes this. Send it any video or GIF, get back a file that Telegram w…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/liveavabot/building-a-telegram-video-avatar-bot-with-ffmpeg-and-aiogram-3-49h

## Related notes
- [[2026-05-28-converting-iphone-hevc-videos-to-telegram-video-avatars-with-ffmpeg]]
- [[2026-05-24-why-your-iphone-video-avatar-silently-fails-in-telegram]]
- [[2026-07-01-why-iphone-videos-silently-fail-as-telegram-video-avatars-and-how-to-fix-it-with-ffmpeg]]
- [[2026-04-21-how-i-built-a-telegram-video-avatar-bot-with-python-and-ffmpeg]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
