# learning

Language-agnostic teaching and incremental guide guidance.

Published as plugin `tj-agents/learning` from the `tj-agents` marketplace.

## Authoring this repository

This `tj-agents/learning` source repository and its worktrees are Tommy's explicitly designated
personal tooling projects, so they adopt `personal@tj-agents` for authoring. That source designation
does not change the published Learning profile or force Personal on consumers: a project can select
Learning as an optional overlay, for example while learning a new language. See
[AGENTS.md](AGENTS.md) for the canonical authoring-scope policy.

## Skills

- Policies: `learning:teaching`.
- Conventions: `learning:guide`.
- Utilities: `learning:guide-build`.

## Authoring and verification

```powershell
pwsh .agents/sync-generated.ps1
pwsh .agents/sync-generated.ps1 -Check
```

The layout, the vendored generator and CI come from [Template](https://github.com/tj-agents/template).
