---
title: I Ran My ML Secrets Detector Against My Own Repositories — Here's What It Found
date: '2026-05-16'
source: https://dev.to/pgmpofu/i-ran-my-ml-secrets-detector-against-my-own-repositories-heres-what-it-found-281p
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-26-i-got-tired-of-setting-up-fastapi-projects-manually-so-i-built-a-cli-to-do-it-for-me]]'
- '[[2026-04-12-i-built-a-tcp-networking-library-in-python-at-14-and-v162-just-hit-110k-msgs-with-zero-dependencies]]'
- '[[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]'
status: unread
---

> **TL;DR:** here's a moment every security tool builder eventually faces. You've built the scanner. You've written the rules. You've validated it against synthetic test cases and contrived examples. And then you point it at your own…

## What’s new and why it matters
here's a moment every security tool builder eventually faces. You've built the scanner. You've written the rules. You've validated it against synthetic test cases and contrived examples. And then you point it at your own code — the repositories you've actually written, committed, and pushed over years of real development work. That moment is humbling. I ran my ML secrets detector against every personal repository I own — 11 repositories across Python, Java, Node.js, and Kotlin projects accumulated over several years of portfolio building and side projects. I'm documenting the results honestly:…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/pgmpofu/i-ran-my-ml-secrets-detector-against-my-own-repositories-heres-what-it-found-281p

## Related notes
- [[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-26-i-got-tired-of-setting-up-fastapi-projects-manually-so-i-built-a-cli-to-do-it-for-me]]
- [[2026-04-12-i-built-a-tcp-networking-library-in-python-at-14-and-v162-just-hit-110k-msgs-with-zero-dependencies]]
- [[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]
