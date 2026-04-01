---
title: I built a portable SIEM detection toolkit that converts Sigma rules to Splunk,
  Elastic, and Kibana queries
date: '2026-04-01'
source: https://dev.to/tiltedlunar123/i-built-a-portable-siem-detection-toolkit-that-converts-sigma-rules-to-splunk-elastic-and-kibana-412o
domain: Productivity
relevance: 🔴
tags:
- '#ai'
- '#library'
- '#productivity'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-03-10-data-forge-vs-mockaroo-vs-fakerjs-i-tested-all-3-so-you-dont-have-to]]'
- '[[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-03-06-how-to-detect-renewable-energy-sentiment-shifts-with-the-pulsebit-api-python]]'
status: unread
---

> **TL;DR:** The problem If you've ever tried to manage detection content across different SIEMs, you know the pain. Sigma rules live in one folder, your Sysmon config is somewhere else, Wazuh custom rules are in yet another director…

## What’s new and why it matters
The problem If you've ever tried to manage detection content across different SIEMs, you know the pain. Sigma rules live in one folder, your Sysmon config is somewhere else, Wazuh custom rules are in yet another directory, and none of it maps cleanly back to MITRE ATT&CK. Converting rules between SIEM formats usually means installing sigmac or setting up a whole pipeline just to get a Splunk query out of a YAML file. I'm a cybersecurity student and I got tired of this workflow in my home lab, so I built SIEMForge — a single Python CLI that keeps all your detection content in one place and conv…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/tiltedlunar123/i-built-a-portable-siem-detection-toolkit-that-converts-sigma-rules-to-splunk-elastic-and-kibana-412o

## Related notes
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-03-10-data-forge-vs-mockaroo-vs-fakerjs-i-tested-all-3-so-you-dont-have-to]]
- [[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-03-06-how-to-detect-renewable-energy-sentiment-shifts-with-the-pulsebit-api-python]]
