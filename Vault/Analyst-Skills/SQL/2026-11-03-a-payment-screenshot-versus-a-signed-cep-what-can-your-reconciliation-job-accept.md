---
title: 'A payment screenshot versus a signed CEP: what can your reconciliation job
  accept?'
date: '2026-11-03'
source: https://dev.to/ismurray/a-payment-screenshot-versus-a-signed-cep-what-can-your-reconciliation-job-accept-35c8
domain: SQL
relevance: 🔴
tags:
- '#career'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-14-test-the-next-effect-not-just-the-first-tool-call]]'
- '[[2026-09-15-4-failure-modes-of-txt-record-domain-ownership-verification-in-fastapi-onboarding]]'
- '[[2026-10-20-can-this-local-otp-branch-send-a-real-message]]'
- '[[2026-11-03-reject-a-mistyped-clabe-before-requesting-a-paid-bank-name-check]]'
- '[[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]'
- '[[2026-10-02-how-i-turn-ai-images-into-print-ready-vector-stickers-no-illustrator-no-gpu]]'
status: unread
---

> **TL;DR:** A customer sends a screenshot of a SPEI transfer and asks you to release an order. Your reconciliation job must decide whether that image is evidence or only a claim. This article proposes how a job could treat a CEP che…

## What’s new and why it matters
A customer sends a screenshot of a SPEI transfer and asks you to release an order. Your reconciliation job must decide whether that image is evidence or only a claim. This article proposes how a job could treat a CEP check result built from task status, original-evidence availability, signature status and exact transaction binding, and why pending or unavailable must stay inconclusive. The example output shown is a synthetic contract illustration, not a live check. The problem: an image is not the original record A screenshot of a banking app shows an amount, a date and perhaps a tracking key.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ismurray/a-payment-screenshot-versus-a-signed-cep-what-can-your-reconciliation-job-accept-35c8

## Related notes
- [[2026-09-14-test-the-next-effect-not-just-the-first-tool-call]]
- [[2026-09-15-4-failure-modes-of-txt-record-domain-ownership-verification-in-fastapi-onboarding]]
- [[2026-10-20-can-this-local-otp-branch-send-a-real-message]]
- [[2026-11-03-reject-a-mistyped-clabe-before-requesting-a-paid-bank-name-check]]
- [[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]
- [[2026-10-02-how-i-turn-ai-images-into-print-ready-vector-stickers-no-illustrator-no-gpu]]
