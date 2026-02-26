---
title: 'Rebuilding My Home Lab Dashboard: From 4 Nodes to 7, SSH Key Distribution,
  and Status Badges'
date: '2026-02-26'
source: https://dev.to/linou518/rebuilding-my-home-lab-dashboard-from-4-nodes-to-7-ssh-key-distribution-and-status-badges-242h
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#tool'
- '#zendesk'
related:
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-02-23-getting-started-with-trinity-pattern-in-10-minutes]]'
- '[[2026-02-22-no-wifi-no-problem-using-electricsql-to-implement-local-first-syncing]]'
- '[[2026-02-23-flask-vs-nodejs-choosing-the-right-backend-framework-for-2026]]'
- '[[2026-02-25-beyond-to-do-lists-building-a-closed-loop-health-agent-with-langgraph-and-google-calendar]]'
- '[[2026-02-25-finally-stopped-guessing-my-betaflight-pids---heres-what-worked]]'
status: unread
---

> **TL;DR:** I recently did a major refactor of my home lab Dashboard. The trigger was simple: the number of nodes I manage had grown, but I left the old 4-node setup untouched — and the guilt finally caught up with me. Problems with…

## What’s new and why it matters
I recently did a major refactor of my home lab Dashboard. The trigger was simple: the number of nodes I manage had grown, but I left the old 4-node setup untouched — and the guilt finally caught up with me. Problems with the Old Setup The old Dashboard (v1) managed these 4 nodes: T440 (joe) GMK1 through GMK3 In reality, 7 machines were running. Excluding infra and web (which handle infrastructure services), 6 nodes plus joe were in active operation. The Dashboard was completely out of sync with reality. Migrating to the New Setup Updating the Node Definition NODES = [ { " id " : " joe " , " ip…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/linou518/rebuilding-my-home-lab-dashboard-from-4-nodes-to-7-ssh-key-distribution-and-status-badges-242h

## Related notes
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-02-23-getting-started-with-trinity-pattern-in-10-minutes]]
- [[2026-02-22-no-wifi-no-problem-using-electricsql-to-implement-local-first-syncing]]
- [[2026-02-23-flask-vs-nodejs-choosing-the-right-backend-framework-for-2026]]
- [[2026-02-25-beyond-to-do-lists-building-a-closed-loop-health-agent-with-langgraph-and-google-calendar]]
- [[2026-02-25-finally-stopped-guessing-my-betaflight-pids---heres-what-worked]]
