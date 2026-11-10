---
title: Counting hurricane passes per Caribbean island with NOAA HURDAT2
date: '2026-11-10'
source: https://dev.to/gladori/counting-hurricane-passes-per-caribbean-island-with-noaa-hurdat2-1b5n
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#support-analytics'
- '#tool'
related:
- '[[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]'
- '[[2026-08-30-funnel-conversion-in-sql-and-the-step-that-shows-100]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
status: unread
---

> **TL;DR:** Is Aruba really safer from hurricanes than St. Barts? NOAA keeps the record that answers it in one plain text file. HURDAT2 is the National Hurricane Center's best-track database, and it lists every known Atlantic storm…

## What’s new and why it matters
Is Aruba really safer from hurricanes than St. Barts? NOAA keeps the record that answers it in one plain text file. HURDAT2 is the National Hurricane Center's best-track database, and it lists every known Atlantic storm since 1851 with its position and wind every six hours. About 80 lines of standard-library Python turn that file into a count per island. Over 1966 to 2025, the script below finds one hurricane within 50 nautical miles of Aruba. For Virgin Gorda it finds twelve. How a HURDAT2 file is laid out The file stacks blocks. Each block opens with a header line, and a set number of track…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/gladori/counting-hurricane-passes-per-caribbean-island-with-noaa-hurdat2-1b5n

## Related notes
- [[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]
- [[2026-08-30-funnel-conversion-in-sql-and-the-step-that-shows-100]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
