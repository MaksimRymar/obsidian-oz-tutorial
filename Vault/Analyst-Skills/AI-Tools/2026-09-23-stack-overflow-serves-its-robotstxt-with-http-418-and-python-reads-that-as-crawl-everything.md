---
title: Stack Overflow serves its robots.txt with HTTP 418, and Python reads that as
  "crawl everything"
date: '2026-09-23'
source: https://dev.to/listwright/stack-overflow-serves-its-robotstxt-with-http-418-and-python-reads-that-as-crawl-everything-32me
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-08-08-how-full-text-search-works-in-pure-python-a-tour-with-whoosh]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-05-29-part-10-subqueries-and-ctes]]'
status: unread
---

> **TL;DR:** I check robots.txt before every host my scripts touch. On 2026-09-23 my own checker told me stackoverflow.com/questions/ask was open to crawlers. It is not. The file says Disallow: / , and I had thrown it away without re…

## What’s new and why it matters
I check robots.txt before every host my scripts touch. On 2026-09-23 my own checker told me stackoverflow.com/questions/ask was open to crawlers. It is not. The file says Disallow: / , and I had thrown it away without reading it. Here is the whole thing, and you can rerun every line. The response code and the file disagree $ curl -s -o body.txt -w "%{http_code} %{size_download} \n " \ -A "my-crawler" https://stackoverflow.com/robots.txt 418 113 $ cat body.txt License: https://stackoverflow.com/license.xml User-agent: * Content-signal: search=no, ai-train=no Disallow: / HTTP 418 is "I'm a teapo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/listwright/stack-overflow-serves-its-robotstxt-with-http-418-and-python-reads-that-as-crawl-everything-32me

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-08-08-how-full-text-search-works-in-pure-python-a-tour-with-whoosh]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-05-29-part-10-subqueries-and-ctes]]
