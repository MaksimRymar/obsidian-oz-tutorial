---
title: Shipping a vision-model verdict on Bedrock and Lightsail
date: '2026-08-16'
source: https://dev.to/aws-builders/shipping-a-vision-model-verdict-on-bedrock-and-lightsail-411
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]'
- '[[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
- '[[2026-08-10-you-cannot-predict-what-an-llm-call-will-cost-before-you-make-it]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
status: unread
---

> **TL;DR:** Built 2026-08-15 against us.amazon.nova-lite-v1:0 via the Bedrock Converse API. FastAPI on Python 3.13, deployed to an Amazon Lightsail container service ( nano , scale 1) in us-east-1 . Scored against the live deploymen…

## What’s new and why it matters
Built 2026-08-15 against us.amazon.nova-lite-v1:0 via the Bedrock Converse API. FastAPI on Python 3.13, deployed to an Amazon Lightsail container service ( nano , scale 1) in us-east-1 . Scored against the live deployment, not localhost: 20/20 on the fixture set, median 880 ms per scan. Live: Dog or Not: Lite · Source: github.com/xbill9/dog-or-not-lite · Built for the AWS Weekend Challenge: Build a Creative App . TL;DR Make the model fill in a schema instead of writing a sentence. The Converse API's toolConfig plus toolChoice forces a named function call, so is_dog arrives as a boolean because…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aws-builders/shipping-a-vision-model-verdict-on-bedrock-and-lightsail-411

## Related notes
- [[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]
- [[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
- [[2026-08-10-you-cannot-predict-what-an-llm-call-will-cost-before-you-make-it]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
