---
title: 'Moving face search off AWS Rekognition in two days: a photo marketplace''s
  playbook'
date: '2026-11-06'
source: https://dev.to/ashish_sikka/moving-face-search-off-aws-rekognition-in-two-days-a-photo-marketplaces-playbook-5ele
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-10-06-a-new-campaigns-first-results-cost-zero-api-quota-because-postgres-already-has-the-titles]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-10-17-batch-converting-500-pngs-to-jpg-i-timed-my-pillow-script-against-the-alternatives]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
status: unread
---

> **TL;DR:** This article was written with AI. Disclosure: I work on SightRadar, the API this team moved to. The figures below are the ones sellphotos.online reported. The full case study is at sightradar.com/customers/sellphotos . s…

## What’s new and why it matters
This article was written with AI. Disclosure: I work on SightRadar, the API this team moved to. The figures below are the ones sellphotos.online reported. The full case study is at sightradar.com/customers/sellphotos . sellphotos.online is a marketplace where event and sports photographers upload their shots and guests buy the ones they appear in. A guest uploads a selfie and the platform finds every photo that person is in. They process hundreds of thousands of photos a month across weddings, marathons and corporate events. They ran this on AWS Rekognition and had two problems with it. The bi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashish_sikka/moving-face-search-off-aws-rekognition-in-two-days-a-photo-marketplaces-playbook-5ele

## Related notes
- [[2026-10-06-a-new-campaigns-first-results-cost-zero-api-quota-because-postgres-already-has-the-titles]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-10-17-batch-converting-500-pngs-to-jpg-i-timed-my-pillow-script-against-the-alternatives]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
