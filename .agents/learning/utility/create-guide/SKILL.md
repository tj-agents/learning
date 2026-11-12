---
name: create-guide
description: Create the small Markdown scaffold for an incremental project learning guide. Use when a selected Learning project needs its first guide or lesson.
kind: utility
domain: learning
profile: core
applicability: projects explicitly selecting learning
requires: learning guide, selected subject contributors
provenance: house
---

# Create a learning guide

Owns the initial guide structure. Create only repository-owned Markdown:

```text
guide/
  README.md
  lessons/
    01-<real-request-or-boundary>.md
```

`README.md` names the guide and links to lessons in reading order. Inspect the
current project before writing the first lesson: it follows one real request or
boundary and links only to code that exists. `learning:guide` owns the lesson
headings, prose, and decision to add a Mermaid diagram.

Do not create `guide.json`, generated HTML, a renderer, or a publishing setup.
The Markdown files are the guide; GitHub and a Markdown-aware editor can render
them where supported.

```markdown
# Project learning guide

Read the lessons in order.

1. `lessons/01-request-reaches-driver.md` — One request reaches the driver
```
