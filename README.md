# learning

Language-agnostic teaching and incremental Markdown guide guidance.

Published as plugin `learning` from this repository's `learning-agents` marketplace.

## Skills

- Policies: `learning:teaching`.
- Conventions: `learning:guide`.
- Utilities: `learning:create-guide`.

## Authoring and verification

```powershell
pwsh .agents/sync-generated.ps1
pwsh .agents/sync-generated.ps1 -Check
```

The layout, the vendored generator and CI come from [Template](https://github.com/tj-agents/template).
