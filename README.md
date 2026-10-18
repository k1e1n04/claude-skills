# claude-skills

Claude Code 用スキルの開発・公開リポジトリ。

## インストール

```
/plugin marketplace add k1e1n04/claude-skills
/plugin install k1e1n04-skills@k1e1n04-skills
```

## 構成

```
.claude-plugin/
  plugin.json        # プラグイン定義
  marketplace.json   # マーケットプレイス定義
skills/<skill-name>/
  SKILL.md           # frontmatter(name, description) + 本文
  (scripts/, references/ など任意)
scripts/validate.py  # スキルと JSON の検証
```

## スキルの追加

1. `skills/<skill-name>/SKILL.md` を作成(`name` はディレクトリ名と一致、kebab-case)
2. `python3 scripts/validate.py` で検証
3. `plugin.json` の `version` を上げて push

作成には `skill-creator` スキルが使える。ローカル試用は `claude --plugin-dir .`。
