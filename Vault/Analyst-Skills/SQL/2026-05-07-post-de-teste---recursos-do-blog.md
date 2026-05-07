---
title: Post de Teste - Recursos do Blog
date: '2026-05-07'
source: https://dev.to/ewertoncodes/post-de-teste-recursos-do-blog-4k5m
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-07-writing-sql-that-doesnt-come-back-to-haunt-you]]'
- '[[2026-04-07-postgresql-explain-analyze-reading-query-plans-like-a-pro]]'
- '[[2026-03-25-the-only-sql-cheatsheet-youll-ever-need-with-real-examples]]'
- '[[2026-03-22-format-sql-queries-in-seconds-no-extensions-no-installs]]'
- '[[2026-03-08-i-built-a-sql-query-builder-in-python---never-hand-write-sql-again]]'
- '[[2026-05-03-robinhood-data-engineering-interview-questions-prep-guide]]'
status: unread
---

> **TL;DR:** Este post serve para testar os recursos de formatação do blog. Código Ruby class Pessoa attr_accessor :nome , :idade def initialize ( nome , idade ) @nome = nome @idade = idade end def maior_de_idade? @idade >= 18 end de…

## What’s new and why it matters
Este post serve para testar os recursos de formatação do blog. Código Ruby class Pessoa attr_accessor :nome , :idade def initialize ( nome , idade ) @nome = nome @idade = idade end def maior_de_idade? @idade >= 18 end def to_s " #{ @nome } ( #{ @idade } anos)" end end pessoa = Pessoa . new ( "Ewerton" , 30 ) puts pessoa puts pessoa . maior_de_idade? # => true Código SQL SELECT u . name , COUNT ( p . id ) AS total_posts , AVG ( p . views ) AS media_views FROM users u LEFT JOIN posts p ON p . user_id = u . id WHERE u . created_at >= NOW () - INTERVAL '30 days' GROUP BY u . id , u . name HAVING C…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ewertoncodes/post-de-teste-recursos-do-blog-4k5m

## Related notes
- [[2026-04-07-writing-sql-that-doesnt-come-back-to-haunt-you]]
- [[2026-04-07-postgresql-explain-analyze-reading-query-plans-like-a-pro]]
- [[2026-03-25-the-only-sql-cheatsheet-youll-ever-need-with-real-examples]]
- [[2026-03-22-format-sql-queries-in-seconds-no-extensions-no-installs]]
- [[2026-03-08-i-built-a-sql-query-builder-in-python---never-hand-write-sql-again]]
- [[2026-05-03-robinhood-data-engineering-interview-questions-prep-guide]]
