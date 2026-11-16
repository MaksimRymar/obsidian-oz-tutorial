---
title: 'A duration test that could not fail: ffprobe reports the container, not the
  picture'
date: '2026-11-16'
source: https://dev.to/bitpage/a-duration-test-that-could-not-fail-ffprobe-reports-the-container-not-the-picture-4a7m
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
status: unread
---

> **TL;DR:** Short answer: ffprobe -show_entries format=duration reports the container's duration, which is the maximum over its streams, and in a generated clip the silent audio track always runs the full promised length. The pictur…

## What’s new and why it matters
Short answer: ffprobe -show_entries format=duration reports the container's duration, which is the maximum over its streams, and in a generated clip the silent audio track always runs the full promised length. The picture can end over a second early and that number does not move, so any test comparing it against the planned duration is green by construction. Ask the streams instead, add an assertion that the picture is not shorter than the sound, and derive the tolerance from the file's own frame rate. The pipeline builds a vertical clip from still images, a voice track and burned-in subtitles…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/bitpage/a-duration-test-that-could-not-fail-ffprobe-reports-the-container-not-the-picture-4a7m

## Related notes
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
