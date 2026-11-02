---
title: 'AWS FinOps Field Notes (2026-11-02): Eliminating Idle NAT Gateways & Unattached
  EIPs with Python'
date: '2026-11-02'
source: https://dev.to/ace7coder/aws-finops-field-notes-2026-11-02-eliminating-idle-nat-gateways-unattached-eips-with-python-39ga
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-08-23-i-got-28-tps-out-of-free-kaggle-gpus-heres-what-it-took]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-08-02-i-built-an-open-source-osint-tool-that-runs-55-modules-with-zero-api-keys]]'
- '[[2026-03-02-how-to-schedule-python-scripts-to-run-automatically]]'
- '[[2026-04-10-free-kokoro-tts-api-open-source-voice-synthesis-with-no-monthly-fee]]'
- '[[2026-03-05-i-built-a-python-library-to-make-tcp-networking-as-simple-as-fastapi]]'
status: unread
---

> **TL;DR:** While auditing cloud infrastructure costs this week, recurring configuration gaps continue to quietly inflate monthly cloud bills. Field Insight: The Hidden Cost Trap Tim O'Brien: Says fifty abandoned 100 GB unattached E…

## What’s new and why it matters
While auditing cloud infrastructure costs this week, recurring configuration gaps continue to quietly inflate monthly cloud bills. Field Insight: The Hidden Cost Trap Tim O'Brien: Says fifty abandoned 100 GB unattached EBS volumes cost $500/month ($6k/year), and that clearing a couple hundred forgotten S3 buckets and EBS volumes is a program rather than a script because every terabyte needs an owner to justify it. Automated Detection: Auditing Idle NAT Gateways and Unattached Elastic IPs with Boto3 import boto3 from datetime import datetime , timedelta , timezone def audit_idle_network_costs (…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ace7coder/aws-finops-field-notes-2026-11-02-eliminating-idle-nat-gateways-unattached-eips-with-python-39ga

## Related notes
- [[2026-08-23-i-got-28-tps-out-of-free-kaggle-gpus-heres-what-it-took]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-08-02-i-built-an-open-source-osint-tool-that-runs-55-modules-with-zero-api-keys]]
- [[2026-03-02-how-to-schedule-python-scripts-to-run-automatically]]
- [[2026-04-10-free-kokoro-tts-api-open-source-voice-synthesis-with-no-monthly-fee]]
- [[2026-03-05-i-built-a-python-library-to-make-tcp-networking-as-simple-as-fastapi]]
