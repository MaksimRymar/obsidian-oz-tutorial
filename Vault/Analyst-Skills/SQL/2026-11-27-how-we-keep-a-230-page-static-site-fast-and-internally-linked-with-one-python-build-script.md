---
title: How we keep a 230-page static site fast and internally linked with one Python
  build script
date: '2026-11-27'
source: https://dev.to/dizigoo_digital_933f500cf/how-we-keep-a-230-page-static-site-fast-and-internally-linked-with-one-python-build-script-1a55
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]'
- '[[2026-09-04-google-crawled-230-pages-of-my-site-and-indexed-2-here-is-how-i-diagnosed-it]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-10-25-a-free-python-script-to-audit-your-sites-on-page-seo-titles-meta-h1s-broken-links]]'
- '[[2026-10-09-x-x---1-and-three-other-bit-tricks-and-the-one-that-lies-about-negative-numbers]]'
status: unread
---

> **TL;DR:** Our agency site has about 230 pages: services, software, guides and city pages. Instead of a CMS, one Python script builds every page as plain HTML. Here is what worked for speed and for search. 1. Compress images at bui…

## What’s new and why it matters
Our agency site has about 230 pages: services, software, guides and city pages. Instead of a CMS, one Python script builds every page as plain HTML. Here is what worked for speed and for search. 1. Compress images at build time The build converts every JPG and PNG to WebP (quality around 74, lower for blog photos) and rewrites the HTML to point at the WebP files. Pages stay light without any manual work. 2. Generate internal links from the page list Orphan pages are easy to create when you add pages by hand. After all pages are built, the script groups them (services, software, guides, cities)…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dizigoo_digital_933f500cf/how-we-keep-a-230-page-static-site-fast-and-internally-linked-with-one-python-build-script-1a55

## Related notes
- [[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]
- [[2026-09-04-google-crawled-230-pages-of-my-site-and-indexed-2-here-is-how-i-diagnosed-it]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-10-25-a-free-python-script-to-audit-your-sites-on-page-seo-titles-meta-h1s-broken-links]]
- [[2026-10-09-x-x---1-and-three-other-bit-tricks-and-the-one-that-lies-about-negative-numbers]]
