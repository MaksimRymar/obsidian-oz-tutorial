---
title: The WAV said 48 kHz. Why did the test tone play sharp?
date: '2026-11-25'
source: https://dev.to/sparkllm/the-wav-said-48-khz-why-did-the-test-tone-play-sharp-10ja
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-19-my-batch-job-had-a-100-success-rate-and-a-4-corruption-rate]]'
- '[[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]'
- '[[2026-06-24-i-got-tired-of-cryptic-python-error-messages-so-i-built-a-vs-code-extension-that-fixes-them-automatically]]'
- '[[2026-10-06-anthropic-sdk-maxretries-stacked-on-my-retries-36-calls-per-job]]'
- '[[2026-09-12-i-debugged-a-snapshot-for-48-hours-datetimenow-had-a-hometown]]'
- '[[2026-09-24-what-a-server-knows-about-you-before-it-reads-a-single-header]]'
status: unread
---

> **TL;DR:** The delivery brief asked for 48 kHz. The WAV header agreed. Then the editor played the reference tone. What should have been 1,000 Hz sounded sharp. Kevinchen1104 built that discrepancy into a synthetic test recording. T…

## What’s new and why it matters
The delivery brief asked for 48 kHz. The WAV header agreed. Then the editor played the reference tone. What should have been 1,000 Hz sounded sharp. Kevinchen1104 built that discrepancy into a synthetic test recording. The samples were recorded for 44.1 kHz playback, but the header was changed to 48 kHz. Playing the same samples faster moved the measured peak to 1,088.42 Hz in both channels. ffprobe and the decoder both reported the header rate correctly. Spark-X2.6-4B ran locally on four CPU threads and read the written brief. Asked for the rate in Hz, it returned 48 . Asked which passage spe…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sparkllm/the-wav-said-48-khz-why-did-the-test-tone-play-sharp-10ja

## Related notes
- [[2026-08-19-my-batch-job-had-a-100-success-rate-and-a-4-corruption-rate]]
- [[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]
- [[2026-06-24-i-got-tired-of-cryptic-python-error-messages-so-i-built-a-vs-code-extension-that-fixes-them-automatically]]
- [[2026-10-06-anthropic-sdk-maxretries-stacked-on-my-retries-36-calls-per-job]]
- [[2026-09-12-i-debugged-a-snapshot-for-48-hours-datetimenow-had-a-hometown]]
- [[2026-09-24-what-a-server-knows-about-you-before-it-reads-a-single-header]]
