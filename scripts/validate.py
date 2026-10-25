#!/usr/bin/env python3
"""skills/*/SKILL.md と agents/*.md の frontmatter とマーケットプレイス定義を検証する(標準ライブラリのみ)。"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
errors: list[str] = []


def parse_frontmatter(text: str) -> dict[str, str] | None:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm


skills_dir = ROOT / "skills"
for d in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
    f = d / "SKILL.md"
    if not f.exists():
        errors.append(f"{d.name}: SKILL.md がありません")
        continue
    fm = parse_frontmatter(f.read_text(encoding="utf-8"))
    if fm is None:
        errors.append(f"{d.name}: frontmatter がありません")
        continue
    name, desc = fm.get("name", ""), fm.get("description", "")
    if not NAME_RE.match(name) or len(name) > 64:
        errors.append(f"{d.name}: name が不正です ({name!r})")
    if name != d.name:
        errors.append(f"{d.name}: name とディレクトリ名が一致しません ({name!r})")
    if not desc or len(desc) > 1024:
        errors.append(f"{d.name}: description が空、または 1024 文字超です")

agents_dir = ROOT / "agents"
if agents_dir.is_dir():
    for f in sorted(agents_dir.rglob("*.md")):
        rel = f.relative_to(ROOT)
        fm = parse_frontmatter(f.read_text(encoding="utf-8"))
        if fm is None:
            errors.append(f"{rel}: frontmatter がありません")
            continue
        name, desc = fm.get("name", ""), fm.get("description", "")
        if not NAME_RE.match(name) or len(name) > 64:
            errors.append(f"{rel}: name が不正です ({name!r})")
        if name != f.stem:
            errors.append(f"{rel}: name とファイル名が一致しません ({name!r})")
        if not desc:
            errors.append(f"{rel}: description が空です")

for rel in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"):
    try:
        json.loads((ROOT / rel).read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        errors.append(f"{rel}: {e}")

if errors:
    print("\n".join(f"NG {e}" for e in errors))
    sys.exit(1)
print("OK: すべての検証に成功しました")
