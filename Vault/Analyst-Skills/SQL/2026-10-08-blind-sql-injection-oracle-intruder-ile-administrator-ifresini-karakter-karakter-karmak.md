---
title: 'Blind SQL Injection (Oracle): Intruder ile Administrator Şifresini Karakter
  Karakter Çıkarmak'
date: '2026-10-08'
source: https://dev.to/yunusemredere16/blind-sql-injection-oracle-intruder-ile-administrator-sifresini-karakter-karakter-cikarmak-339
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-07-18-postgresqlde-yava-sorgular-explain-analyze-ile-zmek]]'
- '[[2026-02-25-yazlmda-yazlm-mimarisinde-veritaban-normalizasyonu-ve-den]]'
- '[[2026-02-25-claude-ile-bir-python-projesinde-veritaban-ynetimi-iin-sqla]]'
- '[[2026-04-10-tartmaoklu-entegrasyon-energytech-karbon-rapor-artk-ok-daha-hzl]]'
- '[[2026-06-14-pep-20]]'
- '[[2026-04-10-tartmajson-hazr-healthtech-tibbi-dokuman-json]]'
status: unread
---

> **TL;DR:** HTTP cevabında sorgumuz sebebiyle oluşan herhangi bir farklılık yoksa ve uygulama SQL Injection'a karşı savunmasızsa Blind SQL Injection kullanabiliriz. Bu yazı, Burp Suite ve Intruder kullanılarak Cookie tarafında Track…

## What’s new and why it matters
HTTP cevabında sorgumuz sebebiyle oluşan herhangi bir farklılık yoksa ve uygulama SQL Injection'a karşı savunmasızsa Blind SQL Injection kullanabiliriz. Bu yazı, Burp Suite ve Intruder kullanılarak Cookie tarafında TrackingId sorgulamasından faydalanarak administrator şifresini veritabanından nasıl karakter karakter tespit edip şifreyi bulabileceğimizi ve bu süreçte karşılaştığım zorlukları anlatıyor. Lab Tanıtımı Lab Adı : Blind SQL injection with conditional errors Zorluk : Practitioner Senaryo : Cookie:TrackingId içine payload enjekte ederek karakter karakter administrator hesabının şifresi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yunusemredere16/blind-sql-injection-oracle-intruder-ile-administrator-sifresini-karakter-karakter-cikarmak-339

## Related notes
- [[2026-07-18-postgresqlde-yava-sorgular-explain-analyze-ile-zmek]]
- [[2026-02-25-yazlmda-yazlm-mimarisinde-veritaban-normalizasyonu-ve-den]]
- [[2026-02-25-claude-ile-bir-python-projesinde-veritaban-ynetimi-iin-sqla]]
- [[2026-04-10-tartmaoklu-entegrasyon-energytech-karbon-rapor-artk-ok-daha-hzl]]
- [[2026-06-14-pep-20]]
- [[2026-04-10-tartmajson-hazr-healthtech-tibbi-dokuman-json]]
