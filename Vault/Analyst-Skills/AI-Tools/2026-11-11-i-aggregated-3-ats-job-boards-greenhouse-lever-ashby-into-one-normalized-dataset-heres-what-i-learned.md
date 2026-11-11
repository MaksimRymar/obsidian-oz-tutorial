---
title: I aggregated 3 ATS job boards (Greenhouse, Lever, Ashby) into one normalized
  dataset — here's what I learned
date: '2026-11-11'
source: https://dev.to/realjons/i-aggregated-3-ats-job-boards-greenhouse-lever-ashby-into-one-normalized-dataset-heres-what-p6m
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-10-26-how-to-pull-job-postings-straight-from-company-career-sites-greenhouse-lever-ashby-workday-as-json]]'
- '[[2026-08-08-merging-job-postings-from-ten-ats-platforms-into-one-schema-and-the-four-fields-that-fight-back]]'
- '[[2026-07-27-i-tested-42-large-employers-to-see-which-ones-you-can-actually-scrape-only-7-worked]]'
- '[[2026-11-09-how-to-get-job-listings-from-seek-new-zealand-with-an-api-python-node-or-no-code]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-09-27-normalizing-public-job-board-data-with-python]]'
status: unread
---

> **TL;DR:** Job postings data is messy. Every company uses a different ATS, and each ATS returns a completely different schema: Greenhouse : integer IDs, location.name nested object, departments array Lever : UUIDs, flat categories…

## What’s new and why it matters
Job postings data is messy. Every company uses a different ATS, and each ATS returns a completely different schema: Greenhouse : integer IDs, location.name nested object, departments array Lever : UUIDs, flat categories object, workplace type as separate field Ashby : different ID format again, isRemote boolean, 970KB responses that stream-truncate I built an Apify Actor to normalize all three into one schema. Technical notes: The double-encoded HTML trap Greenhouse serves some boards with double-encoded HTML: &lt;p&gt;Salary: $121,600...&lt;/p&gt; instead of <p>...</p> . One html.unescape() p…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/realjons/i-aggregated-3-ats-job-boards-greenhouse-lever-ashby-into-one-normalized-dataset-heres-what-p6m

## Related notes
- [[2026-10-26-how-to-pull-job-postings-straight-from-company-career-sites-greenhouse-lever-ashby-workday-as-json]]
- [[2026-08-08-merging-job-postings-from-ten-ats-platforms-into-one-schema-and-the-four-fields-that-fight-back]]
- [[2026-07-27-i-tested-42-large-employers-to-see-which-ones-you-can-actually-scrape-only-7-worked]]
- [[2026-11-09-how-to-get-job-listings-from-seek-new-zealand-with-an-api-python-node-or-no-code]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-09-27-normalizing-public-job-board-data-with-python]]
