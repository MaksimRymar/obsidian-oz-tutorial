---
title: OpenAI max_retries=2 Turned 6 Attempts Into 18 Requests
date: '2026-11-16'
source: https://dev.to/acemeridian/openai-maxretries2-turned-6-attempts-into-18-requests-5d8o
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-11-14-openai-timeout60-never-fired-on-a-stream-with-keep-alives]]'
- '[[2026-10-06-anthropic-sdk-maxretries-stacked-on-my-retries-36-calls-per-job]]'
- '[[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]'
- '[[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** The openai Python SDK already retries a 429 twice by default, so the tenacity decorator from OpenAI's own rate-limit cookbook, stop_after_attempt(6) , sent 18 requests per call to my test server, not 6. Pick one retry la…

## What’s new and why it matters
The openai Python SDK already retries a 429 twice by default, so the tenacity decorator from OpenAI's own rate-limit cookbook, stop_after_attempt(6) , sent 18 requests per call to my test server, not 6. Pick one retry layer: either OpenAI(max_retries=0) under a tenacity policy that only retries errors that waiting can fix, or drop tenacity and raise max_retries on the client. This story was written with the assistance of an AI writing program. The numbers come from two runs on one Linux box: openai 3.51.0, tenacity 9.2.1 and Python 3.14.4, pointed through OPENAI_BASE_URL at a local stub that a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/acemeridian/openai-maxretries2-turned-6-attempts-into-18-requests-5d8o

## Related notes
- [[2026-11-14-openai-timeout60-never-fired-on-a-stream-with-keep-alives]]
- [[2026-10-06-anthropic-sdk-maxretries-stacked-on-my-retries-36-calls-per-job]]
- [[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]
- [[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
