---
title: 96.5% Accurate Spam Filter, and the 58 Spam Messages It Let Through
date: '2026-10-09'
source: https://dev.to/ayush_pangaonkar/965-accurate-spam-filter-and-the-58-spam-messages-it-let-through-akm
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-07-when-my-house-price-model-hit-100-accuracy-i-should-have-been-worried]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-02-22-what-mongodb-taught-me-about-postgres]]'
- '[[2026-07-06-i-got-tired-of-my-portfolio-looking-like-a-list-of-links-so-i-built-an-mcp-server-for-it]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** My spam classifier scores 96.5% accuracy on the test set. That sounds great. The confusion matrix tells a more useful story. The setup The dataset is mail_data.csv , with 5,572 messages: 4,825 ham (86.6%) and 747 spam (1…

## What’s new and why it matters
My spam classifier scores 96.5% accuracy on the test set. That sounds great. The confusion matrix tells a more useful story. The setup The dataset is mail_data.csv , with 5,572 messages: 4,825 ham (86.6%) and 747 spam (13.4%), no missing values. I mapped labels to 0 (spam) and 1 (ham), split 70/30 with random_state=3 , fit a TfidfVectorizer (English stopwords removed, vocabulary of 6,896 terms) on the training messages, and trained a LogisticRegression model. Metric Value Train accuracy 96.6% Test accuracy 96.5% Always predict ham 86.6% Test accuracy beats the always-ham baseline by about ten…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ayush_pangaonkar/965-accurate-spam-filter-and-the-58-spam-messages-it-let-through-akm

## Related notes
- [[2026-10-07-when-my-house-price-model-hit-100-accuracy-i-should-have-been-worried]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-02-22-what-mongodb-taught-me-about-postgres]]
- [[2026-07-06-i-got-tired-of-my-portfolio-looking-like-a-list-of-links-so-i-built-an-mcp-server-for-it]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
