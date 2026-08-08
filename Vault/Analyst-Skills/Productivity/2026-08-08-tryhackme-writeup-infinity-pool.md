---
title: '[TryHackMe Writeup] Infinity Pool'
date: '2026-08-08'
source: https://dev.to/w1hi4/tryhackme-writeup-infinity-pool-613
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-02-9104-rows-in-5000-out-the-silent-cap-that-made-my-dashboard-lie]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-08-02-workdays-job-api-tells-you-there-are-2000-jobs-then-says-0-on-page-two]]'
- '[[2026-02-27-beginner-friendly-guide-minimum-operations-to-equalize-binary-string---problem-3666-c-python-javascript]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
status: unread
---

> **TL;DR:** Infinity Pool (Byte Lotus) — Full Room Walkthrough Target: 10.49.x.x (THM IP rotates — replace <IP> everywhere) Box: Ubuntu 24.04.4 / FreePBX + Asterisk + custom "Closed Circuit" (cc-) services Goal: User flag ( /home/we…

## What’s new and why it matters
Infinity Pool (Byte Lotus) — Full Room Walkthrough Target: 10.49.x.x (THM IP rotates — replace <IP> everywhere) Box: Ubuntu 24.04.4 / FreePBX + Asterisk + custom "Closed Circuit" (cc-) services Goal: User flag ( /home/web/user.txt ) → Root flag ( /root/root.txt ) USER FLAG: THM{n0_v1s1bl3_3dg3} ROOT FLAG: THM{tr4c3d_t0_th3_h0r1z0n} 0. Attack surface overview Port Service Purpose 22 ssh (no creds needed for the solve) 80 edge booking site (Flask/gunicorn as web ) initial foothold 127.0.0.1:8080 FreePBX admin + UCP UCP voicemail = automation key 127.0.0.1:8088/8089 Asterisk ARI — 127.0.0.1:9000…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/w1hi4/tryhackme-writeup-infinity-pool-613

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-02-9104-rows-in-5000-out-the-silent-cap-that-made-my-dashboard-lie]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-08-02-workdays-job-api-tells-you-there-are-2000-jobs-then-says-0-on-page-two]]
- [[2026-02-27-beginner-friendly-guide-minimum-operations-to-equalize-binary-string---problem-3666-c-python-javascript]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
