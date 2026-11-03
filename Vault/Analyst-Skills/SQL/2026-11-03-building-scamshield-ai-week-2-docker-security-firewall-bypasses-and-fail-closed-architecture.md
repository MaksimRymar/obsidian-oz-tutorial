---
title: 'Building ScamShield AI: Week 2 — Docker Security, Firewall Bypasses, and Fail-Closed
  Architecture'
date: '2026-11-03'
source: https://dev.to/siddharthrane07/building-scamshield-ai-week-2-docker-security-firewall-bypasses-and-fail-closed-architecture-aka
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]'
- '[[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]'
- '[[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]'
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
status: unread
---

> **TL;DR:** 🛡️ ScamShield AI: Week 2 Build Log Hardening Container Boundaries: iptables, SSRF Mitigations & Fail-Closed Sandboxes 🚨 The Journey So Far If you caught Week 1, you know I'm building ScamShield AI — an evidence-grounded…

## What’s new and why it matters
🛡️ ScamShield AI: Week 2 Build Log Hardening Container Boundaries: iptables, SSRF Mitigations & Fail-Closed Sandboxes 🚨 The Journey So Far If you caught Week 1, you know I'm building ScamShield AI — an evidence-grounded threat intelligence platform designed to safely analyze Indian scam SMS messages and WhatsApp forwards (fake KYC alerts, electricity cut-off threats, UPI traps). To safely "click" a scammer's link without letting them compromise our backend infrastructure, we are building an isolated Docker sandbox using Playwright (Headless Chromium) and Mitmproxy (The Network Guard) . This we…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/siddharthrane07/building-scamshield-ai-week-2-docker-security-firewall-bypasses-and-fail-closed-architecture-aka

## Related notes
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]
- [[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]
- [[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
