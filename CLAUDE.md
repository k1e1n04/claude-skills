# claude-skills

- スキルは `skills/<name>/SKILL.md`。`name` はディレクトリ名と一致させる(kebab-case)。
- `description` は「何をするか」+「いつ使うか(トリガー)」を書く。1024 文字以内。
- 変更後は `python3 scripts/validate.py` を実行する。
- 公開時は `.claude-plugin/plugin.json` の `version` を更新する。
- 外部依存を追加する場合はバージョン固定・公開3日以上のものだけを使う(グローバル規約に従う)。
