---
title: Detecting & Blocking Anomalous Traffic with Cloud Anomaly Detector
date: '2026-04-28'
source: https://dev.to/izzyjosh/detecting-blocking-anomalous-traffic-with-cloud-anomaly-detector-2i7n
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-04-26-building-a-real-time-anomaly-detection-engine-for-a-self-hosted-nextcloud-hng-stage-3]]'
- '[[2026-03-14-i-built-a-threat-intelligence-tool-that-maps-malicious-ips-in-real-time]]'
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
- '[[2026-04-14-stock-recommendation-system-using-anthropic-mcp-and-python]]'
- '[[2026-03-17-i-built-a-cognitive-layer-for-ai-agents-that-learns-without-llm-calls]]'
- '[[2026-04-23-4-open-source-tools-to-build-production-ready-ai-voice-agents]]'
status: unread
---

> **TL;DR:** A lightweight, containerized anomaly detection system that monitors traffic in real time, detects abuse patterns, and automatically blocks malicious IPs at the host firewall level. I built a real-time anomaly detection s…

## What’s new and why it matters
A lightweight, containerized anomaly detection system that monitors traffic in real time, detects abuse patterns, and automatically blocks malicious IPs at the host firewall level. I built a real-time anomaly detection system that monitors nginx access logs, computes adaptive rolling baselines per time window, detects traffic anomalies using statistical methods (z-score + spike multipliers), and automatically blocks malicious IPs using host-level iptables rules. The system includes Slack alerts and a live dashboard for observability and debugging. 🧠 Background / Motivation Modern systems face…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/izzyjosh/detecting-blocking-anomalous-traffic-with-cloud-anomaly-detector-2i7n

## Related notes
- [[2026-04-26-building-a-real-time-anomaly-detection-engine-for-a-self-hosted-nextcloud-hng-stage-3]]
- [[2026-03-14-i-built-a-threat-intelligence-tool-that-maps-malicious-ips-in-real-time]]
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
- [[2026-04-14-stock-recommendation-system-using-anthropic-mcp-and-python]]
- [[2026-03-17-i-built-a-cognitive-layer-for-ai-agents-that-learns-without-llm-calls]]
- [[2026-04-23-4-open-source-tools-to-build-production-ready-ai-voice-agents]]
