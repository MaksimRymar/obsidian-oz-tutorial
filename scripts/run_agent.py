#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

# Ensure the repo root is on sys.path so `import agent` works when this is executed as a file.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agent.runner import run  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.yaml")
    args = ap.parse_args()
    run(args.config)


if __name__ == "__main__":
    main()
