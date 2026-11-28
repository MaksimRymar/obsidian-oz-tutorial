---
title: 'Migrating WooCommerce customers and orders to Shopify: what transfers, what
  does not, and a Python CSV converter'
date: '2026-11-28'
source: https://dev.to/dzimark/migrating-woocommerce-customers-and-orders-to-shopify-what-transfers-what-does-not-and-a-python-104e
domain: Productivity
relevance: 🔴
tags:
- '#library'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-11-27-soft-delete-vs-archive-table-which-one-keeps-your-foreign-keys-working]]'
- '[[2026-09-26-26-of-45-shops-had-no-way-to-reach-them-heres-the-script-i-added]]'
status: unread
---

> **TL;DR:** Moving a store from WooCommerce to Shopify sounds like one job. In practice it's three: products, customers and orders, and each one moves differently. Products are the easy part. Customers come across with some gaps you…

## What’s new and why it matters
Moving a store from WooCommerce to Shopify sounds like one job. In practice it's three: products, customers and orders, and each one moves differently. Products are the easy part. Customers come across with some gaps you need to plan for. Orders are where most people get stuck, because the tool they used for the first two doesn't handle them. This post covers what transfers, what doesn't, and a short Python script that turns a WooCommerce customer export into a file Shopify's customer import accepts. What transfers and what doesn't? Transfers cleanly: names, email addresses, a default address,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/dzimark/migrating-woocommerce-customers-and-orders-to-shopify-what-transfers-what-does-not-and-a-python-104e

## Related notes
- [[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-11-27-soft-delete-vs-archive-table-which-one-keeps-your-foreign-keys-working]]
- [[2026-09-26-26-of-45-shops-had-no-way-to-reach-them-heres-the-script-i-added]]
