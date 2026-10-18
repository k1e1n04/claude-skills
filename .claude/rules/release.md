---
paths:
  - ".claude-plugin/**"
  - ".github/**"
  - "README.md"
---

# リリースルール

- スキルを追加・変更したら `.claude-plugin/plugin.json` の `version` を SemVer で上げる(追加=minor、修正=patch、互換性なし=major)。
- バージョンを上げたら `v<version>` タグを打つ。
- push 前に `python3 scripts/validate.py` と `claude plugin validate .` を実行する。
- `plugin.json` と `marketplace.json` の `name` は一致させる。
- スキルを追加したら README の「スキル一覧」を更新する。
- CI(`.github/workflows/validate.yml`)が失敗した状態でタグを打たない。
