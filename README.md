# claude-skills

[Claude Code](https://claude.com/claude-code) 用スキルとエージェントの集。プラグイン／マーケットプレイスとして配布しています。

## インストール

```
/plugin marketplace add k1e1n04/claude-skills
/plugin install k1e1n04-skills@k1e1n04-skills
```

更新:

```
/plugin marketplace update k1e1n04-skills
```

## スキル一覧

| スキル | 内容 |
| --- | --- |
| `hello-skill` | 動作確認用のサンプル(実スキル追加後に削除予定) |
| `ux-design-for-architects` | API・設定・拡張機能の UX を 6 原則で設計・レビューする |

## エージェント一覧

| エージェント | 内容 |
| --- | --- |
| `steve-jobs-reviewer` | ジョブズの視点で成果物をレビューする(読み取り専用)。集中・体験・仕上げの 5 つのレンズで「削れ/直せ」を示す |

インストール後は `@agent-k1e1n04-skills:steve-jobs-reviewer <レビュー対象>` で呼び出せます。
「ジョブズ目線でレビューして」と頼めば Claude が自動で委譲することもあります。

## 開発

### リポジトリ構成

```
.claude-plugin/
  plugin.json          # プラグイン定義(version を管理)
  marketplace.json     # マーケットプレイス定義
agents/<agent-name>.md   # frontmatter(name, description, tools, ...) + システムプロンプト
skills/<skill-name>/
  SKILL.md             # frontmatter(name, description) + 本文
  scripts/ references/ assets/   # 任意
scripts/validate.py    # スキル・エージェントと JSON の検証
.claude/rules/         # パス別ルール
AGENTS.md              # エージェント向け指示(CLAUDE.md から import)
```

### スキルを追加する

1. `skills/<skill-name>/SKILL.md` を作成する(`name` はディレクトリ名と一致、kebab-case)。

   ```markdown
   ---
   name: my-skill
   description: 何をするか。いつ使うか(トリガー条件)。
   ---

   # my-skill

   手順...
   ```

2. 検証する。

   ```
   python3 scripts/validate.py
   claude plugin validate .
   ```

3. ローカルで試す: `claude --plugin-dir .`
4. README の一覧を更新し、`plugin.json` の `version` を上げて push する。

### エージェントを追加する

1. `agents/<agent-name>.md` を作成する(`name` はファイル名と一致、kebab-case)。
2. `description` に「何をするか」+「いつ委譲するか」を書く。レビュー系は `tools` を読み取り系に絞る。
3. 検証・ローカル試用はスキルと同じ。

### ルール

`.claude/rules/` に、スキル作成・依存関係・リリースの各ルールがあります。

## ライセンス

[MIT](LICENSE)
