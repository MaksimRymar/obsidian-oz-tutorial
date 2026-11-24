---
title: 'Ubuntu removed a root CA. Node 22.23.2 still trusts it: comparing CA lists
  by public key'
date: '2026-11-24'
source: https://dev.to/jose_pollman_fa7c6ec43cdd/ubuntu-removed-a-root-ca-node-22232-still-trusts-it-comparing-ca-lists-by-public-key-4pnh
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#feature'
- '#library'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-06-the-julius-ai-free-plan-what-the-free-credits-actually-get-you]]'
- '[[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]'
- '[[2026-10-27-find-low-stock-products-in-a-shopify-csv-with-60-lines-of-python]]'
status: unread
---

> **TL;DR:** On 30 October, apt on my Ubuntu 24.04 container installed ca-certificates 20260816ubuntu0.24.04.1 . Its changelog has one line that matters here: * Blacklist the following CA cert due to intermediate cert compromise (LP:…

## What’s new and why it matters
On 30 October, apt on my Ubuntu 24.04 container installed ca-certificates 20260816ubuntu0.24.04.1 . Its changelog has one line that matters here: * Blacklist the following CA cert due to intermediate cert compromise (LP: #2171507) + "emSign ECC Root CA - G3" That is the root above the intermediates with tiny private keys that I wrote about in October . The system store dropped it. The question I wanted answered was narrower: what on this machine still trusts it? Answering it takes two steps. Ask each runtime which list it reads, then compare the lists by public key. Step 1: ask each runtime wh…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jose_pollman_fa7c6ec43cdd/ubuntu-removed-a-root-ca-node-22232-still-trusts-it-comparing-ca-lists-by-public-key-4pnh

## Related notes
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-06-the-julius-ai-free-plan-what-the-free-credits-actually-get-you]]
- [[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]
- [[2026-10-27-find-low-stock-products-in-a-shopify-csv-with-60-lines-of-python]]
