---
title: 'Two requests, one rule, two rows: fixing the INSERT ... WHERE NOT EXISTS race
  in PostgreSQL'
date: '2026-10-29'
source: https://dev.to/talentopsystems/two-requests-one-rule-two-rows-fixing-the-insert-where-not-exists-race-in-postgresql-dfj
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
status: unread
---

> **TL;DR:** A rule like "one comment per user per hour" looks easy. You check for a recent row, and you only insert if there is none. It works in every test you write by hand. Then two requests arrive at the same moment, and the rul…

## What’s new and why it matters
A rule like "one comment per user per hour" looks easy. You check for a recent row, and you only insert if there is none. It works in every test you write by hand. Then two requests arrive at the same moment, and the rule quietly breaks. We set up the exact case on PostgreSQL 17.5, made it fail on purpose, and tried four fixes. Every number below comes from those runs. The question Someone on r/PostgreSQL asked about this query. The goal was to let a user post only one comment per hour: INSERT INTO comments ( user_id , content ) SELECT : user_id , 'my comment' WHERE NOT EXISTS ( SELECT 1 FROM…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/talentopsystems/two-requests-one-rule-two-rows-fixing-the-insert-where-not-exists-race-in-postgresql-dfj

## Related notes
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
