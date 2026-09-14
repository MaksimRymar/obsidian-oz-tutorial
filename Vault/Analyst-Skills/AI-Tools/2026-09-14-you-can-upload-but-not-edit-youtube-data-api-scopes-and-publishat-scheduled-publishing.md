---
title: 'You Can Upload but Not Edit: YouTube Data API Scopes and publishAt Scheduled
  Publishing'
date: '2026-09-14'
source: https://dev.to/acs_developer/you-can-upload-but-not-edit-youtube-data-api-scopes-and-publishat-scheduled-publishing-4b4h
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-30-vanna-aivanna-has-been-archived-since-march---whats-actually-frozen-what-isnt-and-your-four-real-options]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-06-13-select-final-and-optimize-final-are-not-the-same-thing]]'
status: unread
---

> **TL;DR:** Automating YouTube uploads with scheduled publishing produced three failures that never raised an error: youtube.upload cannot call videos.update , a token can silently belong to the wrong channel, and publishAt is ignor…

## What’s new and why it matters
Automating YouTube uploads with scheduled publishing produced three failures that never raised an error: youtube.upload cannot call videos.update , a token can silently belong to the wrong channel, and publishAt is ignored unless privacyStatus is private . What I wanted Export one short video a day and publish it at a fixed time the next day. I automated the part where "once the exported file is in place, everything runs through to scheduled publishing" with the YouTube Data API v3. Done by hand it is five steps: open Studio, pick the video, paste in the title and description, swap the thumbna…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/acs_developer/you-can-upload-but-not-edit-youtube-data-api-scopes-and-publishat-scheduled-publishing-4b4h

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-30-vanna-aivanna-has-been-archived-since-march---whats-actually-frozen-what-isnt-and-your-four-real-options]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-06-13-select-final-and-optimize-final-are-not-the-same-thing]]
