---
title: How I Fixed iPhone HEVC Videos for Telegram Video Avatars
date: '2026-11-15'
source: https://dev.to/liveavabot/how-i-fixed-iphone-hevc-videos-for-telegram-video-avatars-2boo
domain: Productivity
relevance: 🟡
tags:
- '#best-practice'
- '#feature'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-07-24-building-a-telegram-video-avatar-bot-with-ffmpeg-and-aiogram-3]]'
- '[[2026-05-28-converting-iphone-hevc-videos-to-telegram-video-avatars-with-ffmpeg]]'
- '[[2026-10-03-how-i-converted-iphone-hevc-videos-into-telegram-video-avatars]]'
- '[[2026-10-05-why-iphone-videos-silently-fail-as-telegram-avatars]]'
- '[[2026-05-24-why-your-iphone-video-avatar-silently-fails-in-telegram]]'
- '[[2026-09-14-why-iphone-videos-fail-as-telegram-avatars-and-how-to-fix-it]]'
status: unread
---

> **TL;DR:** The Problem You record a video on your iPhone and try to set it as your Telegram video avatar. Telegram silently rejects it. No error, no dialog, just nothing happens. The culprit is HEVC (H.265). iPhones have recorded i…

## What’s new and why it matters
The Problem You record a video on your iPhone and try to set it as your Telegram video avatar. Telegram silently rejects it. No error, no dialog, just nothing happens. The culprit is HEVC (H.265). iPhones have recorded in HEVC by default since iOS 11. Telegram's video avatar feature only accepts H.264. It doesn't tell you that. I hit this myself, then saw it come up repeatedly in Telegram support threads. So I built a bot to handle the conversion. What Telegram Actually Requires After reading the docs and doing a lot of trial and error, the full spec for a Telegram video avatar is: Codec: H.26…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/liveavabot/how-i-fixed-iphone-hevc-videos-for-telegram-video-avatars-2boo

## Related notes
- [[2026-07-24-building-a-telegram-video-avatar-bot-with-ffmpeg-and-aiogram-3]]
- [[2026-05-28-converting-iphone-hevc-videos-to-telegram-video-avatars-with-ffmpeg]]
- [[2026-10-03-how-i-converted-iphone-hevc-videos-into-telegram-video-avatars]]
- [[2026-10-05-why-iphone-videos-silently-fail-as-telegram-avatars]]
- [[2026-05-24-why-your-iphone-video-avatar-silently-fails-in-telegram]]
- [[2026-09-14-why-iphone-videos-fail-as-telegram-avatars-and-how-to-fix-it]]
