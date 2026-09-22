---
title: Your Python Service Grows 40 MB a Day and Then OOMs. Here's How to Find the
  Leak in an Hour
date: '2026-09-22'
source: https://dev.to/mdyer94/your-python-service-grows-40-mb-a-day-and-then-ooms-heres-how-to-find-the-leak-in-an-hour-291d
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-06-02-claude-api-from-scratch-your-first-working-call-in-30-minutes-2026]]'
- '[[2026-09-02-the-impact-radius-refactor-around-every-caller-you-cant-see]]'
- '[[2026-07-24-you-dont-need-a-backend-to-store-form-submissions-you-need-a-place-to-ask-how-many]]'
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
status: unread
---

> **TL;DR:** A gunicorn worker with a 512 MB --max-requests -less config starts at 180 MB RSS. Three days later it's 480 MB. On day four the OOM killer takes it, the health check flaps, and your pager fires at 3 AM. Restarting the wo…

## What’s new and why it matters
A gunicorn worker with a 512 MB --max-requests -less config starts at 180 MB RSS. Three days later it's 480 MB. On day four the OOM killer takes it, the health check flaps, and your pager fires at 3 AM. Restarting the worker fixes it for exactly three days. gc.collect() in a debug endpoint reclaims 2 MB — which tells you the objects aren't garbage, they're referenced . Something is holding them. The reflex is to reach for gc.get_objects() and dump counts. Don't. That gives you a 200,000-line wall of <class 'dict'> and tells you nothing. The workflow below is what actually works: tracemalloc to…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mdyer94/your-python-service-grows-40-mb-a-day-and-then-ooms-heres-how-to-find-the-leak-in-an-hour-291d

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-06-02-claude-api-from-scratch-your-first-working-call-in-30-minutes-2026]]
- [[2026-09-02-the-impact-radius-refactor-around-every-caller-you-cant-see]]
- [[2026-07-24-you-dont-need-a-backend-to-store-form-submissions-you-need-a-place-to-ask-how-many]]
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
