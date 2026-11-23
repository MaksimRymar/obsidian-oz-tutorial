---
title: Automate the 28-day “high impressions, low clicks” report with the Search Console
  API
date: '2026-11-23'
source: https://dev.to/proxdigitalagencylondon/automate-the-28-day-high-impressions-low-clicks-report-with-the-search-console-api-4590
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
- '[[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]'
- '[[2026-07-01-how-to-write-a-python-script-that-finds-cannibalized-queries-in-a-search-console-export]]'
- '[[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
status: unread
---

> **TL;DR:** The Search Console API doesn't only filter with equals and contains . Its filter operators include includingRegex and excludingRegex , both using RE2 syntax ( Search Analytics API reference ). That one detail lets you au…

## What’s new and why it matters
The Search Console API doesn't only filter with equals and contains . Its filter operators include includingRegex and excludingRegex , both using RE2 syntax ( Search Analytics API reference ). That one detail lets you automate a review that most people do by hand, one page at a time. The review in question goes like this: give a page 28 days of data, then find the searches where Google shows it often but people rarely click, plus the long, conversational queries that read like questions. Those are the phrases to work into the page. This post turns that into a script you can run on a schedule.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/proxdigitalagencylondon/automate-the-28-day-high-impressions-low-clicks-report-with-the-search-console-api-4590

## Related notes
- [[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
- [[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]
- [[2026-07-01-how-to-write-a-python-script-that-finds-cannibalized-queries-in-a-search-console-export]]
- [[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
