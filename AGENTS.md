# AGENTS.md

Claude Code 用スキルを開発・公開するリポジトリ。プラグイン兼マーケットプレイスとして配布する。

## 構成

- `skills/<skill-name>/SKILL.md` — スキル本体(`scripts/`, `references/`, `assets/` は任意)
- `.claude-plugin/plugin.json` — プラグイン定義(`version` を管理)
- `.claude-plugin/marketplace.json` — マーケットプレイス定義
- `scripts/validate.py` — スキルと JSON の検証(標準ライブラリのみ)
- `.claude/rules/` — パス別のルール(スキル作成、依存、リリース)

## コマンド

- 検証: `python3 scripts/validate.py`
- プラグイン検証: `claude plugin validate .`
- ローカル試用: `claude --plugin-dir .`

## 基本ルール

- `name` はディレクトリ名と一致させる(kebab-case、64 文字以内)。
- `description` は「何をするか」+「いつ使うか」を書く(1024 文字以内)。
- 変更後は必ず `python3 scripts/validate.py` を実行し、通ってから完了とする。
- 詳細は `.claude/rules/` を参照。
- コミットは Conventional Commits(`feat:`, `fix:`, `docs:`, `chore:`)。
- 秘密情報(トークン、`.env`)をコミットしない。
