---
title: 'Scraping Greenhouse Job Boards (boards-api.greenhouse.io): Four Quirks That
  Break Parsers'
date: '2026-11-26'
source: https://dev.to/devsignal_eng/scraping-greenhouse-job-boards-boards-apigreenhouseio-four-quirks-that-break-parsers-3435
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-11-24-how-to-get-jobs-from-the-greenhouse-job-board-api]]'
- '[[2026-11-11-i-aggregated-3-ats-job-boards-greenhouse-lever-ashby-into-one-normalized-dataset-heres-what-i-learned]]'
- '[[2026-10-26-how-to-pull-job-postings-straight-from-company-career-sites-greenhouse-lever-ashby-workday-as-json]]'
- '[[2026-08-08-merging-job-postings-from-ten-ats-platforms-into-one-schema-and-the-four-fields-that-fight-back]]'
- '[[2026-11-09-how-to-get-job-listings-from-seek-new-zealand-with-an-api-python-node-or-no-code]]'
- '[[2026-11-18-i-built-one-job-market-dashboard-in-tableau-and-power-bi-to-learn-both-properly]]'
status: unread
---

> **TL;DR:** Greenhouse is still the single largest job board source across mid-market and late-stage tech companies. Out of 81 AI and devtools companies we benchmarked, 31 boards (5,214 open roles) ran on Greenhouse, including anthr…

## What’s new and why it matters
Greenhouse is still the single largest job board source across mid-market and late-stage tech companies. Out of 81 AI and devtools companies we benchmarked, 31 boards (5,214 open roles) ran on Greenhouse, including anthropic.com (500 tracked roles, median $335,000 ), stripe.com (500 roles), cloudflare.com (500 roles, median $207,500 ), databricks.com (500 roles, median $213,750 ), datadoghq.com (386 roles), and coinbase.com (250 roles, 89.2% remote). The public JSON endpoint requires no API key and returns an entire company's job board in one GET: curl -sS "https://boards-api.greenhouse.io/v1/…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/devsignal_eng/scraping-greenhouse-job-boards-boards-apigreenhouseio-four-quirks-that-break-parsers-3435

## Related notes
- [[2026-11-24-how-to-get-jobs-from-the-greenhouse-job-board-api]]
- [[2026-11-11-i-aggregated-3-ats-job-boards-greenhouse-lever-ashby-into-one-normalized-dataset-heres-what-i-learned]]
- [[2026-10-26-how-to-pull-job-postings-straight-from-company-career-sites-greenhouse-lever-ashby-workday-as-json]]
- [[2026-08-08-merging-job-postings-from-ten-ats-platforms-into-one-schema-and-the-four-fields-that-fight-back]]
- [[2026-11-09-how-to-get-job-listings-from-seek-new-zealand-with-an-api-python-node-or-no-code]]
- [[2026-11-18-i-built-one-job-market-dashboard-in-tableau-and-power-bi-to-learn-both-properly]]
