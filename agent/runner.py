from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from .classify import classify_item
from .config import load_config
from .digest import write_weekly_digest
from .inbox import enrich_inbox
from .llm import summarize
from .models import DiscoveredItem
from .state import AgentState
from .vault import domain_folder, ensure_dirs, find_related_notes, render_note, slugify, write_note_if_missing

from .sources import devto, github_trending, hackernews, html_scrape, medium, pypi, rss


def _iso_date(dt: datetime | None) -> str:
    if not dt:
        dt = datetime.now(timezone.utc)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.strftime("%Y-%m-%d")


def _is_relevant(item: DiscoveredItem, all_keywords: list[str]) -> bool:
    """Keep broad sources from spamming the vault.

    For sources that are already tightly scoped (RSS/Medium/Dev.to/PyPI), we accept items without
    keyword hits. For broad sources (HN, GitHub Trending, generic HTML scraping), we require at
    least one keyword match.
    """

    if item.source == "PyPI":
        return True

    broad = (
        item.id.startswith("hn:")
        or item.id.startswith("ghtrending:")
        or item.id.startswith("html:")
        or item.id.startswith("devto:")
        or item.id.startswith("medium:")
    )
    if not broad:
        return True

    hay = (item.title + " " + (item.summary or "") + " " + item.url).lower()
    return any(k.lower() in hay for k in all_keywords)


def _note_body(summary_text: str, how_to_apply: str, url: str, related: list[str], relevance: str) -> str:
    lines: list[str] = []
    # Put a short 1-line summary up top for fast scanning in Obsidian.
    tldr = " ".join((summary_text or "").strip().split())
    if tldr:
        if len(tldr) > 220:
            tldr = tldr[:220].rstrip() + "…"
        lines.append(f"> **TL;DR:** {tldr}")
        lines.append("")

    lines.append("## What’s new and why it matters")
    lines.append(summary_text.strip())
    lines.append("\n## How to apply")
    lines.append(how_to_apply.strip())
    lines.append("\n## Relevance")
    lines.append(relevance)
    lines.append("\n## Source")
    lines.append(url)
    if related:
        lines.append("\n## Related notes")
        for r in related:
            lines.append(f"- [[{r}]]")
    return "\n".join(lines)


def _inject_truststore() -> None:
    """Use system trust store (macOS Keychain / corporate root CAs) if available.

    This helps in environments where TLS is intercepted by a proxy that uses a locally-trusted CA,
    which is not present in certifi.
    """

    try:
        import truststore

        truststore.inject_into_ssl()
    except Exception:
        # Best-effort only
        return


def _resolve_from(base: Path, p: Path) -> Path:
    if p.is_absolute():
        return p
    return (base / p).resolve()


