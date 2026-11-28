---
title: I checked the link previews of 35 new GitHub projects' homepages. 1 in 5 had
  no image
date: '2026-11-28'
source: https://dev.to/penny24x7/i-checked-the-link-previews-of-35-new-github-projects-homepages-1-in-5-had-no-image-407k
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-10-25-a-free-python-script-to-audit-your-sites-on-page-seo-titles-meta-h1s-broken-links]]'
- '[[2026-11-27-how-to-check-every-page-on-your-site-for-duplicate-h1-tags-with-python]]'
- '[[2026-09-26-your-link-previews-are-blank-because-ogimage-is-missing-here-is-a-stdlib-only-python-fix]]'
- '[[2026-10-07-what-a-url-only-brand-audit-can-actually-see-build-a-tiny-checker-in-python]]'
- '[[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]'
- '[[2026-11-07-a-broken-link-and-seo-audit-of-your-whole-site-with-a-ranked-fix-list-for-your-developer]]'
status: unread
---

> **TL;DR:** When someone pastes your project's homepage into X, Slack or Discord, the crawler reads your raw HTML, without running JavaScript, and builds the preview from a few meta tags. If those tags are missing, you get a bare li…

## What’s new and why it matters
When someone pastes your project's homepage into X, Slack or Discord, the crawler reads your raw HTML, without running JavaScript, and builds the preview from a few meta tags. If those tags are missing, you get a bare link. I wanted a number for how often that happens on brand-new projects, so I ran a small scan. Method GitHub search API: 60 repos created after 2026-11-01 with 100–2,000 stars, plus 40 repos created after 2026-10-15 with 200+ stars (sorted by stars). 100 repos total. For each repo I read the og:image GitHub serves for the repo page (custom social preview vs. GitHub's auto-gener…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/penny24x7/i-checked-the-link-previews-of-35-new-github-projects-homepages-1-in-5-had-no-image-407k

## Related notes
- [[2026-10-25-a-free-python-script-to-audit-your-sites-on-page-seo-titles-meta-h1s-broken-links]]
- [[2026-11-27-how-to-check-every-page-on-your-site-for-duplicate-h1-tags-with-python]]
- [[2026-09-26-your-link-previews-are-blank-because-ogimage-is-missing-here-is-a-stdlib-only-python-fix]]
- [[2026-10-07-what-a-url-only-brand-audit-can-actually-see-build-a-tiny-checker-in-python]]
- [[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]
- [[2026-11-07-a-broken-link-and-seo-audit-of-your-whole-site-with-a-ranked-fix-list-for-your-developer]]
