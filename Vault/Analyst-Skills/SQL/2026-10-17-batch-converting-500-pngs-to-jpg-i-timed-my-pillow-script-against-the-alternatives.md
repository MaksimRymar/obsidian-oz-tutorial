---
title: 'Batch-Converting 500 PNGs to JPG: I Timed My Pillow Script Against the Alternatives'
date: '2026-10-17'
source: https://dev.to/dennyguide/batch-converting-500-pngs-to-jpg-i-timed-my-pillow-script-against-the-alternatives-dm8
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-10-02-how-i-turn-ai-images-into-print-ready-vector-stickers-no-illustrator-no-gpu]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-09-06-the-julius-ai-free-plan-what-the-free-credits-actually-get-you]]'
- '[[2026-08-14-funnel-analysis-in-sql-find-exactly-where-users-drop-off]]'
status: unread
---

> **TL;DR:** Every few months I get the same folder: a few hundred PNGs exported from a design tool, all needing to be JPG before they can go into a CMS that has a hard 25 MB per-image cap. PNGs of screenshots and photos are heavy, a…

## What’s new and why it matters
Every few months I get the same folder: a few hundred PNGs exported from a design tool, all needing to be JPG before they can go into a CMS that has a hard 25 MB per-image cap. PNGs of screenshots and photos are heavy, and nobody on the content team is going to open an image editor 500 times. So I have a script for this. But the last time I posted it, someone asked the obvious question: "is that actually faster than just using an online converter?" Fair. Let's measure it. The task 500 PNG files, 800×600 About 20% have an alpha channel (logos/icons), the rest are opaque Target: JPG, quality 85,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dennyguide/batch-converting-500-pngs-to-jpg-i-timed-my-pillow-script-against-the-alternatives-dm8

## Related notes
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-10-02-how-i-turn-ai-images-into-print-ready-vector-stickers-no-illustrator-no-gpu]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-09-06-the-julius-ai-free-plan-what-the-free-credits-actually-get-you]]
- [[2026-08-14-funnel-analysis-in-sql-find-exactly-where-users-drop-off]]
