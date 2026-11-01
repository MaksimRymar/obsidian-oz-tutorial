---
title: 'Slopsquatting: When Your AI Assistant Invents Packages and Attackers Register
  Them First'
date: '2026-11-01'
source: https://dev.to/eme_gug_0821b41b948be6516/slopsquatting-when-your-ai-assistant-invents-packages-and-attackers-register-them-first-2h48
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-10-28-your-tests-pass-but-do-they-actually-test-anything-a-practical-guide-to-mutation-testing-with-mutmut-and-strykerjs]]'
- '[[2026-10-09-cheap-models-first-building-an-llm-cascade-router-that-cuts-your-ai-bill-without-hurting-quality]]'
- '[[2026-10-08-to-retry-or-not-to-retry-exponential-backoff-jitter-and-idempotency-keys-done-right]]'
- '[[2026-09-28-before-you-build-an-ai-agent-try-an-if-statement-first]]'
- '[[2026-05-09-hiu-chun-acid-transaction-ng-database-ca-bn-toang-v-li-c-bn]]'
- '[[2026-07-31-phn-tch-python-cc-b-ch-cn-4gb-ram-vi-claude-code]]'
status: unread
---

> **TL;DR:** Tuần này trên Dev.to có một bài khá thú vị: một bạn chạy model local để sinh code, và model tự bịa ra 162 Python package không tồn tại . Điều đáng sợ là khi chạy lại từ đầu, 161 cái tên vẫn quay lại y hệt . Nghĩa là pack…

## What’s new and why it matters
Tuần này trên Dev.to có một bài khá thú vị: một bạn chạy model local để sinh code, và model tự bịa ra 162 Python package không tồn tại . Điều đáng sợ là khi chạy lại từ đầu, 161 cái tên vẫn quay lại y hệt . Nghĩa là package do AI bịa ra không hề ngẫu nhiên. Chúng lặp lại và đoán trước được. Đây chính là điều kiện để kẻ tấn công kiếm lợi: họ cho model chạy hàng nghìn prompt, gom các tên bị bịa ra lặp lại nhiều nhất, rồi đăng ký chúng lên PyPI hoặc npm kèm payload độc hại. Kiểu tấn công này có tên là slopsquatting , họ hàng của typosquatting nhưng nguy hiểm hơn, vì người gõ lệnh cài không gõ sai…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/eme_gug_0821b41b948be6516/slopsquatting-when-your-ai-assistant-invents-packages-and-attackers-register-them-first-2h48

## Related notes
- [[2026-10-28-your-tests-pass-but-do-they-actually-test-anything-a-practical-guide-to-mutation-testing-with-mutmut-and-strykerjs]]
- [[2026-10-09-cheap-models-first-building-an-llm-cascade-router-that-cuts-your-ai-bill-without-hurting-quality]]
- [[2026-10-08-to-retry-or-not-to-retry-exponential-backoff-jitter-and-idempotency-keys-done-right]]
- [[2026-09-28-before-you-build-an-ai-agent-try-an-if-statement-first]]
- [[2026-05-09-hiu-chun-acid-transaction-ng-database-ca-bn-toang-v-li-c-bn]]
- [[2026-07-31-phn-tch-python-cc-b-ch-cn-4gb-ram-vi-claude-code]]
