---
title: Building a real-time anomaly detection engine for a self-hosted Nextcloud (HNG
  Stage 3)
date: '2026-04-26'
source: https://dev.to/ibraheembello/building-a-real-time-anomaly-detection-engine-for-a-self-hosted-nextcloud-hng-stage-3-59km
domain: Presentations
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#presentations'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-03-16-build-an-mcp-server-that-finds-your-rag-chatbots-blind-spots]]'
- '[[2026-04-21-is-chatgpt-citing-your-site-a-conceptual-guide-to-geo-tracking-in-python-published]]'
- '[[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
status: unread
---

> **TL;DR:** TL;DR — I built a Python daemon that watches every HTTP request hitting an Nginx reverse proxy, learns what normal traffic looks like in real time, and automatically bans IPs that misbehave by inserting iptables rules at…

## What’s new and why it matters
TL;DR — I built a Python daemon that watches every HTTP request hitting an Nginx reverse proxy, learns what normal traffic looks like in real time, and automatically bans IPs that misbehave by inserting iptables rules at the kernel level. It alerts to Slack and ships its live metrics on a public dashboard. This post explains every piece in beginner-friendly terms. Live demo: http://cloud-ng-anomaly.duckdns.org Source code: https://github.com/ibraheembello/hng-stage3-anomaly-detector What the project does and why it matters Imagine you run a public website — say, a self-hosted Google-Drive-styl…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ibraheembello/building-a-real-time-anomaly-detection-engine-for-a-self-hosted-nextcloud-hng-stage-3-59km

## Related notes
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-03-16-build-an-mcp-server-that-finds-your-rag-chatbots-blind-spots]]
- [[2026-04-21-is-chatgpt-citing-your-site-a-conceptual-guide-to-geo-tracking-in-python-published]]
- [[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
