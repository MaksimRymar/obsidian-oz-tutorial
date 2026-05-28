---
title: Converting iPhone HEVC Videos to Telegram Video Avatars With FFmpeg
date: '2026-05-28'
source: https://dev.to/liveavabot/converting-iphone-hevc-videos-to-telegram-video-avatars-with-ffmpeg-396g
domain: SQL
relevance: 🔴
tags:
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-21-how-i-built-a-telegram-video-avatar-bot-with-python-and-ffmpeg]]'
- '[[2026-05-24-why-your-iphone-video-avatar-silently-fails-in-telegram]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-03-23-i-ran-56-experiments-to-find-the-best-way-to-make-ai-watch-videos]]'
- '[[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]'
- '[[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]'
status: unread
---

> **TL;DR:** The Problem: iPhone Videos Silently Fail I tried to set my Telegram video avatar from an iPhone clip and it just didn't work. No error message. The upload completed and my avatar stayed the same. After digging into the T…

## What’s new and why it matters
The Problem: iPhone Videos Silently Fail I tried to set my Telegram video avatar from an iPhone clip and it just didn't work. No error message. The upload completed and my avatar stayed the same. After digging into the Telegram Bot API spec and a few hours of trial and error with ffprobe, I figured out why. iPhones record video as HEVC (H.265) by default since iOS 11, and Telegram's video avatar endpoint only accepts H.264 in an MP4 container. When you upload HEVC, Telegram drops it on the floor without telling you. I built @liveavabot to fix this for myself, then opened it up. This post walks…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/liveavabot/converting-iphone-hevc-videos-to-telegram-video-avatars-with-ffmpeg-396g

## Related notes
- [[2026-04-21-how-i-built-a-telegram-video-avatar-bot-with-python-and-ffmpeg]]
- [[2026-05-24-why-your-iphone-video-avatar-silently-fails-in-telegram]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-03-23-i-ran-56-experiments-to-find-the-best-way-to-make-ai-watch-videos]]
- [[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]
- [[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]