def run(config_path: str | Path) -> None:
    _inject_truststore()
    cfg = load_config(config_path)

    base_dir = Path(config_path).resolve().parent

    # Resolve paths relative to the config file directory (repo root in typical usage)
    vault_dir = _resolve_from(base_dir, Path(cfg.vault_dir))
    inbox_dir = _resolve_from(base_dir, Path(cfg.inbox_dir))
    weekly_digest_dir = _resolve_from(base_dir, Path(cfg.weekly_digest_dir))
    state_path = _resolve_from(base_dir, Path(cfg.state_file))

    ensure_dirs(vault_dir)

    state = AgentState.load(state_path)

    # Build keyword list for relevance filtering
    all_keywords: list[str] = []
    for kws in cfg.classification.domain_keywords.values():
        all_keywords.extend(kws)
    all_keywords.extend(cfg.github_trending.keywords_any)
    all_keywords.extend(cfg.pypi_libraries)

    discovered: list[DiscoveredItem] = []

    # HackerNews
    try:
        discovered += hackernews.fetch_top(limit=cfg.limits.hn_top)
    except Exception:
        pass
    try:
        discovered += hackernews.fetch_new(limit=cfg.limits.hn_new)
    except Exception:
        pass

    # GitHub trending
    for lang in cfg.github_trending.languages:
        try:
            items = github_trending.fetch_trending(lang, limit=cfg.limits.github_trending)
            items = github_trending.keyword_filter(items, cfg.github_trending.keywords_any)
            discovered += items
        except Exception:
            continue

    # RSS feeds
    for f in cfg.rss_feeds:
        try:
            discovered += rss.fetch_feed(f.name, f.url, limit=cfg.limits.rss)
        except Exception:
            continue

    # HTML sources (no RSS)
    for s in cfg.html_sources:
        try:
            discovered += html_scrape.fetch_recent_links(s.name, s.url, limit=25)
        except Exception:
            continue

    # Dev.to and Medium tags
    for tag in cfg.devto_tags:
        try:
            discovered += devto.fetch_tag(tag, limit=cfg.limits.devto)
        except Exception:
            continue
    for tag in cfg.medium_tags:
        try:
            discovered += medium.fetch_tag(tag, limit=cfg.limits.medium_tag)
        except Exception:
            continue

    # PyPI
    for pkg in cfg.pypi_libraries:
        version, published_at, project_url = pypi.fetch_latest_version(pkg)
        if not version or not project_url:
            continue
        prev = state.pypi_versions.get(pkg)
        if prev == version:
            continue
        discovered.append(pypi.as_item(pkg, version, project_url, published_at))
        state.pypi_versions[pkg] = version

    # Write notes (cap total per run)
    discovered.sort(key=lambda x: (x.published_at or datetime(1970, 1, 1, tzinfo=timezone.utc)), reverse=True)

    created_count = 0
    for item in discovered:
        if created_count >= cfg.limits.max_notes_per_run:
            break
        if item.id in state.seen_ids:
            continue
        if not _is_relevant(item, all_keywords):
            continue

        classified = classify_item(item, cfg.classification.domain_keywords, cfg.classification.tag_keywords)
        domain = classified.domain

        tags = [f"#{t}" for t in classified.tags]

        llm = summarize(
            title=item.title,
            source=item.source,
            url=item.url,
            raw_text=(item.summary or "")[:8000],
            domain=domain,
        )

        related = find_related_notes(vault_dir, item.title, (item.summary or "") + "\n" + llm.summary)

        body = _note_body(
            summary_text=llm.summary,
            how_to_apply=llm.how_to_apply,
            url=item.url,
            related=related,
            relevance=llm.relevance,
        )

        fm = {
            "title": item.title,
            "date": _iso_date(item.published_at),
            "source": item.url,
            "domain": domain,
            "relevance": llm.relevance,
            "tags": tags,
            "related": [f"[[{x}]]" for x in related],
            "status": "unread",
        }

        note_txt = render_note(fm, body)

        # Path
        folder = domain_folder(vault_dir, domain)
        filename = f"{_iso_date(item.published_at)}-{slugify(item.title)}.md"
        out_path = folder / filename

        created = write_note_if_missing(out_path, note_txt)
        if created:
            created_count += 1
            state.seen_ids.add(item.id)
        else:
            # If already exists, still mark as seen to avoid reprocessing
            state.seen_ids.add(item.id)

    # Inbox enrichment (manual notes)
    enrich_inbox(
        vault_dir=vault_dir,
        inbox_dir=inbox_dir,
        domain_keywords=cfg.classification.domain_keywords,
        tag_keywords=cfg.classification.tag_keywords,
    )

    # Weekly digest on Mondays (UTC)
    now = datetime.now(timezone.utc)
    week_key = f"{now.isocalendar().year}-W{now.isocalendar().week:02d}"
    if now.weekday() == 0 and week_key not in state.weekly_digest_weeks:
        write_weekly_digest(vault_dir=vault_dir, weekly_digest_dir=weekly_digest_dir, now=now)
        state.weekly_digest_weeks.add(week_key)

    state.save(state_path)
