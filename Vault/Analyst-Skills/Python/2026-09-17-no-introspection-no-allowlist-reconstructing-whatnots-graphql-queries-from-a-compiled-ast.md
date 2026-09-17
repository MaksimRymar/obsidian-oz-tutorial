---
title: 'No introspection, no allowlist: reconstructing Whatnot''s GraphQL queries
  from a compiled AST'
date: '2026-09-17'
source: https://dev.to/devil_scrapes/no-introspection-no-allowlist-reconstructing-whatnots-graphql-queries-from-a-compiled-ast-2764
domain: Python
relevance: 🟡
tags:
- '#python'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-08-10-my-ai-agent-found-a-5-sigma-result-on-day-one-i-deleted-it]]'
- '[[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]'
- '[[2026-09-02-pypdf-and-the-pin-that-never-gets-its-fix]]'
- '[[2026-06-04-i-built-a-cache-engine-from-scratch-in-python-and-o1-lfu-eviction-is-sneakier-than-lru]]'
status: unread
---

> **TL;DR:** Quick answer: Whatnot's GraphQL endpoint has no persisted-query allowlist and no introspection . It parses and executes whatever query text you send, validated against the live schema. So you can't ask the server what fi…

## What’s new and why it matters
Quick answer: Whatnot's GraphQL endpoint has no persisted-query allowlist and no introspection . It parses and executes whatever query text you send, validated against the live schema. So you can't ask the server what fields exist — but once you know, you can ask for exactly those, with no cookies, no browser and no session. Two of the three queries this Actor uses are not shipped to client JavaScript at all. If introspection is off, where do the queries come from? Two different places, because the site gets them two different ways. GetUser was recovered by decompiling Apollo Client's own Docu…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/devil_scrapes/no-introspection-no-allowlist-reconstructing-whatnots-graphql-queries-from-a-compiled-ast-2764

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-08-10-my-ai-agent-found-a-5-sigma-result-on-day-one-i-deleted-it]]
- [[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]
- [[2026-09-02-pypdf-and-the-pin-that-never-gets-its-fix]]
- [[2026-06-04-i-built-a-cache-engine-from-scratch-in-python-and-o1-lfu-eviction-is-sneakier-than-lru]]
