---
title: 'When web scraping breaks: using AI to extract messy data'
date: '2026-05-29'
source: https://dev.to/__c1b9e06dc90a7e0a676b/when-web-scraping-breaks-using-ai-to-extract-messy-data-19il
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-02-24-stop-writing-css-selectors-that-break---extract-web-data-with-plain-english-using-ai]]'
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
- '[[2026-05-04-day-3-prompting-techniques-in-ai-part-1]]'
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
- '[[2026-04-25-build-your-first-ai-agent-in-60-lines-of-python-no-framework-needed]]'
- '[[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]'
status: unread
---

> **TL;DR:** I spent three days building a web scraper for a client. Three days of carefully crafting CSS selectors, testing edge cases, and patching broken parsers. On day four, the target website redesigned their product pages. Eve…

## What’s new and why it matters
I spent three days building a web scraper for a client. Three days of carefully crafting CSS selectors, testing edge cases, and patching broken parsers. On day four, the target website redesigned their product pages. Everything broke. I sat there staring at a wall of None values and AttributeError messages. The old selectors were useless. The new HTML structure was inconsistent across different product categories. Some pages used <div class="price"> , others used <span class="cost"> , and a few had the price embedded in a JSON-LD script tag. My beautiful, fragile parser was dead. This is the s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/__c1b9e06dc90a7e0a676b/when-web-scraping-breaks-using-ai-to-extract-messy-data-19il

## Related notes
- [[2026-02-24-stop-writing-css-selectors-that-break---extract-web-data-with-plain-english-using-ai]]
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
- [[2026-05-04-day-3-prompting-techniques-in-ai-part-1]]
- [[2026-05-18-top-orm-tools-practical-comparison]]
- [[2026-04-25-build-your-first-ai-agent-in-60-lines-of-python-no-framework-needed]]
- [[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]
