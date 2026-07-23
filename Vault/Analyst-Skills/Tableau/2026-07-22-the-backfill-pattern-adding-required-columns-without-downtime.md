---
title: 'The Backfill Pattern: Adding Required Columns Without Downtime'
date: '2026-07-22'
source: https://dev.to/thdr/the-backfill-pattern-adding-required-columns-without-downtime-5e53
domain: Tableau
relevance: 🟡
tags:
- '#best-practice'
- '#tableau'
- '#tool'
related:
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-06-20-green-unit-tests-are-a-comfort-blanket]]'
- '[[2026-07-07-the-caller-heard-silence-for-two-seconds-before-the-agent-spoke]]'
- '[[2026-06-28-our-sql-server-loop-kept-writing-the-previous-rows-value]]'
status: unread
---

> **TL;DR:** Adding a required column to a table sounds like the simplest task in the world. Then you try it on a table that's already in production, with code writing to it every second, and you find out why it isn't. There are two…

## What’s new and why it matters
Adding a required column to a table sounds like the simplest task in the world. Then you try it on a table that's already in production, with code writing to it every second, and you find out why it isn't. There are two ways people usually try this, and both break. Add the column as NOT NULL right away, and the migration fails outright, or it locks the table while it scans millions of existing rows that have no value to give it. Add it as nullable instead and move on, and nothing enforces the constraint at all. Six months later half the rows are still null, and the column is "required" only in…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/thdr/the-backfill-pattern-adding-required-columns-without-downtime-5e53

## Related notes
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-06-20-green-unit-tests-are-a-comfort-blanket]]
- [[2026-07-07-the-caller-heard-silence-for-two-seconds-before-the-agent-spoke]]
- [[2026-06-28-our-sql-server-loop-kept-writing-the-previous-rows-value]]
