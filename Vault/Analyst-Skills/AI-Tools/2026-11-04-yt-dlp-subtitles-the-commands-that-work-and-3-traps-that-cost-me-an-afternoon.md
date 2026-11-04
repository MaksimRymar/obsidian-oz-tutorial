---
title: 'yt-dlp subtitles: the commands that work, and 3 traps that cost me an afternoon'
date: '2026-11-04'
source: https://dev.to/rapidshortsai_012681b0e02/yt-dlp-subtitles-the-commands-that-work-and-3-traps-that-cost-me-an-afternoon-18m6
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#support-analytics'
- '#tool'
related:
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-11-01-spark-is-lazy-and-that-one-fact-explains-most-beginner-confusion]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]'
- '[[2026-10-15-see-every-google-ad-a-competitor-runs-from-just-their-domain-curl-python-n8n]]'
status: unread
---

> **TL;DR:** If you only want the subtitles from a YouTube video, yt-dlp can do it without downloading the video. The flags look simple. Then you run them on a real channel and get a 429, a folder full of junk languages, or a re-run…

## What’s new and why it matters
If you only want the subtitles from a YouTube video, yt-dlp can do it without downloading the video. The flags look simple. Then you run them on a real channel and get a 429, a folder full of junk languages, or a re-run that starts again from zero. Everything below was run with yt-dlp 2026.07.04 on real videos this week. The one command most people want yt-dlp --skip-download --write-subs --write-auto-subs \ --sub-langs en --sub-format srt \ -o "%(id)s.%(ext)s" \ "https://www.youtube.com/watch?v=dQw4w9WgXcQ" What each part does: --skip-download keeps the video off your disk. You only get the s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rapidshortsai_012681b0e02/yt-dlp-subtitles-the-commands-that-work-and-3-traps-that-cost-me-an-afternoon-18m6

## Related notes
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-11-01-spark-is-lazy-and-that-one-fact-explains-most-beginner-confusion]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]
- [[2026-10-15-see-every-google-ad-a-competitor-runs-from-just-their-domain-curl-python-n8n]]
