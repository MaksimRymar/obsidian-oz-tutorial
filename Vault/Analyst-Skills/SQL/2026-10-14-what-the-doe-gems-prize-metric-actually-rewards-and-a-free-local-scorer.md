---
title: What the DOE GEMS Prize metric actually rewards (and a free local scorer)
date: '2026-10-14'
source: https://dev.to/munimv2/what-the-doe-gems-prize-metric-actually-rewards-and-a-free-local-scorer-4054
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-06-02-deepseek-vs-qwen-vs-kimi-vs-glm-which-chinese-ai-model-actually-wins-in-2026]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-08-21-how-to-comment-in-sql----and-and-the-two-traps-that-break-a-query]]'
- '[[2026-08-26-python-for-data-analytics-a-hands-on-field-guide]]'
status: unread
---

> **TL;DR:** The DOE GEMS Prize on DrivenData ($300,000, closes 3 December 2026) asks for a map of hidden geologic faults in western Nevada, scored with a distance-weighted Tversky index. I read the metric closely and wrote an open l…

## What’s new and why it matters
The DOE GEMS Prize on DrivenData ($300,000, closes 3 December 2026) asks for a map of hidden geologic faults in western Nevada, scored with a distance-weighted Tversky index. I read the metric closely and wrote an open local scorer and baseline so I could reason about it. Three things fell out that changed how I would build a submission. 1. Recall is worth four times precision. The metric is TP / (TP + 0.2 FP + 0.8 FN). A missed fault pixel costs 0.8; a false alarm costs 0.2. That is a strong hint to predict generously. 2. There is a closed-form threshold. If your model can reach a score of la…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/munimv2/what-the-doe-gems-prize-metric-actually-rewards-and-a-free-local-scorer-4054

## Related notes
- [[2026-06-02-deepseek-vs-qwen-vs-kimi-vs-glm-which-chinese-ai-model-actually-wins-in-2026]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-08-21-how-to-comment-in-sql----and-and-the-two-traps-that-break-a-query]]
- [[2026-08-26-python-for-data-analytics-a-hands-on-field-guide]]
