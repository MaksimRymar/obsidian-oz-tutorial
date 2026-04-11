---
title: I Built an Offline Threat Hunting CLI That Runs Sigma Rules and Maps Everything
  to MITRE ATT&CK
date: '2026-04-11'
source: https://dev.to/tiltedlunar123/i-built-an-offline-threat-hunting-cli-that-runs-sigma-rules-and-maps-everything-to-mitre-attck-5dco
domain: Productivity
relevance: 🔴
tags:
- '#best-practice'
- '#feature'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-01-i-built-a-portable-siem-detection-toolkit-that-converts-sigma-rules-to-splunk-elastic-and-kibana-queries]]'
- '[[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]'
- '[[2026-02-22-python-geospatial-analysis-5-practical-techniques-to-master-location-data-today]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-04-09-i-open-sourced-my-ollama-logging-proxy]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
status: unread
---

> **TL;DR:** Most log analysis workflows assume you have a full SIEM stack running. Splunk, Elastic, Sentinel — they're powerful, but they're also heavy. When I needed to triage Windows security logs during a lab exercise, I didn't w…

## What’s new and why it matters
Most log analysis workflows assume you have a full SIEM stack running. Splunk, Elastic, Sentinel — they're powerful, but they're also heavy. When I needed to triage Windows security logs during a lab exercise, I didn't want to spin up infrastructure. I wanted to point a tool at a folder of logs and get answers. That's why I built ThreatLens — a Python CLI that parses EVTX, JSON, Syslog, and CEF logs offline, runs detection rules (including native Sigma support), correlates multi-stage attacks, and outputs structured alerts mapped to MITRE ATT&CK. No agents, no cloud, no dependencies beyond PyY…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/tiltedlunar123/i-built-an-offline-threat-hunting-cli-that-runs-sigma-rules-and-maps-everything-to-mitre-attck-5dco

## Related notes
- [[2026-04-01-i-built-a-portable-siem-detection-toolkit-that-converts-sigma-rules-to-splunk-elastic-and-kibana-queries]]
- [[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]
- [[2026-02-22-python-geospatial-analysis-5-practical-techniques-to-master-location-data-today]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-04-09-i-open-sourced-my-ollama-logging-proxy]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
