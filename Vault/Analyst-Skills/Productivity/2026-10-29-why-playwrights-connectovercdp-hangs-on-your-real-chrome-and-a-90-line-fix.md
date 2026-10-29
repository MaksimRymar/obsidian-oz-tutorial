---
title: Why Playwright's connect_over_cdp() hangs on your real Chrome — and a 90-line
  fix
date: '2026-10-29'
source: https://dev.to/bottiezimmie/why-playwrights-connectovercdp-hangs-on-your-real-chrome-and-a-90-line-fix-2038
domain: Productivity
relevance: 🟡
tags:
- '#library'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-09-28-practice-pandas-and-numpy-without-installing-anything-free-browser-compiler]]'
- '[[2026-07-09-dashboards-dont-get-opened-building-a-weekly-lapse-risk-pipeline-that-pushes-work-instead-of-waiting-for-logins]]'
- '[[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
status: unread
---

> **TL;DR:** If you've ever tried to drive your real Chrome — the one with your logins and 20 tabs — over CDP instead of a throwaway headless instance, you've probably watched this freeze: browser = p . chromium . connect_over_cdp (…

## What’s new and why it matters
If you've ever tried to drive your real Chrome — the one with your logins and 20 tabs — over CDP instead of a throwaway headless instance, you've probably watched this freeze: browser = p . chromium . connect_over_cdp ( " http://localhost:9222 " ) # ...hangs for 180s It works in a demo (fresh browser, one tab). Then you point it at a browser that's been open a while, and it times out. You bump the timeout. It still hangs. Here's why — and a tiny fix. Why it hangs connect_over_cdp() doesn't just attach to a tab. It negotiates at the browser level: it runs Target.setAutoAttach and tries to enume…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/bottiezimmie/why-playwrights-connectovercdp-hangs-on-your-real-chrome-and-a-90-line-fix-2038

## Related notes
- [[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-09-28-practice-pandas-and-numpy-without-installing-anything-free-browser-compiler]]
- [[2026-07-09-dashboards-dont-get-opened-building-a-weekly-lapse-risk-pipeline-that-pushes-work-instead-of-waiting-for-logins]]
- [[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
