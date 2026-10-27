---
title: 'JSON-LD, __NEXT_DATA__ and __PRELOADED_STATE__: Where E-commerce Data Actually
  Lives'
date: '2026-10-27'
source: https://dev.to/rslndev/json-ld-nextdata-and-preloadedstate-where-e-commerce-data-actually-lives-5bm3
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-10-16-scraping-workday-job-listings-with-python-the-2000-job-cap-and-two-other-traps]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-09-17-no-introspection-no-allowlist-reconstructing-whatnots-graphql-queries-from-a-compiled-ast]]'
- '[[2026-04-22-mastering-python-lists-through-real-world-use-a-practical-developers-guide]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** Modern store pages ship their data twice: once as HTML for the shopper, and once as JSON for the JavaScript that runs the page. The JSON is usually richer, cleaner and more stable than the markup. Finding it is the singl…

## What’s new and why it matters
Modern store pages ship their data twice: once as HTML for the shopper, and once as JSON for the JavaScript that runs the page. The JSON is usually richer, cleaner and more stable than the markup. Finding it is the single biggest shortcut in e-commerce scraping, as long as you know which of the several JSON blobs to trust. Key takeaways Look in four places, in order: JSON-LD, embedded app state, rendered HTML, and APIs called after load. JSON-LD is easiest to parse but often absent: of five big US retailers we checked, only Best Buy had a schema.org Product with a price. __NEXT_DATA__ exists o…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rslndev/json-ld-nextdata-and-preloadedstate-where-e-commerce-data-actually-lives-5bm3

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-10-16-scraping-workday-job-listings-with-python-the-2000-job-cap-and-two-other-traps]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-09-17-no-introspection-no-allowlist-reconstructing-whatnots-graphql-queries-from-a-compiled-ast]]
- [[2026-04-22-mastering-python-lists-through-real-world-use-a-practical-developers-guide]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
