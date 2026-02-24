---
title: zavisoft_Inv
date: '2026-02-23'
source: https://dev.to/ruhul_aminsujon_f65b3678/zavisoftinv-4bjk
domain: Productivity
relevance: 🟡
tags:
- '#career'
- '#productivity'
related:
- '[[2026-02-23-8-sql-queries-that-catch-90-of-interview-candidates-off-guard]]'
- '[[2026-02-23-data-models-schema-defining-your-database-structure-with-sqlalchemy]]'
- '[[2026-02-21-sql-masterclass]]'
- '[[2026-02-23-flask-vs-nodejs-choosing-the-right-backend-framework-for-2026]]'
- '[[2026-02-05-tracking-activecampaign-deal-performance-using-bi-dashboard]]'
- '[[2026-02-22-what-python-caches-and-what-it-does-not]]'
status: unread
---

> **TL;DR:** 🧱 Full Database Schema Design আমি এখানে Proper Accounting Standard মেনে schema দিচ্ছি। 1️⃣ products products id (PK) name sku (unique) purchase_price (decimal 12,2) sell_price (decimal 12,2) opening_stock (integer) curre…

## What’s new and why it matters
🧱 Full Database Schema Design আমি এখানে Proper Accounting Standard মেনে schema দিচ্ছি। 1️⃣ products products id (PK) name sku (unique) purchase_price (decimal 12,2) sell_price (decimal 12,2) opening_stock (integer) current_stock (integer) created_at updated_at 🔹 current_stock আলাদা রাখছি performance এর জন্য 🔹 opening_stock future auditing এর জন্য থাকবে 2️⃣ customers customers id (PK) name phone email (nullable) address (nullable) created_at updated_at 3️⃣ sales sales id (PK) invoice_no (unique) customer_id (FK) sale_date (date) sub_total (decimal 12,2) -- before discount discount (decimal 12,2…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ruhul_aminsujon_f65b3678/zavisoftinv-4bjk

## Related notes
- [[2026-02-23-8-sql-queries-that-catch-90-of-interview-candidates-off-guard]]
- [[2026-02-23-data-models-schema-defining-your-database-structure-with-sqlalchemy]]
- [[2026-02-21-sql-masterclass]]
- [[2026-02-23-flask-vs-nodejs-choosing-the-right-backend-framework-for-2026]]
- [[2026-02-05-tracking-activecampaign-deal-performance-using-bi-dashboard]]
- [[2026-02-22-what-python-caches-and-what-it-does-not]]
