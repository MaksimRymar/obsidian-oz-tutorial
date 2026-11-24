---
title: 'Uptime Kuma 2 with uptime-kuma-api 1.x: socket timeouts and a dead healer'
date: '2026-11-24'
source: https://dev.to/iam-tech/uptime-kuma-2-with-uptime-kuma-api-1x-socket-timeouts-and-a-dead-healer-bgh
domain: SQL
relevance: 🔴
tags:
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]'
- '[[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]'
- '[[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]'
status: unread
---

> **TL;DR:** I've got a small Python script I call the healer. Every 5 minutes it logs in to Uptime Kuma, asks which monitors are down, and tries to fix them. If a monitor is down for 2 runs in a row it restarts the service. If that…

## What’s new and why it matters
I've got a small Python script I call the healer. Every 5 minutes it logs in to Uptime Kuma, asks which monitors are down, and tries to fix them. If a monitor is down for 2 runs in a row it restarts the service. If that doesn't bring it back, it reboots the container, with a cap on how many reboots it'll do in an hour. It's the bit of my homelab that's meant to fix things while I'm asleep. On 9 August 2026 I opened its log. It was about 2.4 MB of Python tracebacks. It had been dead for months. Not dead once, either. Dead twice, for two completely different reasons, one after the other. And nex…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/iam-tech/uptime-kuma-2-with-uptime-kuma-api-1x-socket-timeouts-and-a-dead-healer-bgh

## Related notes
- [[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]
- [[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]
- [[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]
