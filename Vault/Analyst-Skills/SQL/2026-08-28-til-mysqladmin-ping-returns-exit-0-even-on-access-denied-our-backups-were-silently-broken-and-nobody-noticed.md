---
title: TIL mysqladmin ping returns exit 0 even on Access Denied. our backups were
  silently broken and nobody noticed
date: '2026-08-28'
source: https://dev.to/knutt3/til-mysqladmin-ping-returns-exit-0-even-on-access-denied-our-backups-were-silently-broken-and-5bjk
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-08-17-a-finished-scraper-sat-on-a-git-branch-for-19-days-nothing-noticed]]'
- '[[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-08-05-3-async-python-patterns-i-wish-i-learned-sooner-with-real-code]]'
status: unread
---

> **TL;DR:** so our mysql healthcheck is mysqladmin ping -uroot -p$MYSQL_ROOT_PASSWORD. i figured since we're passing the password it's actually checking auth too, right? wrong lol. turns out mysqladmin ping returns exit 0 even when…

## What’s new and why it matters
so our mysql healthcheck is mysqladmin ping -uroot -p$MYSQL_ROOT_PASSWORD. i figured since we're passing the password it's actually checking auth too, right? wrong lol. turns out mysqladmin ping returns exit 0 even when it gets Access Denied back. apparently that's just how it works, the server responded so technically it's "alive", doesn't matter if it refused you. container's been sitting there green this whole time. meanwhile mysqldump is out here failing with Access Denied every single night and just writing a basically empty .gz file. our backup script does something like docker exec ...…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/knutt3/til-mysqladmin-ping-returns-exit-0-even-on-access-denied-our-backups-were-silently-broken-and-5bjk

## Related notes
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-08-17-a-finished-scraper-sat-on-a-git-branch-for-19-days-nothing-noticed]]
- [[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-08-05-3-async-python-patterns-i-wish-i-learned-sooner-with-real-code]]
