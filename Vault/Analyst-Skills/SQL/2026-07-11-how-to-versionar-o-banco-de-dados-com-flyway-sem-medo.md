---
title: How to versionar o banco de dados com Flyway sem medo
date: '2026-07-11'
source: https://dev.to/isaias_velasquez_d2261770/how-to-versionar-o-banco-de-dados-com-flyway-sem-medo-29io
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-06-25-de-tabela-html-a-insert-sql-em-um-clique]]'
- '[[2026-03-05-a-pegadinha-do-auto-incremento-como-o-serial-do-postgresql-se-compara-a-outros-sgbds]]'
- '[[2026-02-20-python-opensearch-e-bi-construindo-dashboards-em-tempo-real]]'
- '[[2026-05-18-como-no-ter-o-nmero-do-whatsapp-bloqueado-usando-automao-com-ia]]'
- '[[2026-04-15-example-of-e-commice-sql-in-that-specilises-in-the-food-industry]]'
- '[[2026-03-04-a-evoluo-do-modelo-relacional-para-objeto-relacional]]'
status: unread
---

> **TL;DR:** Flyway versiona o schema do banco de dados da mesma forma que o Git versiona o codigo fonte. Cada migracao e um arquivo SQL que o Flyway executa na ordem certa. Adicione a dependencia no build.gradle.kts : implementation…

## What’s new and why it matters
Flyway versiona o schema do banco de dados da mesma forma que o Git versiona o codigo fonte. Cada migracao e um arquivo SQL que o Flyway executa na ordem certa. Adicione a dependencia no build.gradle.kts : implementation("org.flywaydb:flyway-core") runtimeOnly("org.flywaydb:flyway-database-postgresql") Com Spring Boot, a configuracao e simples: # application.properties spring.flyway.enabled=true spring.flyway.locations=classpath:db/migration Crie o primeiro arquivo de migracao em src/main/resources/db/migration/V1__criar_tabela_usuarios.sql : CREATE TABLE usuarios ( id BIGSERIAL PRIMARY KEY, n…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/isaias_velasquez_d2261770/how-to-versionar-o-banco-de-dados-com-flyway-sem-medo-29io

## Related notes
- [[2026-06-25-de-tabela-html-a-insert-sql-em-um-clique]]
- [[2026-03-05-a-pegadinha-do-auto-incremento-como-o-serial-do-postgresql-se-compara-a-outros-sgbds]]
- [[2026-02-20-python-opensearch-e-bi-construindo-dashboards-em-tempo-real]]
- [[2026-05-18-como-no-ter-o-nmero-do-whatsapp-bloqueado-usando-automao-com-ia]]
- [[2026-04-15-example-of-e-commice-sql-in-that-specilises-in-the-food-industry]]
- [[2026-03-04-a-evoluo-do-modelo-relacional-para-objeto-relacional]]
