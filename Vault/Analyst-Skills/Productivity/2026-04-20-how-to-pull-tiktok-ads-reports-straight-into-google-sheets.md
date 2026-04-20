---
title: How to pull TikTok Ads reports straight into Google Sheets
date: '2026-04-20'
source: https://dev.to/julianreiter/how-to-pull-tiktok-ads-reports-straight-into-google-sheets-4opi
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-03-05-my-agent-burned-147-in-40-minutes-so-i-wrote-a-small-circuit-breaker]]'
- '[[2026-04-14-your-code-never-leaves-your-machine-5-ai-developer-tools-i-built-with-local-llms]]'
- '[[2026-03-10-the-script-worked-the-ciso-needed-something-else-iam-audit-v2-interactive-dashboard-root-account-detection-and-docker]]'
- '[[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]'
status: unread
---

> **TL;DR:** The TikTok Ads Manager UI is fine for browsing, but if you run more than two campaigns you eventually need yesterday's spend in a Google Sheet before you've made coffee. The platform's CSV export button is the only path…

## What’s new and why it matters
The TikTok Ads Manager UI is fine for browsing, but if you run more than two campaigns you eventually need yesterday's spend in a Google Sheet before you've made coffee. The platform's CSV export button is the only path the UI offers — and it's the same number of clicks every morning. This post walks through replacing that chore with a 30-line cron job, using the official TikTok Marketing API and a small open-source CLI called aigen-reports . What you'll end up with Every morning at 02:00 your server pulls yesterday's campaign metrics for each of your TikTok ad accounts and appends them to a s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/julianreiter/how-to-pull-tiktok-ads-reports-straight-into-google-sheets-4opi

## Related notes
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-03-05-my-agent-burned-147-in-40-minutes-so-i-wrote-a-small-circuit-breaker]]
- [[2026-04-14-your-code-never-leaves-your-machine-5-ai-developer-tools-i-built-with-local-llms]]
- [[2026-03-10-the-script-worked-the-ciso-needed-something-else-iam-audit-v2-interactive-dashboard-root-account-detection-and-docker]]
- [[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]
