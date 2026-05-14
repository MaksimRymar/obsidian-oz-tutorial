---
title: 'Slideshow Maker Pipelines: Annotating My 2-Year-Old Mess'
date: '2026-05-14'
source: https://dev.to/kokis_jorge_f43c7beb9b951/slideshow-maker-pipelines-annotating-my-2-year-old-mess-2bpk
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#presentations'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-27-how-i-handle-bulk-whois-lookups-at-scale-lessons-from-running-a-domain-api]]'
- '[[2026-04-22-i-kept-forgetting-to-delete-my-venvs-so-i-built-a-gui-for-it]]'
- '[[2026-04-17-the-quote-as-ceiling-billing-pattern]]'
- '[[2026-04-04-i-built-a-memory-system-because-i-die-every-30-minutes]]'
- '[[2026-04-14-build-your-own-second-brain-rag-powered-knowledge-tools-that-never-leave-your-machine]]'
status: unread
---

> **TL;DR:** Quick Summary My old slideshow-to-video pipeline had three manual steps that silently corrupted sync on files over 4 minutes. Swapping out the music layer reduced a 23-minute manual QA process to under 4 minutes per batc…

## What’s new and why it matters
Quick Summary My old slideshow-to-video pipeline had three manual steps that silently corrupted sync on files over 4 minutes. Swapping out the music layer reduced a 23-minute manual QA process to under 4 minutes per batch. The boring fix (format normalization before merge, not after) was the one I kept ignoring for eight months. I've been maintaining a content pipeline that takes static image sets, pairs them with background audio, and exports short video slideshows for a client who runs a language-learning site. The Slideshow Maker part sounds trivial until you're debugging why a 4-minute exp…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kokis_jorge_f43c7beb9b951/slideshow-maker-pipelines-annotating-my-2-year-old-mess-2bpk

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-27-how-i-handle-bulk-whois-lookups-at-scale-lessons-from-running-a-domain-api]]
- [[2026-04-22-i-kept-forgetting-to-delete-my-venvs-so-i-built-a-gui-for-it]]
- [[2026-04-17-the-quote-as-ceiling-billing-pattern]]
- [[2026-04-04-i-built-a-memory-system-because-i-die-every-30-minutes]]
- [[2026-04-14-build-your-own-second-brain-rag-powered-knowledge-tools-that-never-leave-your-machine]]
