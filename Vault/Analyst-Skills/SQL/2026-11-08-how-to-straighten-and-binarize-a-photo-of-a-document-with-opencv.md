---
title: How to straighten and binarize a photo of a document with OpenCV
date: '2026-11-08'
source: https://dev.to/bestaitool/how-to-straighten-and-binarize-a-photo-of-a-document-with-opencv-hfa
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-10-14-our-free-plan-hides-creators-with-a-window-function-and-the-locked-count-is-the-same-predicate-with-a-not-in-front]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** A document scanner app does three things to a phone photo: it finds the paper, warps its four corners into a rectangle, and turns the result into ink and paper. None of the three is exotic, but each has a place where it…

## What’s new and why it matters
A document scanner app does three things to a phone photo: it finds the paper, warps its four corners into a rectangle, and turns the result into ink and paper. None of the three is exotic, but each has a place where it quietly goes wrong. The PDF Editor in the osFoundry desktop app does this with four corner handles and a Black and white button. This post rebuilds the same pipeline in Python with OpenCV and measures it, because there is a way to score it exactly: the photo is one I generated myself, so the page that was "printed" and the corners it was placed at are both known. The test photo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/bestaitool/how-to-straighten-and-binarize-a-photo-of-a-document-with-opencv-hfa

## Related notes
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-10-14-our-free-plan-hides-creators-with-a-window-function-and-the-locked-count-is-the-same-predicate-with-a-not-in-front]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
