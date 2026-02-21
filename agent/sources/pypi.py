from __future__ import annotations

from datetime import datetime

import requests

from ..models import DiscoveredItem


def fetch_latest_version(pkg: str) -> tuple[str | None, datetime | None, str | None]:
    url = f"https://pypi.org/pypi/{pkg}/json"
    r = requests.get(url, timeout=30)
    if r.status_code != 200:
        return None, None, None
    data = r.json()
    info = data.get("info") or {}
    version = info.get("version")

    releases = data.get("releases") or {}
    files = releases.get(version) or []
    upload_time = None
    if files:
        t = files[0].get("upload_time_iso_8601") or files[0].get("upload_time")
        if t:
            try:
                upload_time = datetime.fromisoformat(t.replace("Z", "+00:00"))
            except Exception:
                upload_time = None

    project_url = info.get("project_url") or info.get("package_url") or f"https://pypi.org/project/{pkg}/"
    return version, upload_time, project_url


def as_item(pkg: str, version: str, project_url: str, published_at: datetime | None) -> DiscoveredItem:
    return DiscoveredItem(
        id=f"pypi:{pkg}:{version}",
        title=f"{pkg} {version} released",
        url=project_url,
        source="PyPI",
        published_at=published_at,
        summary=None,
        extra={"package": pkg, "version": version},
    )
