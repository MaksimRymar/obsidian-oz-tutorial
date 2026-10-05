---
title: Parsing and Formatting SQL in JavaScript — Without a Grammar File
date: '2026-10-05'
source: https://dev.to/toolzip/parsing-and-formatting-sql-in-javascript-without-a-grammar-file-18hk
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-04-25-6-essential-sql-concepts-every-beginner-should-master]]'
- '[[2026-04-15-writing-a-sql-formatter-with-a-handwritten-tokenizer]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-05-11-inner-vs-outer-joins-the-two-fundamental-join-types-in-sql]]'
- '[[2026-06-16-dont-parse-sql-to-make-a-query-runner-read-only]]'
- '[[2026-05-13-understanding-sql-query-structure]]'
status: unread
---

> **TL;DR:** Parsing and Formatting SQL in JavaScript — Without a Grammar File Building a SQL formatter sounds like it requires a full parser. For most practical cases, it doesn't. Here's a keyword-based approach that handles 90% of…

## What’s new and why it matters
Parsing and Formatting SQL in JavaScript — Without a Grammar File Building a SQL formatter sounds like it requires a full parser. For most practical cases, it doesn't. Here's a keyword-based approach that handles 90% of real-world SQL. The Core Idea SQL formatting is mostly about: Uppercasing reserved words Adding newlines before clauses Indenting sub-clauses A full AST parser is overkill for formatting. Instead, tokenize by keywords and apply rules. Tokenization const KEYWORDS = [ ' SELECT ' , ' FROM ' , ' WHERE ' , ' JOIN ' , ' LEFT JOIN ' , ' RIGHT JOIN ' , ' INNER JOIN ' , ' ON ' , ' GROUP…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/toolzip/parsing-and-formatting-sql-in-javascript-without-a-grammar-file-18hk

## Related notes
- [[2026-04-25-6-essential-sql-concepts-every-beginner-should-master]]
- [[2026-04-15-writing-a-sql-formatter-with-a-handwritten-tokenizer]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-05-11-inner-vs-outer-joins-the-two-fundamental-join-types-in-sql]]
- [[2026-06-16-dont-parse-sql-to-make-a-query-runner-read-only]]
- [[2026-05-13-understanding-sql-query-structure]]
