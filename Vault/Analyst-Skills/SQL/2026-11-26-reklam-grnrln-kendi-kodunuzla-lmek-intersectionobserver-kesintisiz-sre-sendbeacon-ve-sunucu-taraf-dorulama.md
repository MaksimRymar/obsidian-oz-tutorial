---
title: 'Reklam görünürlüğünü kendi kodunuzla ölçmek: IntersectionObserver, kesintisiz
  süre, sendBeacon ve sunucu tarafı doğrulama'
date: '2026-11-26'
source: https://dev.to/korayyalcin/reklam-gorunurlugunu-kendi-kodunuzla-olcmek-intersectionobserver-kesintisiz-sure-sendbeacon-ve-4ldd
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tableau'
- '#tool'
related:
- '[[2026-11-21-ar-sonucu-kodlamay-kodla-kurmak-iki-katmanl-model-santral-cdr-elemesi-ve-kural-tablosuyla-sonraki-deneme]]'
- '[[2026-11-24-meta-lead-adsi-crme-balamak-webhook-dorulama-graph-api-ile-lead-ekme-token-ynetimi-backfill-ve-mutabakat]]'
- '[[2026-11-15-multi-touch-attribution-sql-ile-kurmak-temas-tablosu-geriye-bak-penceresi-kredi-modelleri-ve-mutabakat]]'
- '[[2026-11-22-frequency-cappingi-reklamn-dna-tamak-crmden-giden-mesajlarda-politika-tablosu-atomik-rezervasyon-ve-bastrma-kayd]]'
- '[[2026-11-22-cac-sql-ile-hesaplamak-maliyet-defteri-dnem-eletirme-kur-dnm-ve-gecikmeli-kapan]]'
- '[[2026-11-19-9-gn-boyunca-bist-verisi-iledim-sonucu-u-oldu]]'
status: unread
---

> **TL;DR:** Programatik reklamda "gösterim" kelimesi çoğu zaman yanıltıcıdır. Ad server bir reklamı sayfaya teslim ettiğinde sayım bir artar; ama o banner sayfanın en altında duruyorsa ve kullanıcı oraya hiç kaydırmadıysa, ekranda k…

## What’s new and why it matters
Programatik reklamda "gösterim" kelimesi çoğu zaman yanıltıcıdır. Ad server bir reklamı sayfaya teslim ettiğinde sayım bir artar; ama o banner sayfanın en altında duruyorsa ve kullanıcı oraya hiç kaydırmadıysa, ekranda kimse onu görmemiştir. Viewability (gösterilebilirlik) tam olarak bu farkı ölçer: teslim edilen gösterimlerin kaçı gerçekten görülebilir alana girdi ve orada yeterince kaldı? Ben Koray Yalçın; lead yönetimi, CRM ve dijital pazarlama altyapıları kuruyorum, ağırlıklı olarak gayrimenkul projeleri ve ilan siteleri tarafında, reklamdan satış ofisine uzanan veri hattında çalışıyorum.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/korayyalcin/reklam-gorunurlugunu-kendi-kodunuzla-olcmek-intersectionobserver-kesintisiz-sure-sendbeacon-ve-4ldd

## Related notes
- [[2026-11-21-ar-sonucu-kodlamay-kodla-kurmak-iki-katmanl-model-santral-cdr-elemesi-ve-kural-tablosuyla-sonraki-deneme]]
- [[2026-11-24-meta-lead-adsi-crme-balamak-webhook-dorulama-graph-api-ile-lead-ekme-token-ynetimi-backfill-ve-mutabakat]]
- [[2026-11-15-multi-touch-attribution-sql-ile-kurmak-temas-tablosu-geriye-bak-penceresi-kredi-modelleri-ve-mutabakat]]
- [[2026-11-22-frequency-cappingi-reklamn-dna-tamak-crmden-giden-mesajlarda-politika-tablosu-atomik-rezervasyon-ve-bastrma-kayd]]
- [[2026-11-22-cac-sql-ile-hesaplamak-maliyet-defteri-dnem-eletirme-kur-dnm-ve-gecikmeli-kapan]]
- [[2026-11-19-9-gn-boyunca-bist-verisi-iledim-sonucu-u-oldu]]
