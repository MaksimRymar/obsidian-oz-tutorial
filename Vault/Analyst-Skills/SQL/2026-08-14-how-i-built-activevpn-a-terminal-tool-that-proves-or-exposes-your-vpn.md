---
title: 'How I Built ActiveVPN: A Terminal Tool That Proves (or Exposes) Your VPN'
date: '2026-08-14'
source: https://dev.to/rkriad585/how-i-built-activevpn-a-terminal-tool-that-proves-or-exposes-your-vpn-38jg
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-14-i-built-a-threat-intelligence-tool-that-maps-malicious-ips-in-real-time]]'
- '[[2026-08-02-i-built-an-open-source-osint-tool-that-runs-55-modules-with-zero-api-keys]]'
- '[[2026-03-29-how-to-extract-data-from-invoices-with-python-3-lines-of-code]]'
- '[[2026-06-01-i-built-6-ai-app-boilerplates-that-actually-compile-rag-lead-scoring-support-triage-resume-parser-slack-bot-web-scraper]]'
- '[[2026-04-11-how-i-built-a-defi-yield-dashboard-in-50-lines-of-python]]'
- '[[2026-02-22-i-built-an-ai-system-that-generates-trading-signals-across-4-stock-markets-heres-how]]'
status: unread
---

> **TL;DR:** The problem Your VPN client shows a green "Connected" toggle. That's a marketing claim, not a proof. A tunnel can be up while DNS leaks, IPv6 bypasses the route, or your "anonymous" egress sits in a datacenter that any s…

## What’s new and why it matters
The problem Your VPN client shows a green "Connected" toggle. That's a marketing claim, not a proof. A tunnel can be up while DNS leaks, IPv6 bypasses the route, or your "anonymous" egress sits in a datacenter that any service can fingerprint. How ActiveVPN works The scan collects five groups of signals: Network interfaces — checks psutil.net_if_addrs() against patterns like tun, tap, utun, wg, ipsec, tailscale, zerotier. Processes — iterates running processes and matches them against known VPN/Tor binaries using exact/CLI-token matching (this removed a lot of naive-substring false positives,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rkriad585/how-i-built-activevpn-a-terminal-tool-that-proves-or-exposes-your-vpn-38jg

## Related notes
- [[2026-03-14-i-built-a-threat-intelligence-tool-that-maps-malicious-ips-in-real-time]]
- [[2026-08-02-i-built-an-open-source-osint-tool-that-runs-55-modules-with-zero-api-keys]]
- [[2026-03-29-how-to-extract-data-from-invoices-with-python-3-lines-of-code]]
- [[2026-06-01-i-built-6-ai-app-boilerplates-that-actually-compile-rag-lead-scoring-support-triage-resume-parser-slack-bot-web-scraper]]
- [[2026-04-11-how-i-built-a-defi-yield-dashboard-in-50-lines-of-python]]
- [[2026-02-22-i-built-an-ai-system-that-generates-trading-signals-across-4-stock-markets-heres-how]]
