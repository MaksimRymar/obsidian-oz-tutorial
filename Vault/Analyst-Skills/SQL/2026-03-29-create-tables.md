---
title: Create Tables
date: '2026-03-29'
source: https://dev.to/shreya_princy_8194cc37e3f/create-tables-144m
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
related:
- '[[2026-03-26-create-tables]]'
- '[[2026-03-26-create-tables]]'
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-03-20-postgresql-constraints]]'
- '[[2026-03-28-modifying-tables-in-sql-using-alter]]'
- '[[2026-03-26-design-a-reliable-wallet-transfer-system-with-acid-guarantees-pt---1-atomicity]]'
status: unread
---

> **TL;DR:** Students Table Every student should have a unique identifier. This is achieved using a primary key. CREATE TABLE students (id SERIAL PRIMARY KEY,name TEXT,age INT); Employees Table In many real-world cases, certain field…

## What’s new and why it matters
Students Table Every student should have a unique identifier. This is achieved using a primary key. CREATE TABLE students (id SERIAL PRIMARY KEY,name TEXT,age INT); Employees Table In many real-world cases, certain fields must always have values. For employees, name and email are required, while phone number can be optional. CREATE TABLE employees (id SERIAL PRIMARY KEY,name TEXT NOT NULL,emailTEXT NOT NULL,phone_number TEXT); To prevent duplicate accounts, both username and email should be unique. CREATE TABLE users (id SERIAL PRIMARY KEY,username TEXT UNIQUE,email TEXT UNIQUE); Products Tabl…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/shreya_princy_8194cc37e3f/create-tables-144m

## Related notes
- [[2026-03-26-create-tables]]
- [[2026-03-26-create-tables]]
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-03-20-postgresql-constraints]]
- [[2026-03-28-modifying-tables-in-sql-using-alter]]
- [[2026-03-26-design-a-reliable-wallet-transfer-system-with-acid-guarantees-pt---1-atomicity]]
