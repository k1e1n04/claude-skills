---
paths:
  - "agents/**"
---

# エージェント作成ルール

- 1 エージェント = 1 ファイル `agents/<name>.md`。`name` はファイル名(拡張子なし)と一致、kebab-case。
- `description` に「何をするか」+「いつ委譲するか」を具体的に書く。
- プラグイン同梱のエージェントで有効な frontmatter: `name` `description` `model` `effort` `maxTurns` `tools` `disallowedTools` `skills` `memory` `background` `isolation` `color`。`hooks` `mcpServers` `permissionMode` は無視される。
- レビュー系は `tools` を読み取り系(Read, Grep, Glob, Bash)に絞り、書き込みさせない。
- 実在人物の口調を再現する場合、実在の発言を捏造しない。引用は一次資料で確認できるものに限る。
- 追加・変更後は `python3 scripts/validate.py` と `claude plugin validate .` を実行し、`plugin.json` の `version` を上げる。
