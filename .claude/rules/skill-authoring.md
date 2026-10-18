---
paths:
  - "skills/**"
---

# スキル作成ルール

- 1 スキル = 1 ディレクトリ。`SKILL.md` が必須。
- frontmatter は `name` と `description` が必須。`name` はディレクトリ名と完全一致。
- `description` にトリガー条件(どんな依頼・ファイル・語句で使うか)を具体的に書く。曖昧だと発火しない。
- `SKILL.md` 本文は 500 行以内。長い資料は `references/` に分け、本文から参照する。
- 手順は命令形で簡潔に。要点を先に、背景説明は最小限にする。
- 決定的な処理(変換、検証など)は `scripts/` に置き、本文には実行方法だけ書く。
- スクリプトの外部依存は避ける。必要なら `.claude/rules/dependencies.md` に従う。
- 秘密情報や個人情報をスキル内に含めない。
- 追加・変更後は `python3 scripts/validate.py` を実行する。
