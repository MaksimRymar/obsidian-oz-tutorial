---
title: 'Building a SQL Lexer in Rust: Why I Replaced `Vec<char>` with `&str` and `Ident(String)`
  with Spans'
date: '2026-06-06'
source: https://dev.to/musab0986/building-a-sql-lexer-in-rust-why-i-replaced-vec-with-str-and-identstring-with-spans-5c8
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-05-31-building-a-sql-lexer-in-rust-why-i-replaced-vecchar-with-str-and-identstring-with-spans]]'
- '[[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]'
- '[[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]'
- '[[2026-05-22-building-a-sql-like-relational-database-engine-in-c-from-scratch]]'
- '[[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]'
- '[[2026-04-21-how-i-started-thinking-in-sql-not-just-writing-queries]]'
status: unread
---

> **TL;DR:** I've been building a database engine from scratch in Rust, and I recently finished the lexer. The lexer itself wasn't the most interesting part. What I found more valuable was how my design evolved as I learned more abou…

## What’s new and why it matters
I've been building a database engine from scratch in Rust, and I recently finished the lexer. The lexer itself wasn't the most interesting part. What I found more valuable was how my design evolved as I learned more about Rust and how compilers and database systems are typically implemented. My First Approach When I started, I stored the input as a Vec<char> . It felt straightforward because I could access characters directly without worrying about UTF-8 boundaries. I also represented identifiers like this: Ident ( String ) At first glance, this seems perfectly reasonable. Every identifier tok…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/musab0986/building-a-sql-lexer-in-rust-why-i-replaced-vec-with-str-and-identstring-with-spans-5c8

## Related notes
- [[2026-05-31-building-a-sql-lexer-in-rust-why-i-replaced-vecchar-with-str-and-identstring-with-spans]]
- [[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]
- [[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]
- [[2026-05-22-building-a-sql-like-relational-database-engine-in-c-from-scratch]]
- [[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]
- [[2026-04-21-how-i-started-thinking-in-sql-not-just-writing-queries]]
