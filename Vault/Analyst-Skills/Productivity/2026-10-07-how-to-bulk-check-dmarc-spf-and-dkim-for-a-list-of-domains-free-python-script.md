---
title: How to bulk-check DMARC, SPF and DKIM for a list of domains (free Python script)
date: '2026-10-07'
source: https://dev.to/probelane/how-to-bulk-check-dmarc-spf-and-dkim-for-a-list-of-domains-free-python-script-1m6k
domain: Productivity
relevance: 🟡
tags:
- '#library'
- '#productivity'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-05-bulk-domain-age-expiry-and-dns-audit-in-python-rdap-with-whois-fallback]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-09-26-26-of-45-shops-had-no-way-to-reach-them-heres-the-script-i-added]]'
- '[[2026-05-16-automated-domain-investing-with-hard-budget-walls-and-an-ai-council-that-has-to-agree-before-any-money-moves]]'
status: unread
---

> **TL;DR:** Every few weeks someone on Reddit or a sysadmin forum asks some version of: "I have 300 client/prospect domains. How do I check which ones have no DMARC, or a weak SPF, without pasting them one by one into MXToolbox?" He…

## What’s new and why it matters
Every few weeks someone on Reddit or a sysadmin forum asks some version of: "I have 300 client/prospect domains. How do I check which ones have no DMARC, or a weak SPF, without pasting them one by one into MXToolbox?" Here's a small, dependency-light Python script that does exactly that from public DNS, plus the gotchas we hit doing this on real small-business domains. The script pip install dnspython # bulk_dmarc.py - usage: python bulk_dmarc.py domains.txt > results.csv import csv , re , sys import dns.resolver R = dns . resolver . Resolver () R . lifetime = 5 DKIM_SELECTORS = [ " google " ,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/probelane/how-to-bulk-check-dmarc-spf-and-dkim-for-a-list-of-domains-free-python-script-1m6k

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-05-bulk-domain-age-expiry-and-dns-audit-in-python-rdap-with-whois-fallback]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-09-26-26-of-45-shops-had-no-way-to-reach-them-heres-the-script-i-added]]
- [[2026-05-16-automated-domain-investing-with-hard-budget-walls-and-an-ai-council-that-has-to-agree-before-any-money-moves]]
