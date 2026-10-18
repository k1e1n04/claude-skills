---
paths:
  - "skills/**/scripts/**"
  - "scripts/**"
  - "**/package.json"
  - "**/pyproject.toml"
  - "**/go.mod"
---

# 依存関係ルール(サプライチェーン対策)

- 依存は極力追加しない。標準ライブラリを優先する。
- バージョンは完全固定する(`^` `~` や `@latest` は禁止)。
- 公開から 3 日(72 時間)未満のバージョンは使わない。追加・更新時にレジストリで公開日を確認する。
- JavaScript/TypeScript: `npm` は使わず `pnpm`。`pnpm-workspace.yaml` に `minimumReleaseAge: 4320` と `minimumReleaseAgeStrict: true`。Node.js は 24 系、TypeScript は 7 系以降で固定。
- Python: `uv` を使い、`uv.lock` をコミット。`[tool.uv] exclude-newer` は常に「実行時点の 3 日前」。`pip` 直接実行は禁止。
- Go: `go.sum` を維持し、`go install` はタグ明示。
