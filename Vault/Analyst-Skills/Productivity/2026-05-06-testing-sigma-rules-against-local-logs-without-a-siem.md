---
title: Testing Sigma Rules Against Local Logs Without a SIEM
date: '2026-05-06'
source: https://dev.to/tiltedlunar123/testing-sigma-rules-against-local-logs-without-a-siem-1cp9
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#productivity'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-01-i-built-a-portable-siem-detection-toolkit-that-converts-sigma-rules-to-splunk-elastic-and-kibana-queries]]'
- '[[2026-04-11-i-built-an-offline-threat-hunting-cli-that-runs-sigma-rules-and-maps-everything-to-mitre-attck]]'
- '[[2026-04-21-i-spent-6-months-obsessing-over-mt5-bot-logic-heres-what-finally-clicked]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]'
status: unread
---

> **TL;DR:** I'd written a few Sigma rules for my home lab and wanted to know if they actually fired on real Sysmon events. The standard answer is "deploy to Wazuh and replay logs". That's a lot of overhead when I just want to confir…

## What’s new and why it matters
I'd written a few Sigma rules for my home lab and wanted to know if they actually fired on real Sysmon events. The standard answer is "deploy to Wazuh and replay logs". That's a lot of overhead when I just want to confirm a regex matches. So I built SIEMForge. It's a Python CLI that loads Sigma YAML files, parses the detection logic, and matches it against JSON, JSONL, syslog, or CSV log files locally. No SIEM required. This post is the messy version of how it came together. The final code is on GitHub at github.com/TiltedLunar123/SIEMForge. The problem I had ten Sigma rules covering things li…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tiltedlunar123/testing-sigma-rules-against-local-logs-without-a-siem-1cp9

## Related notes
- [[2026-04-01-i-built-a-portable-siem-detection-toolkit-that-converts-sigma-rules-to-splunk-elastic-and-kibana-queries]]
- [[2026-04-11-i-built-an-offline-threat-hunting-cli-that-runs-sigma-rules-and-maps-everything-to-mitre-attck]]
- [[2026-04-21-i-spent-6-months-obsessing-over-mt5-bot-logic-heres-what-finally-clicked]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]
