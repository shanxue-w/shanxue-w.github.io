#!/usr/bin/env python3
"""Generate docs/publications.md from data/publications.json."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "publications.json"
OUTPUT_PATH = ROOT / "docs" / "publications.md"


def sentence(text: str) -> str:
    text = text.strip()
    if text.endswith("."):
        return text
    return f"{text}."


def bold_years(text: str) -> str:
    return re.sub(r"\b((?:19|20)\d{2})\b", r"**\1**", text.strip())


def render_entry(number: int, entry: dict[str, str]) -> str:
    authors = sentence(entry["authors"])
    details = sentence(bold_years(entry["details"]))
    if entry.get("title"):
        return f"{number}. **{entry['title']}**<br>\n   {authors} {details}"
    return f"{number}. {authors} {details}"


def render_publications(data: dict[str, object]) -> str:
    lines: list[str] = ["# Publications", ""]
    number = 1
    for section in data["sections"]:
        heading = section["heading"]
        entries = section["entries"]
        lines.extend([f"## {heading}", ""])
        for entry in entries:
            lines.append(render_entry(number, entry))
            number += 1
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if docs/publications.md is out of date")
    args = parser.parse_args()

    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    rendered = render_publications(data)

    if args.check:
        current = OUTPUT_PATH.read_text(encoding="utf-8")
        if current != rendered:
            sys.stdout.write("docs/publications.md is out of date. Run python3 scripts/generate_publications.py\n")
            return 1
        return 0

    OUTPUT_PATH.write_text(rendered, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
