---
title: I built an API that checks whether SEC financial data adds up
date: '2026-09-28'
source: https://dev.to/dominique_church_a9abd890/i-built-an-api-that-checks-whether-sec-financial-data-adds-up-kjn
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-03-14-i-was-tired-of-parsing-xbrl-so-i-built-a-sec-edgar-api]]'
- '[[2026-09-28-your-dashboard-is-green-and-the-number-is-wrong-the-sql-checks-i-schedule-next-to-every-metric]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]'
status: unread
---

> **TL;DR:** I'm a solo developer in Canada, and I built BalanceProof: an API for SEC EDGAR fundamentals on 6,000+ US public companies, where every balance sheet, income statement and cash flow is checked against its own totals befor…

## What’s new and why it matters
I'm a solo developer in Canada, and I built BalanceProof: an API for SEC EDGAR fundamentals on 6,000+ US public companies, where every balance sheet, income statement and cash flow is checked against its own totals before you get it. The video above is the 33-second version. This post is the longer one: what it does, why I bothered, and how to try it for free. The problem If you have ever pulled fundamentals out of SEC filings yourself, you know the numbers are not as tidy as the filings look on paper. XBRL is flexible, which is great for filers and painful for anyone reading it in bulk. The s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dominique_church_a9abd890/i-built-an-api-that-checks-whether-sec-financial-data-adds-up-kjn

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-03-14-i-was-tired-of-parsing-xbrl-so-i-built-a-sec-edgar-api]]
- [[2026-09-28-your-dashboard-is-green-and-the-number-is-wrong-the-sql-checks-i-schedule-next-to-every-metric]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]
