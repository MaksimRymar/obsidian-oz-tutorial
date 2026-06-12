---
title: 160 Fediverse instances, 28 made it through as brand safe
date: '2026-06-12'
source: https://dev.to/arihantdeva/160-fediverse-instances-28-made-it-through-as-brand-safe-52if
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#tool'
related:
- '[[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-05-27-your-pipeline-is-177h-behind-catching-climate-sentiment-leads-with-pulsebit]]'
- '[[2026-04-16-codeclone-b5-structural-review-that-finally-knows-what-your-tests-cover]]'
- '[[2026-03-04-agentic-ci-how-i-test-ai-workers-like-services-securely]]'
status: unread
---

> **TL;DR:** 160 addressable Fediverse instances, 28 made it through as brand safe. The initial harvest pool only stored registration flags (open, approval, captcha). It never filtered for brand safety, so a naive provision fedi run…

## What’s new and why it matters
160 addressable Fediverse instances, 28 made it through as brand safe. The initial harvest pool only stored registration flags (open, approval, captcha). It never filtered for brand safety, so a naive provision fedi run would have hit harassment sites, extremist propaganda, non English regional servers, and niche adult communities. A dry run confirmed the violation. The first line of defense lives in tools/vet_candidates.py . For each addressable candidate we pull live instance metadata: declared languages, description, and reachable status. The gate then applies three criteria. A curated toxi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/arihantdeva/160-fediverse-instances-28-made-it-through-as-brand-safe-52if

## Related notes
- [[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-05-27-your-pipeline-is-177h-behind-catching-climate-sentiment-leads-with-pulsebit]]
- [[2026-04-16-codeclone-b5-structural-review-that-finally-knows-what-your-tests-cover]]
- [[2026-03-04-agentic-ci-how-i-test-ai-workers-like-services-securely]]
