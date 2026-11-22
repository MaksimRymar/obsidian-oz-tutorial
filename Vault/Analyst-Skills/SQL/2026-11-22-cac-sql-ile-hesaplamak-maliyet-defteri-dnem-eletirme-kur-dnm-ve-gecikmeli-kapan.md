---
title: 'CAC''ı SQL ile hesaplamak: Maliyet defteri, dönem eşleştirme, kur dönüşümü
  ve gecikmeli kapanış'
date: '2026-11-22'
source: https://dev.to/korayyalcin/caci-sql-ile-hesaplamak-maliyet-defteri-donem-eslestirme-kur-donusumu-ve-gecikmeli-kapanis-n1d
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#support-analytics'
- '#tableau'
- '#tool'
related:
- '[[2026-11-15-multi-touch-attribution-sql-ile-kurmak-temas-tablosu-geriye-bak-penceresi-kredi-modelleri-ve-mutabakat]]'
- '[[2026-11-21-ar-sonucu-kodlamay-kodla-kurmak-iki-katmanl-model-santral-cdr-elemesi-ve-kural-tablosuyla-sonraki-deneme]]'
- '[[2026-11-22-frequency-cappingi-reklamn-dna-tamak-crmden-giden-mesajlarda-politika-tablosu-atomik-rezervasyon-ve-bastrma-kayd]]'
- '[[2026-11-19-9-gn-boyunca-bist-verisi-iledim-sonucu-u-oldu]]'
- '[[2026-07-18-postgresqlde-yava-sorgular-explain-analyze-ile-zmek]]'
- '[[2026-02-25-claude-ile-bir-python-projesinde-veritaban-ynetimi-iin-sqla]]'
status: unread
---

> **TL;DR:** Bir yönetim toplantısında "müşteri edinme maliyetimiz ne?" sorusu sorulduğunda genellikle üç farklı cevap çıkar. Pazarlama ekibi reklam panelindeki harcamayı CRM'deki yeni müşteri sayısına böler. Finans ekibi ajans ücret…

## What’s new and why it matters
Bir yönetim toplantısında "müşteri edinme maliyetimiz ne?" sorusu sorulduğunda genellikle üç farklı cevap çıkar. Pazarlama ekibi reklam panelindeki harcamayı CRM'deki yeni müşteri sayısına böler. Finans ekibi ajans ücretini, yazılım lisanslarını ve satış ekibinin primlerini de ekler. Satış müdürü ise "o ay kapanan satışların çoğu üç ay önceki lansmandan geliyordu" diyerek iki rakama da itiraz eder. Üç kişi de haklıdır; sorun formülde değil, formülün altındaki verinin tanımsız olmasındadır. Ben Koray Yalçın; lead yönetimi, CRM ve pazarlama otomasyonu altyapıları kuruyorum, ağırlıklı olarak gayr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/korayyalcin/caci-sql-ile-hesaplamak-maliyet-defteri-donem-eslestirme-kur-donusumu-ve-gecikmeli-kapanis-n1d

## Related notes
- [[2026-11-15-multi-touch-attribution-sql-ile-kurmak-temas-tablosu-geriye-bak-penceresi-kredi-modelleri-ve-mutabakat]]
- [[2026-11-21-ar-sonucu-kodlamay-kodla-kurmak-iki-katmanl-model-santral-cdr-elemesi-ve-kural-tablosuyla-sonraki-deneme]]
- [[2026-11-22-frequency-cappingi-reklamn-dna-tamak-crmden-giden-mesajlarda-politika-tablosu-atomik-rezervasyon-ve-bastrma-kayd]]
- [[2026-11-19-9-gn-boyunca-bist-verisi-iledim-sonucu-u-oldu]]
- [[2026-07-18-postgresqlde-yava-sorgular-explain-analyze-ile-zmek]]
- [[2026-02-25-claude-ile-bir-python-projesinde-veritaban-ynetimi-iin-sqla]]
