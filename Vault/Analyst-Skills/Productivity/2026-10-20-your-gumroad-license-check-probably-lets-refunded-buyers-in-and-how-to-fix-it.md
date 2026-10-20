---
title: Your Gumroad license check probably lets refunded buyers in (and how to fix
  it)
date: '2026-10-20'
source: https://dev.to/pau_drudis_6182de07fdc9f0/your-gumroad-license-check-probably-lets-refunded-buyers-in-and-how-to-fix-it-368g
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-05-a-domain-that-doesnt-exist-returns-http-200-ok]]'
- '[[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]'
- '[[2026-05-19-asyncawait-in-python-explained-using-a-food-delivery-app]]'
- '[[2026-08-27-design-functions-that-compound]]'
- '[[2026-06-22-how-i-cut-my-llm-api-bill-by-80-with-a-simple-router]]'
- '[[2026-04-06-want-to-learn-python-for-free-but-dont-know-where-to-start]]'
status: unread
---

> **TL;DR:** If you sell software on Gumroad and gate it with license keys, there's a good chance your check looks like this: const res = await fetch ( " https://api.gumroad.com/v2/licenses/verify " , { method : " POST " , body : new…

## What’s new and why it matters
If you sell software on Gumroad and gate it with license keys, there's a good chance your check looks like this: const res = await fetch ( " https://api.gumroad.com/v2/licenses/verify " , { method : " POST " , body : new URLSearchParams ({ product_id , license_key }), }). then (( r ) => r . json ()); if ( res . success ) unlock (); // looks fine... The problem: success only tells you the key exists. After a buyer is refunded, files a chargeback, or cancels a subscription, /v2/licenses/verify still returns success: true . The status lives in the purchase object, so a check on success alone lets…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/pau_drudis_6182de07fdc9f0/your-gumroad-license-check-probably-lets-refunded-buyers-in-and-how-to-fix-it-368g

## Related notes
- [[2026-09-05-a-domain-that-doesnt-exist-returns-http-200-ok]]
- [[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]
- [[2026-05-19-asyncawait-in-python-explained-using-a-food-delivery-app]]
- [[2026-08-27-design-functions-that-compound]]
- [[2026-06-22-how-i-cut-my-llm-api-bill-by-80-with-a-simple-router]]
- [[2026-04-06-want-to-learn-python-for-free-but-dont-know-where-to-start]]
