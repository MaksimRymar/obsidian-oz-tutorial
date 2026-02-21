# Obsidian Analyst Vault Agent
This repo contains an Obsidian vault (`Vault/`) plus a scheduled agent that (a) monitors a set of sources, (b) writes new notes into the vault under `Vault/Analyst-Skills/*`, (c) cleans up notes you add manually in `Vault/Inbox/`, and (d) generates a weekly digest note every Monday.

## How it works
- Every run:
  - Fetches new items from the configured sources (HN, GitHub Trending, RSS feeds, Dev.to + Medium tags, PyPI versions).
  - Filters/classifies them into a domain folder.
  - Creates a note with frontmatter + summary + "how to apply".
  - Scans `Vault/Inbox/` for notes you added manually and fills missing frontmatter, tags, and related links.
- Every Monday (UTC): generates a weekly digest note in `Vault/Weekly-Digests/`.

## Local run
```zsh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_agent.py --config config.yaml
```

## Cloud automation (GitHub Actions)
1) Push this repo to GitHub.
2) Ensure Actions are enabled.
3) The workflow commits new notes back to the repo using `GITHUB_TOKEN`.
4) Optional (recommended): add an `OPENAI_API_KEY` repository secret to get higher-quality summaries.

## Open in Obsidian
Open the `Vault/` folder as your vault.
