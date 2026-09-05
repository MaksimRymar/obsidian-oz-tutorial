---
title: 'Cloudflare''s /security.txt 404s with Content-Type: text/plain'
date: '2026-09-05'
source: https://dev.to/devil_scrapes/cloudflares-securitytxt-404s-with-content-type-textplain-2pdb
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#career'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-26-your-site-is-bleeding-seo-over-dead-links-heres-a-10-minute-fix]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]'
- '[[2026-08-03-how-to-export-all-google-maps-reviews-to-a-spreadsheet-2026-guide]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-07-01-how-to-write-a-python-script-that-finds-cannibalized-queries-in-a-search-console-export]]'
status: unread
---

> **TL;DR:** Quick answer cloudflare.com/security.txt returns HTTP 404 with Content-Type: text/plain . So does github.com/security.txt . If your "does this file exist" check is content_type.startswith("text/plain") , both of those ar…

## What’s new and why it matters
Quick answer cloudflare.com/security.txt returns HTTP 404 with Content-Type: text/plain . So does github.com/security.txt . If your "does this file exist" check is content_type.startswith("text/plain") , both of those are a present file. If it's status == 200 , you'll miss the sites that serve a real security.txt from a soft-404 handler. You need both, plus a third check neither one gives you. Three ways to be wrong about a text file 📄 Auditing well-known files — robots.txt , security.txt , ads.txt , humans.txt — sounds like the most boring HTTP work imaginable. Fetch a path, parse some lines.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/devil_scrapes/cloudflares-securitytxt-404s-with-content-type-textplain-2pdb

## Related notes
- [[2026-08-26-your-site-is-bleeding-seo-over-dead-links-heres-a-10-minute-fix]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]
- [[2026-08-03-how-to-export-all-google-maps-reviews-to-a-spreadsheet-2026-guide]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-07-01-how-to-write-a-python-script-that-finds-cannibalized-queries-in-a-search-console-export]]
