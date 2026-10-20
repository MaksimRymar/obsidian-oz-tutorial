---
title: Python's mutable default argument bug, run one call at a time
date: '2026-10-20'
source: https://dev.to/realdev9868/pythons-mutable-default-argument-bug-run-one-call-at-a-time-5h9j
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-09-02-the-impact-radius-refactor-around-every-caller-you-cant-see]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-19-faq-five-myths-about-tests-the-agent-wrote-for-itself]]'
status: unread
---

> **TL;DR:** This function looks fine. It adds a tag to a list and returns the list. If you don't pass a list, it starts a new empty one. At least that's what it seems to do. def add_tag ( tag , tags = []): tags . append ( tag ) retu…

## What’s new and why it matters
This function looks fine. It adds a tag to a list and returns the list. If you don't pass a list, it starts a new empty one. At least that's what it seems to do. def add_tag ( tag , tags = []): tags . append ( tag ) return tags print ( add_tag ( " python " )) print ( add_tag ( " sql " )) print ( add_tag ( " dsa " , [])) print ( add_tag ( " git " )) [ 'python' ] [ 'python' , 'sql' ] [ 'dsa' ] [ 'python' , 'sql' , 'git' ] The first call is fine. The second call returns ['python', 'sql'] , even though we never passed a list. The third call passed its own list, so it got a clean result. Then the f…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/realdev9868/pythons-mutable-default-argument-bug-run-one-call-at-a-time-5h9j

## Related notes
- [[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-09-02-the-impact-radius-refactor-around-every-caller-you-cant-see]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-19-faq-five-myths-about-tests-the-agent-wrote-for-itself]]
