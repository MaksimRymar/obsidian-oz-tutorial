---
title: Broken links in docs are silent. This Python CLI names the broken kind.
date: '2026-11-09'
source: https://dev.to/haiderstudio/broken-links-in-docs-are-silent-this-python-cli-names-the-broken-kind-16li
domain: Productivity
relevance: 🟡
tags:
- '#best-practice'
- '#library'
- '#productivity'
- '#python'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-02-22-md-files-connector-stop-losing-track-of-your-markdown-docs]]'
- '[[2026-07-28-why-schema-drift-goes-undetected]]'
- '[[2026-09-26-your-link-previews-are-blank-because-ogimage-is-missing-here-is-a-stdlib-only-python-fix]]'
- '[[2026-10-28-check-a-shopify-product-csv-for-missing-prices-and-images-before-you-import-it]]'
- '[[2026-11-04-reading-medium-articles-by-tag-author-and-publication-with-rss-and-where-it-stops]]'
status: unread
---

> **TL;DR:** You update a docs page, move a file, rename a heading. Nothing breaks loudly. A reader clicks a link weeks later and lands on a 404 — or worse, on the right page with the wrong anchor, staring at the top while the sectio…

## What’s new and why it matters
You update a docs page, move a file, rename a heading. Nothing breaks loudly. A reader clicks a link weeks later and lands on a 404 — or worse, on the right page with the wrong anchor, staring at the top while the section they wanted is three screens down. Most link checkers give you one word: broken. This one tells you which kind of broken, because the fix is different. broken-link-checker-cli is a Python CLI. Standard library only. It scans .md , .markdown and .html files, checks every link for real, and reports each link as one of three things: OK — the page exists, and the anchor on it exi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/haiderstudio/broken-links-in-docs-are-silent-this-python-cli-names-the-broken-kind-16li

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-02-22-md-files-connector-stop-losing-track-of-your-markdown-docs]]
- [[2026-07-28-why-schema-drift-goes-undetected]]
- [[2026-09-26-your-link-previews-are-blank-because-ogimage-is-missing-here-is-a-stdlib-only-python-fix]]
- [[2026-10-28-check-a-shopify-product-csv-for-missing-prices-and-images-before-you-import-it]]
- [[2026-11-04-reading-medium-articles-by-tag-author-and-publication-with-rss-and-where-it-stops]]
