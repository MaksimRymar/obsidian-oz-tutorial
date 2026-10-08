---
title: 'To Retry or Not to Retry: Exponential Backoff, Jitter and Idempotency Keys
  Done Right'
date: '2026-10-08'
source: https://dev.to/eme_gug_0821b41b948be6516/to-retry-or-not-to-retry-exponential-backoff-jitter-and-idempotency-keys-done-right-bcm
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-09-hiu-chun-acid-transaction-ng-database-ca-bn-toang-v-li-c-bn]]'
- '[[2026-07-18-docker-vs-virtualenv-setup-python-trn-laptop-ai-amd-intel]]'
- '[[2026-05-09-master-window-function-trong-sql-b-kp-ti-u-phn-tch-d-liu]]'
- '[[2026-07-31-phn-tch-python-cc-b-ch-cn-4gb-ram-vi-claude-code]]'
- '[[2026-10-05-your-database-will-leak-someday-field-level-encryption-and-blind-indexes-for-pii-with-python-and-postgresql]]'
- '[[2026-05-05-build-an-mcp-server-in-python-in-15-minutes]]'
status: unread
---

> **TL;DR:** Hầu như dev nào cũng từng viết một vòng for i in range(3) bọc quanh một HTTP call, rồi tự tin là hệ thống đã "resilient". Mình cũng vậy, cho đến một đêm payment gateway của đối tác chậm khoảng 2 giây. Service của tụi mìn…

## What’s new and why it matters
Hầu như dev nào cũng từng viết một vòng for i in range(3) bọc quanh một HTTP call, rồi tự tin là hệ thống đã "resilient". Mình cũng vậy, cho đến một đêm payment gateway của đối tác chậm khoảng 2 giây. Service của tụi mình retry ngay lập tức, 3 lần, trên 40 instance. Một sự cố nhỏ thành ra một cơn retry storm, và gateway sập hẳn. Tệ hơn nữa, vài khách hàng bị trừ tiền 2 lần vì request đầu thật ra đã thành công, chỉ có response là bị timeout. Retry không phải lúc nào cũng sai, nhưng retry ẩu thì nguy hiểm hơn là không retry. Bài này tóm lại những gì mình rút ra sau vài lần bị ăn hành: khi nào nê…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/eme_gug_0821b41b948be6516/to-retry-or-not-to-retry-exponential-backoff-jitter-and-idempotency-keys-done-right-bcm

## Related notes
- [[2026-05-09-hiu-chun-acid-transaction-ng-database-ca-bn-toang-v-li-c-bn]]
- [[2026-07-18-docker-vs-virtualenv-setup-python-trn-laptop-ai-amd-intel]]
- [[2026-05-09-master-window-function-trong-sql-b-kp-ti-u-phn-tch-d-liu]]
- [[2026-07-31-phn-tch-python-cc-b-ch-cn-4gb-ram-vi-claude-code]]
- [[2026-10-05-your-database-will-leak-someday-field-level-encryption-and-blind-indexes-for-pii-with-python-and-postgresql]]
- [[2026-05-05-build-an-mcp-server-in-python-in-15-minutes]]
