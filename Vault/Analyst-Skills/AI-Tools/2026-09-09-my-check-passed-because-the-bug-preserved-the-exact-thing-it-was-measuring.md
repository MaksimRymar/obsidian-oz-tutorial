---
title: My check passed because the bug preserved the exact thing it was measuring
date: '2026-09-09'
source: https://dev.to/mahirhir/my-check-passed-because-the-bug-preserved-the-exact-thing-it-was-measuring-4jp6
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#tool'
related:
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
status: unread
---

> **TL;DR:** I wrote a reconciliation to catch a filter that silently drops fields. It compared how many fields the type declares against how many the filter matched, and raised on a mismatch. I ran it against a broken filter and it…

## What’s new and why it matters
I wrote a reconciliation to catch a filter that silently drops fields. It compared how many fields the type declares against how many the filter matched, and raised on a mismatch. I ran it against a broken filter and it passed. The filter was broken. The check was not lying. The bug preserved the count. filter emitted count-check name-check both good 5 true true true renaming 5 true false false duplicate 10 false true false renaming is (\w+)=(\S+) against a field called risk-level . \w does not cross the hyphen, so it matches from level onward and produces the right value under the wrong name.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mahirhir/my-check-passed-because-the-bug-preserved-the-exact-thing-it-was-measuring-4jp6

## Related notes
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
