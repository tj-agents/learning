# learning

This repository uses the plugin layout `template:check` documents and enforces
(https://github.com/tj-agents/template). Authored skills live once under `.agents/<namespace>/skills/<subject>/SKILL.md`,
with each skill's scripts and templates beside it; related skills share a family folder, family first
(`state/client/` publishes `state-client`). `.agents/sync_generated.py`, `.agents/sync-generated.ps1`,
`.gitattributes`, `.gitignore`, `CLAUDE.md` and `.github/workflows/ci.yml` are vendored from Template's main branch.
Change them in Template, then run `template:update` to refresh the exact vendored content.

`.codex/skills/`, `.claude/skills/`, `.agents/INDEX.md`, both marketplace files and `plugins/*` are generated. Run
`pwsh .agents/sync-generated.ps1` after authored changes and require `pwsh .agents/sync-generated.ps1 -Check`
before delivery.

```powershell
pwsh .agents/sync-generated.ps1
pwsh .agents/sync-generated.ps1 -Check
```

Follow `engineering:docs` when adding or changing a skill or standard. Keep a standard's required `Owns …`
opening, then use a concrete fenced example before additional explanatory prose to settle ambiguous terminology. A
starter's explicit unfinished placeholder is not an example, so replace it with real behaviour before committing
because the guidance-example check rejects it.

The Learning plugin separates teaching guidance (`learning`), guide construction rules (`standard`) and the guide build command (`operation`). Kind describes behavior; every skill uses the same subject folder layout. Declare mandatory host hooks in the shipped harness manifest and verify their delivery on each supported host.
