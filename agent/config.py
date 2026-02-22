from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class FeedCfg:
    name: str
    url: str
    default_domain: str


@dataclass(frozen=True)
class HtmlSourceCfg:
    name: str
    url: str
    default_domain: str


@dataclass(frozen=True)
class LimitsCfg:
    hn_top: int = 40
    hn_new: int = 40
    github_trending: int = 30
    devto: int = 30
    medium_tag: int = 30
    rss: int = 50
    max_notes_per_run: int = 80


@dataclass(frozen=True)
class GitHubTrendingCfg:
    languages: list[str]
    keywords_any: list[str]


@dataclass(frozen=True)
class ClassificationCfg:
    domain_keywords: dict[str, list[str]]
    tag_keywords: dict[str, list[str]]


@dataclass(frozen=True)
class AgentConfig:
    vault_dir: Path
    inbox_dir: Path
    weekly_digest_dir: Path
    state_file: Path
    limits: LimitsCfg

    pypi_libraries: list[str]
    rss_feeds: list[FeedCfg]
    html_sources: list[HtmlSourceCfg]
    devto_tags: list[str]
    medium_tags: list[str]
    github_trending: GitHubTrendingCfg
    classification: ClassificationCfg


def _req(d: dict[str, Any], key: str) -> Any:
    if key not in d:
        raise KeyError(f"Missing required config key: {key}")
    return d[key]


def load_config(config_path: str | Path) -> AgentConfig:
    p = Path(config_path)
    raw = yaml.safe_load(p.read_text(encoding="utf-8"))

    vault_dir = Path(_req(raw, "vault_dir"))
    inbox_dir = Path(_req(raw, "inbox_dir"))
    weekly_digest_dir = Path(_req(raw, "weekly_digest_dir"))
    state_file = Path(_req(raw, "state_file"))

    limits_raw = raw.get("limits", {})
    limits = LimitsCfg(**limits_raw)

    rss = [FeedCfg(**x) for x in raw.get("rss_feeds", [])]
    html_sources = [HtmlSourceCfg(**x) for x in raw.get("html_sources", [])]

    gh = raw.get("github_trending", {})
    gh_cfg = GitHubTrendingCfg(
        languages=list(gh.get("languages", [])),
        keywords_any=list(gh.get("keywords_any", [])),
    )

    cls = raw.get("classification", {})
    cls_cfg = ClassificationCfg(
        domain_keywords=dict(cls.get("domain_keywords", {})),
        tag_keywords=dict(cls.get("tag_keywords", {})),
    )

    return AgentConfig(
        vault_dir=vault_dir,
        inbox_dir=inbox_dir,
        weekly_digest_dir=weekly_digest_dir,
        state_file=state_file,
        limits=limits,
        pypi_libraries=list(raw.get("pypi_libraries", [])),
        rss_feeds=rss,
        html_sources=html_sources,
        devto_tags=list(raw.get("devto_tags", [])),
        medium_tags=list(raw.get("medium_tags", [])),
        github_trending=gh_cfg,
        classification=cls_cfg,
    )
