---
name: guide-build
description: Scaffold, validate and render a selected Learning project's local guide from short Markdown lessons and anchored source excerpts. Use when creating a guide, building it locally, or checking its excerpts and links.
kind: utility
domain: learning
profile: core
applicability: projects explicitly selecting learning
requires: python>=3.9
provenance: house
---

# Build a local learning guide

Run the shipped script from the repository that owns the guide. It works on
Windows and Linux with the host's Python executable and needs no publishing
service.

```text
python <skill-directory>/scripts/guide_build.py scaffold --repo C:/source/project
python <skill-directory>/scripts/guide_build.py build --repo C:/source/project
python3 <skill-directory>/scripts/guide_build.py build --repo /source/project
```

`scaffold` creates only missing repository-owned files: `guide/guide.json` and
`guide/lessons/`. `build` validates every Markdown link and every
`<!-- excerpt: path#anchor -->` reference, then writes the one configured local
HTML output. The builder never publishes, changes subject knowledge, or edits a
lesson. `learning:guide` owns what lessons say.
