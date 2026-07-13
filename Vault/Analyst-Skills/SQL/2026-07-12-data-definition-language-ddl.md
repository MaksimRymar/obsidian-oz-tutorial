---
title: Data Definition Language (DDL)
date: '2026-07-12'
source: https://dev.to/yuripeixinho/data-definition-language-ddl-o5g
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#zendesk'
related:
- '[[2026-07-12-data-manipulation-language-dml]]'
- '[[2026-07-13-sql-data-constraints]]'
- '[[2026-07-13-sql-aggregate-queries]]'
- '[[2026-06-25-de-tabela-html-a-insert-sql-em-um-clique]]'
- '[[2026-07-13-sql-join-queries]]'
- '[[2026-07-11-how-to-criar-indices-no-sql-que-realmente-fazem-diferenca]]'
status: unread
---

> **TL;DR:** Introdução DDL é o conjunto de comandos responsável por definir e modificar a estrutura do banco de dados: criar tabelas, alterar colunas, remover objetos. Operações DDL geralmente são irreversíveis — um DROP TABLE não p…

## What’s new and why it matters
Introdução DDL é o conjunto de comandos responsável por definir e modificar a estrutura do banco de dados: criar tabelas, alterar colunas, remover objetos. Operações DDL geralmente são irreversíveis — um DROP TABLE não pede confirmação, ele simplesmente executa. CREATE TABLE Cria uma nova tabela com suas colunas, tipos de dados e restrições. CREATE TABLE clientes ( id INT PRIMARY KEY , nomeVARCHAR ( 100 ) NOT NULL , emailVARCHAR ( 150 ) UNIQUE , criado_em DATE DEFAULT CURRENT_DATE ); Neste exemplo, id é a chave primária, nome não pode ser nulo, email deve ser único em toda a tabela, e criado_e…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yuripeixinho/data-definition-language-ddl-o5g

## Related notes
- [[2026-07-12-data-manipulation-language-dml]]
- [[2026-07-13-sql-data-constraints]]
- [[2026-07-13-sql-aggregate-queries]]
- [[2026-06-25-de-tabela-html-a-insert-sql-em-um-clique]]
- [[2026-07-13-sql-join-queries]]
- [[2026-07-11-how-to-criar-indices-no-sql-que-realmente-fazem-diferenca]]
