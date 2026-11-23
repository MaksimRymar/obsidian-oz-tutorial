---
title: 'youtube-transcript-api NoTranscriptFound vs TranscriptsDisabled: what they
  mean and how to fix them'
date: '2026-11-23'
source: https://dev.to/logicbase_systems/youtube-transcript-api-notranscriptfound-vs-transcriptsdisabled-what-they-mean-and-how-to-fix-them-2886
domain: Productivity
relevance: 🟡
tags:
- '#library'
- '#productivity'
- '#python'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-11-17-youtube-transcript-api-requestblocked-on-a-cloud-server-why-it-happens-and-3-fixes]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-10-01-transcribe-tiktok-and-instagram-videos-to-text-with-python-whisper-no-api-key]]'
- '[[2026-11-16-oracle-fusion-rest-api-returns-only-25-invoices-page-through-with-limit-offset-and-hasmore]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-09-18-why-your-youtube-transcript-scraper-says-no-captions-found-on-a-video-that-has-captions]]'
status: unread
---

> **TL;DR:** Disclosure: I made the Apify Actor mentioned at the end, so I'm biased. Apify links here are referral links. Everything before that section is free and uses only youtube-transcript-api . You call YouTubeTranscriptApi().f…

## What’s new and why it matters
Disclosure: I made the Apify Actor mentioned at the end, so I'm biased. Apify links here are referral links. Everything before that section is free and uses only youtube-transcript-api . You call YouTubeTranscriptApi().fetch(video_id) and get one of these: youtube_transcript_api._errors.NoTranscriptFound: No transcripts were found for any of the requested language codes: ('en',) youtube_transcript_api._errors.TranscriptsDisabled: Subtitles are disabled for this video They look similar, but they mean different things and have different fixes. Everything below was tested on 23 November 2026 with…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/logicbase_systems/youtube-transcript-api-notranscriptfound-vs-transcriptsdisabled-what-they-mean-and-how-to-fix-them-2886

## Related notes
- [[2026-11-17-youtube-transcript-api-requestblocked-on-a-cloud-server-why-it-happens-and-3-fixes]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-10-01-transcribe-tiktok-and-instagram-videos-to-text-with-python-whisper-no-api-key]]
- [[2026-11-16-oracle-fusion-rest-api-returns-only-25-invoices-page-through-with-limit-offset-and-hasmore]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-09-18-why-your-youtube-transcript-scraper-says-no-captions-found-on-a-video-that-has-captions]]
