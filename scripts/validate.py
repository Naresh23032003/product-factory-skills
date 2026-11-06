#!/usr/bin/env python3
"""Validate skill front matter and plugin manifests. Standard library only."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
errors = []


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: cannot parse ({exc})")
        return None


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fields = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip().strip("\"'")
    return fields


def check_skill(path):
    rel = path.relative_to(ROOT)
    fm = front_matter(path)
    if fm is None:
        errors.append(f"{rel}: missing YAML front matter")
        return
    folder = path.parent.name
    name = fm.get("name", "")
    if name != folder:
        errors.append(f"{rel}: name '{name}' does not match folder '{folder}'")
    if not NAME_RE.match(name):
        errors.append(f"{rel}: name '{name}' is not kebab-case")
    desc = fm.get("description", "")
    if not desc:
        errors.append(f"{rel}: missing description")
    elif len(desc) >= 300:
        errors.append(f"{rel}: description is {len(desc)} chars (limit 299)")


def main():
    skills = sorted(ROOT.glob("plugins/*/skills/*/SKILL.md"))
    if not skills:
        errors.append("no SKILL.md files found")
    for s in skills:
        check_skill(s)

    market = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    if market is not None:
        for key in ("name", "owner", "plugins"):
            if key not in market:
                errors.append(f"marketplace.json: missing '{key}'")
        for p in market.get("plugins", []):
            src = p.get("source")
            if not p.get("name") or not src:
                errors.append("marketplace.json: plugin entry needs name and source")
                continue
            plugin_dir = (ROOT / src).resolve()
            if not plugin_dir.is_dir():
                errors.append(f"marketplace.json: source '{src}' does not exist")
            elif not (plugin_dir / ".claude-plugin" / "plugin.json").is_file():
                errors.append(f"marketplace.json: '{src}' has no .claude-plugin/plugin.json")

    for pj in sorted(ROOT.glob("plugins/*/.claude-plugin/plugin.json")):
        data = load_json(pj)
        if data is not None:
            for key in ("name", "description", "version"):
                if not data.get(key):
                    errors.append(f"{pj.relative_to(ROOT)}: missing '{key}'")

    if errors:
        print("validate: FAIL")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"validate: OK ({len(skills)} skills, manifests parse, source paths exist)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
