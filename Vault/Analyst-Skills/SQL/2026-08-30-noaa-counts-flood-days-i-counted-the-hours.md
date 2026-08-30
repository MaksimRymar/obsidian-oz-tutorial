---
title: NOAA Counts Flood Days. I Counted the Hours.
date: '2026-08-30'
source: https://dev.to/aws-builders/noaa-counts-flood-days-i-counted-the-hours-5017
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
status: unread
---

> **TL;DR:** What this is: a dataset and a site measuring how long US coastal floods last, not just how often they happen. 137 NOAA tide gauges, every year since 1920, computed from 59.5 million raw hourly readings. Live at floodhour…

## What’s new and why it matters
What this is: a dataset and a site measuring how long US coastal floods last, not just how often they happen. 137 NOAA tide gauges, every year since 1920, computed from 59.5 million raw hourly readings. Live at floodhours.ajithmanmadhan.com . Boston and Galveston flood about the same number of days a year. Thirteen and sixteen. Their flood days are nothing alike. A flood in Boston lasts about ninety minutes. A flood in Galveston lasts about seven and a half hours. The published counts score them the same. A flood day is a binary: did the water cross the local threshold at any point? Water that…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aws-builders/noaa-counts-flood-days-i-counted-the-hours-5017

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
