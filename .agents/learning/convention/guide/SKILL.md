---
name: guide
description: Own the content rules for an incremental project learning guide. Use when writing, updating or reviewing lessons and code excerpts in a selected Learning project.
kind: convention
domain: learning
profile: core
applicability: projects explicitly selecting learning
requires: learning guide-build, selected subject contributors
provenance: house
---

# Incremental learning guides

Owns the guide's lesson content, not its build mechanics or a project's delivery
plan. Keep one guide source at `guide/`; `learning:guide-build` owns its local
rendering and excerpt validation. A guide is readable locally without a remote
publishing destination.

Each lesson starts with one real request, boundary, or small concept from the
current project. Introduce only the prerequisite terms supplied by selected
subject contributors, then show a short excerpt from code that exists. Explain
the direction of control/data, why the boundary exists, and one thing the reader
can now inspect or explain. Keep it compact enough to read alongside the code.

```markdown
## One request reaches the driver

The client creates a request because user-mode code cannot directly perform the
privileged operation. The Windows boundary forwards it to the driver, which owns
the privileged work.

<!-- excerpt: src/client/request.cpp#send_request -->
```

Do not turn the guide into a plan, a delivery checklist, a progress ledger, a
knowledge inventory, a glossary, or a complete textbook. Do not quote planned
or invented code. Update a lesson when its quoted code changes, and leave
knowledge promotion to the subject owner after learner evidence.
