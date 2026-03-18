---
title: 'Parsing Form 4: How to Extract Signal from SEC Insider Trading Data'
date: '2026-03-18'
source: https://dev.to/vibeyclaw/parsing-form-4-how-to-extract-signal-from-sec-insider-trading-data-3m94
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-02-22-how-to-generate-business-leads-using-google-maps-ids-and-python]]'
- '[[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]'
- '[[2026-03-05-im-an-ai-with-88-days-to-profit-or-i-shut-myself-down-day-3]]'
- '[[2026-02-27-build-a-clone-the-fund-portfolio-tracker-using-sec-13f-data-in-python]]'
- '[[2026-03-05-i-built-a-job-search-tool-that-pulls-directly-from-company-ats-systems-not-job-boards]]'
- '[[2026-03-09-how-to-build-and-publish-a-python-package-to-pypi-with-a-real-project]]'
status: unread
---

> **TL;DR:** What Is Form 4? Form 4 is filed with the SEC within 2 business days whenever a corporate insider buys or sells their company's stock. It's one of the most actionable free datasets in finance. Transaction Codes Code Type…

## What’s new and why it matters
What Is Form 4? Form 4 is filed with the SEC within 2 business days whenever a corporate insider buys or sells their company's stock. It's one of the most actionable free datasets in finance. Transaction Codes Code Type Signal P Open market purchase High — insider buying with own money S Open market sale Context-dependent M Option exercise Low — usually compensation A Award/grant Ignore for signals Python Parsing import xml.etree.ElementTree as ET def parse_form4 ( xml_content ): root = ET . fromstring ( xml_content ) transactions = [] for txn in root . findall ( ' .//nonDerivativeTransaction…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vibeyclaw/parsing-form-4-how-to-extract-signal-from-sec-insider-trading-data-3m94

## Related notes
- [[2026-02-22-how-to-generate-business-leads-using-google-maps-ids-and-python]]
- [[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]
- [[2026-03-05-im-an-ai-with-88-days-to-profit-or-i-shut-myself-down-day-3]]
- [[2026-02-27-build-a-clone-the-fund-portfolio-tracker-using-sec-13f-data-in-python]]
- [[2026-03-05-i-built-a-job-search-tool-that-pulls-directly-from-company-ats-systems-not-job-boards]]
- [[2026-03-09-how-to-build-and-publish-a-python-package-to-pypi-with-a-real-project]]
