---
title: Your Discord bot's timestamp says the year 58970 (I tested 16 edge cases)
date: '2026-11-05'
source: https://dev.to/fazal_bhinder/your-discord-bots-timestamp-says-the-year-58970-i-tested-16-edge-cases-403e
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-12-espn-scores-scraper-a-game-that-has-not-started-still-shows-0-0]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]'
- '[[2026-07-09-create-a-serp-diff-table-for-titles-urls-and-positions]]'
status: unread
---

> **TL;DR:** Discord turns <t:1798765200:F> into a date shown in each reader's own time zone. The format is documented, but what Discord does with bad input isn't. Bots generate these strings, and bots get the input wrong, so on 4 No…

## What’s new and why it matters
Discord turns <t:1798765200:F> into a date shown in each reader's own time zone. The format is documented, but what Discord does with bad input isn't. Bots generate these strings, and bots get the input wrong, so on 4 November 2026 I sent 16 malformed or extreme codes to a private server from the Discord web client and read back what rendered. Code What it tests Discord showed <t:1798765200:F> Normal Friday, January 1, 2027 at 6:30 AM <t:1798765200000:F> Milliseconds by mistake Tuesday, August 7, 58970 at 9:30 PM <t:0:F> Zero Thursday, January 1, 1970 at 5:30 AM <t:-86400:F> Negative Wednesday…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/fazal_bhinder/your-discord-bots-timestamp-says-the-year-58970-i-tested-16-edge-cases-403e

## Related notes
- [[2026-10-12-espn-scores-scraper-a-game-that-has-not-started-still-shows-0-0]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]
- [[2026-07-09-create-a-serp-diff-table-for-titles-urls-and-positions]]
