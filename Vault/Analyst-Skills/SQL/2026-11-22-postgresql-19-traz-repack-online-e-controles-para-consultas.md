---
title: PostgreSQL 19 traz REPACK online e controles para consultas
date: '2026-11-22'
source: https://dev.to/guiadeti/postgresql-19-traz-repack-online-e-controles-para-consultas-3pd2
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#sql'
related:
- '[[2026-11-20-postgresql-19-chega-com-recursos-de-administrao-e-desenvolvimento]]'
- '[[2026-07-12-data-manipulation-language-dml]]'
- '[[2026-11-21-wordpress-715-corrige-19-avisos-de-segurana-cinco-de-alta-gravidade]]'
- '[[2026-11-17-curso-gratuito-de-python-bsico-aulas-prticas-e-certificado]]'
- '[[2026-04-13-reduzindo-o-ttft-em-streaming-de-ia-padres-de-arquitetura-para-flush-por-yield-no-django]]'
- '[[2026-03-06-artigo-sobre-a-evoluo-do-modelo-relacional-para-objeto-relacional]]'
status: unread
---

> **TL;DR:** O PostgreSQL Global Development Group lançou o PostgreSQL 19 com mudanças na manutenção de bancos de dados, no planejamento de consultas, na replicação e no desenvolvimento de aplicações. Entre os destaques estão a reorg…

## What’s new and why it matters
O PostgreSQL Global Development Group lançou o PostgreSQL 19 com mudanças na manutenção de bancos de dados, no planejamento de consultas, na replicação e no desenvolvimento de aplicações. Entre os destaques estão a reorganização de tabelas sem interromper leituras ou gravações e novos recursos para orientar a escolha de planos de consulta. Reorganização de tabelas e manutenção O REPACK recupera espaço não utilizado nas tabelas e pode reorganizar os dados para acompanhar um índice. Sua opção CONCURRENTLY permite executar a operação sem bloquear leituras ou gravações, o que pode substituir usos…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/guiadeti/postgresql-19-traz-repack-online-e-controles-para-consultas-3pd2

## Related notes
- [[2026-11-20-postgresql-19-chega-com-recursos-de-administrao-e-desenvolvimento]]
- [[2026-07-12-data-manipulation-language-dml]]
- [[2026-11-21-wordpress-715-corrige-19-avisos-de-segurana-cinco-de-alta-gravidade]]
- [[2026-11-17-curso-gratuito-de-python-bsico-aulas-prticas-e-certificado]]
- [[2026-04-13-reduzindo-o-ttft-em-streaming-de-ia-padres-de-arquitetura-para-flush-por-yield-no-django]]
- [[2026-03-06-artigo-sobre-a-evoluo-do-modelo-relacional-para-objeto-relacional]]
