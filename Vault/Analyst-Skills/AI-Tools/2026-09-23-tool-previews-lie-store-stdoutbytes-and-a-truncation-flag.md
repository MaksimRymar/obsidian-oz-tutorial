---
title: Tool Previews Lie. Store stdout_bytes and a Truncation Flag.
date: '2026-09-23'
source: https://dev.to/apprs_6334/tool-previews-lie-store-stdoutbytes-and-a-truncation-flag-37h7
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-08-charge-wait-time-to-the-same-job]]'
- '[[2026-08-19-my-batch-job-had-a-100-success-rate-and-a-4-corruption-rate]]'
- '[[2026-09-03-record-four-cli-channels-before-you-change-one-flag]]'
- '[[2026-09-07-gate-agent-success-on-closed-spans]]'
- '[[2026-08-14-structured-json-app-logs-that-survive-a-vendor-switch-what-a-small-saas-should-check]]'
- '[[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]'
status: unread
---

> **TL;DR:** A coding agent closed the flaky test ticket. The JSONL span showed pytest and a short preview. The next human run failed in the same module. The wrapper had capped stdout at 8192 bytes. The assertion text started after t…

## What’s new and why it matters
A coding agent closed the flaky test ticket. The JSONL span showed pytest and a short preview. The next human run failed in the same module. The wrapper had capped stdout at 8192 bytes. The assertion text started after that cap. The model never read the failing lines. This is not a prompt problem first. It is missing I/O metadata on the tool span. The failure mode Most agent traces store a short text preview. They also store a loose success flag. That pair cannot describe a clipped pipe. Three wrappers hide the real tool result: Head-cap keeps only the first N bytes. Tail-cap keeps only the la…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/apprs_6334/tool-previews-lie-store-stdoutbytes-and-a-truncation-flag-37h7

## Related notes
- [[2026-09-08-charge-wait-time-to-the-same-job]]
- [[2026-08-19-my-batch-job-had-a-100-success-rate-and-a-4-corruption-rate]]
- [[2026-09-03-record-four-cli-channels-before-you-change-one-flag]]
- [[2026-09-07-gate-agent-success-on-closed-spans]]
- [[2026-08-14-structured-json-app-logs-that-survive-a-vendor-switch-what-a-small-saas-should-check]]
- [[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]
