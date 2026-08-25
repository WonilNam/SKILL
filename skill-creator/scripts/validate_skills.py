#!/usr/bin/env python3
"""Validate one Agent Skill directory or every skill below a repository root."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PLACEHOLDER_RE = re.compile(r"\b(TODO|TBD|YOUR[_ -]|REPLACE[_ -]ME)\b", re.IGNORECASE)


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return {}, [f"cannot read UTF-8 file: {exc}"]
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, ["missing opening YAML frontmatter delimiter"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, ["missing closing YAML frontmatter delimiter"]

    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")):
            # Nested values of supported optional fields are intentionally ignored.
            continue
        if ":" not in line:
            errors.append(f"invalid top-level frontmatter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key in metadata:
            errors.append(f"duplicate top-level frontmatter field: {key}")
            continue
        raw_value = value.strip()
        if raw_value.startswith(("'", '"')) and not raw_value.endswith(raw_value[0]):
            errors.append(f"unterminated quoted value for frontmatter field: {key}")
        metadata[key] = raw_value.strip("'\"")
    if PLACEHOLDER_RE.search(text):
        errors.append("contains an unfinished scaffold placeholder")
    return metadata, errors


def validate(skill_file: Path) -> list[str]:
    metadata, errors = parse_frontmatter(skill_file)
    name = metadata.get("name", "")
    description = metadata.get("description", "")
    if not name:
        errors.append("missing required frontmatter field: name")
    elif not NAME_RE.fullmatch(name):
        errors.append("name must use lowercase letters, digits, and single hyphens")
    elif skill_file.parent.name != name:
        errors.append(f"name {name!r} does not match directory {skill_file.parent.name!r}")
    if not description:
        errors.append("missing required frontmatter field: description")
    elif len(description) > 1024:
        errors.append("description exceeds 1024 characters")
    return errors


def discover(target: Path) -> list[Path]:
    if target.is_file():
        return [target] if target.name == "SKILL.md" else []
    direct = target / "SKILL.md"
    if direct.is_file():
        return [direct]
    return sorted(target.rglob("SKILL.md"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=Path, help="Skill directory, SKILL.md, or repository root")
    args = parser.parse_args()
    files = discover(args.target.resolve())
    if not files:
        print("No SKILL.md files found", file=sys.stderr)
        return 2

    failed = False
    for skill_file in files:
        errors = validate(skill_file)
        status = "FAIL" if errors else "OK"
        print(f"{status} {skill_file}")
        for error in errors:
            print(f"  - {error}")
        failed = failed or bool(errors)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
