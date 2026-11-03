---
title: 'Node2Shell: one Brotli decoder bug, three runtimes to patch (Node.js, Bun,
  Python)'
date: '2026-11-03'
source: https://dev.to/suraj_nandan/node2shell-one-brotli-decoder-bug-three-runtimes-to-patch-nodejs-bun-python-3fi6
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-04-replacing-azure-data-studio-8-sql-clients-priced-for-a-5-dev-team]]'
- '[[2026-09-28-how-i-stream-row-changes-out-of-sqlite-without-touching-the-app-reading-the-wal]]'
- '[[2026-04-11-7-free-defi-apis-every-developer-should-know-in-2026-with-code-examples]]'
status: unread
---

> **TL;DR:** Brotli is the compression format your browser has probably used to load this page. It's fast, efficient and everywhere. It's also why one bug in one C decoder means patching Node.js, Bun, .NET, Python packages and even P…

## What’s new and why it matters
Brotli is the compression format your browser has probably used to load this page. It's fast, efficient and everywhere. It's also why one bug in one C decoder means patching Node.js, Bun, .NET, Python packages and even PHP's Windows builds this month. The bug is CVE-2026-111497 , nicknamed Node2Shell (also HTTP2Shell). Since 27 October it has been on CISA's list of vulnerabilities known to be exploited. What happened On 21 October 2026 , Node.js shipped security releases fixing ten vulnerabilities. The headline one was an out-of-bounds write in the Brotli decoder that Node.js bundles. Google,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/suraj_nandan/node2shell-one-brotli-decoder-bug-three-runtimes-to-patch-nodejs-bun-python-3fi6

## Related notes
- [[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-04-replacing-azure-data-studio-8-sql-clients-priced-for-a-5-dev-team]]
- [[2026-09-28-how-i-stream-row-changes-out-of-sqlite-without-touching-the-app-reading-the-wal]]
- [[2026-04-11-7-free-defi-apis-every-developer-should-know-in-2026-with-code-examples]]
