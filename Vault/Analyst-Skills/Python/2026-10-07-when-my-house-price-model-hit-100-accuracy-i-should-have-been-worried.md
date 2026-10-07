---
title: When My House Price Model Hit 100% Accuracy, I Should Have Been Worried
date: '2026-10-07'
source: https://dev.to/ayush_pangaonkar/when-my-house-price-model-hit-100-accuracy-i-should-have-been-worried-3ec1
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#feature'
- '#python'
- '#tool'
related:
- '[[2026-09-04-i-pulled-100-used-car-listings-from-portugals-largest-marketplace-what-prices-actually-look-like]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-10-01-how-i-close-a-monthly-dataset-and-the-month-i-found-out-mine-had-been-lying]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** My first script on the Kaggle House Prices data reported 100% training accuracy. I was pleased for about as long as it took to look at my feature list. The bug: the answer was in the inputs The script was meant to predic…

## What’s new and why it matters
My first script on the Kaggle House Prices data reported 100% training accuracy. I was pleased for about as long as it took to look at my feature list. The bug: the answer was in the inputs The script was meant to predict SalePrice , but I had included SalePrice itself as one of the input columns. The model could simply read the answer off its own inputs. Once the leaked column was gone, the same setup gave a meaningless 52% on held-out data, because I was treating a price as if it were a class label. A suspiciously perfect number is usually a sign that something is broken, not that the model…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ayush_pangaonkar/when-my-house-price-model-hit-100-accuracy-i-should-have-been-worried-3ec1

## Related notes
- [[2026-09-04-i-pulled-100-used-car-listings-from-portugals-largest-marketplace-what-prices-actually-look-like]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-10-01-how-i-close-a-monthly-dataset-and-the-month-i-found-out-mine-had-been-lying]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
