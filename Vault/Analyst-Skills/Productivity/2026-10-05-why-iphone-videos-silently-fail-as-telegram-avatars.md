---
title: Why iPhone Videos Silently Fail as Telegram Avatars
date: '2026-10-05'
source: https://dev.to/liveavabot/why-iphone-videos-silently-fail-as-telegram-avatars-4boe
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-05-28-converting-iphone-hevc-videos-to-telegram-video-avatars-with-ffmpeg]]'
- '[[2026-10-03-how-i-converted-iphone-hevc-videos-into-telegram-video-avatars]]'
- '[[2026-07-24-building-a-telegram-video-avatar-bot-with-ffmpeg-and-aiogram-3]]'
- '[[2026-05-24-why-your-iphone-video-avatar-silently-fails-in-telegram]]'
- '[[2026-07-01-why-iphone-videos-silently-fail-as-telegram-video-avatars-and-how-to-fix-it-with-ffmpeg]]'
- '[[2026-09-14-why-iphone-videos-fail-as-telegram-avatars-and-how-to-fix-it]]'
status: unread
---

> **TL;DR:** The problem nobody talks about You record a short clip on your iPhone, open Telegram, tap "set video avatar", upload, and nothing happens. No error, no toast, just the old photo sitting there. I hit this once before I go…

## What’s new and why it matters
The problem nobody talks about You record a short clip on your iPhone, open Telegram, tap "set video avatar", upload, and nothing happens. No error, no toast, just the old photo sitting there. I hit this once before I got curious. The culprit is HEVC. Since iOS 11 the default camera codec is H.265 (HEVC), and Telegram's video avatar pipeline rejects HEVC without telling you. The upload "succeeds" because the file reaches the server, but the server side validator throws it out. What Telegram actually wants The video avatar spec is strict and not well documented. After some trial and error on wh…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/liveavabot/why-iphone-videos-silently-fail-as-telegram-avatars-4boe

## Related notes
- [[2026-05-28-converting-iphone-hevc-videos-to-telegram-video-avatars-with-ffmpeg]]
- [[2026-10-03-how-i-converted-iphone-hevc-videos-into-telegram-video-avatars]]
- [[2026-07-24-building-a-telegram-video-avatar-bot-with-ffmpeg-and-aiogram-3]]
- [[2026-05-24-why-your-iphone-video-avatar-silently-fails-in-telegram]]
- [[2026-07-01-why-iphone-videos-silently-fail-as-telegram-video-avatars-and-how-to-fix-it-with-ffmpeg]]
- [[2026-09-14-why-iphone-videos-fail-as-telegram-avatars-and-how-to-fix-it]]
