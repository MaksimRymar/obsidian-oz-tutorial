---
title: Create Tables
date: '2026-03-26'
source: https://dev.to/srimaha_17/create-tables-3gl
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
related:
- '[[2026-03-26-create-tables]]'
- '[[2026-03-26-design-a-reliable-wallet-transfer-system-with-acid-guarantees-pt---1-atomicity]]'
- '[[2026-03-20-postgresql-constraints]]'
- '[[2026-03-26-atomicity---design-a-reliable-wallet-transfer-system-with-acid-guarantees]]'
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-03-15-sql-for-generating-test-data-in-mysql]]'
status: unread
---

> **TL;DR:** 1. Students table with unique id CREATE TABLE students ( id SERIAL PRIMARY KEY, name TEXT,age INT); PRIMARY KEY ensures each student is uniquely identified. 2. Employees table with required fields CREATE TABLE employees…

## What’s new and why it matters
1. Students table with unique id CREATE TABLE students ( id SERIAL PRIMARY KEY, name TEXT,age INT); PRIMARY KEY ensures each student is uniquely identified. 2. Employees table with required fields CREATE TABLE employees (id SERIAL PRIMARY KEY,name TEXT NOT NULL,email TEXT NOT NULL,phone_number TEXT); NOT NULL ensures name and email cannot be empty, phone is optional. 3. Users table with unique values CREATE TABLE users (id SERIAL PRIMARY KEY,username TEXT UNIQUE,email TEXT UNIQUE); UNIQUE prevents duplicate usernames and emails. 4. Products table with constraints CREATE TABLE products (id SERI…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/srimaha_17/create-tables-3gl

## Related notes
- [[2026-03-26-create-tables]]
- [[2026-03-26-design-a-reliable-wallet-transfer-system-with-acid-guarantees-pt---1-atomicity]]
- [[2026-03-20-postgresql-constraints]]
- [[2026-03-26-atomicity---design-a-reliable-wallet-transfer-system-with-acid-guarantees]]
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-03-15-sql-for-generating-test-data-in-mysql]]
