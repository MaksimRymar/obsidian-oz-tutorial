---
title: I Built a SEC Disclosure-Risk Audit Tool — Here's What It Found on a Real Ticker
  (SNBR)
date: '2026-06-28'
source: https://dev.to/jared_ablon_f27e6e2896913/i-built-a-sec-disclosure-risk-audit-tool-heres-what-it-found-on-a-real-ticker-snbr-24c7
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#presentations'
- '#sql'
- '#tool'
related:
- '[[2026-05-27-i-built-a-free-deepfake-detector-in-3-hours-heres-the-architecture]]'
- '[[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]'
- '[[2026-03-14-i-was-tired-of-parsing-xbrl-so-i-built-a-sec-edgar-api]]'
- '[[2026-06-10-i-built-a-tool-that-generates-api-docs-from-your-source-code---no-annotations-no-server-running-no-swagger-config]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]'
status: unread
---

> **TL;DR:** I Built a SEC Disclosure-Risk Audit Tool — Here's What It Found on a Real Ticker (SNBR) I've been building FilingFirehose for the past few months — a tool that ingests every SEC 8-K, 10-K, 10-Q, S-3, and 13D filing in re…

## What’s new and why it matters
I Built a SEC Disclosure-Risk Audit Tool — Here's What It Found on a Real Ticker (SNBR) I've been building FilingFirehose for the past few months — a tool that ingests every SEC 8-K, 10-K, 10-Q, S-3, and 13D filing in real time and scores each issuer for disclosure risk. This week I shipped the first end-to-end "audit" deliverable: a 12-page forensic write-up on a single ticker, with every red flag traced back to a specific EDGAR accession number. I want to walk through the actual audit it generated on Sleep Number Corp (SNBR) — a real, mid-cap, publicly traded company — because the patterns i…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jared_ablon_f27e6e2896913/i-built-a-sec-disclosure-risk-audit-tool-heres-what-it-found-on-a-real-ticker-snbr-24c7

## Related notes
- [[2026-05-27-i-built-a-free-deepfake-detector-in-3-hours-heres-the-architecture]]
- [[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]
- [[2026-03-14-i-was-tired-of-parsing-xbrl-so-i-built-a-sec-edgar-api]]
- [[2026-06-10-i-built-a-tool-that-generates-api-docs-from-your-source-code---no-annotations-no-server-running-no-swagger-config]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]
