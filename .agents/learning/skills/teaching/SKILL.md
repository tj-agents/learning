---
name: teaching
description: Own the teaching method, learner checkpoints and delivery-mode boundary for projects that explicitly select Learning. Use when teaching an unfamiliar concept, choosing between guided delivery and study, or recording learner evidence without changing subject knowledge.
kind: learning
domain: learning
profile: core
applicability: projects explicitly selecting learning
requires: selected language or platform contributors
provenance: house
---

# Teaching while delivering

Learning owns how a project teaches. Selected language and platform plugins own
their terminology, prerequisites, examples, direction and knowledge inventory;
Engineering owns the code change, validation and delivery lifecycle. Never
replace those owners or infer a learner's knowledge from working code, a guide,
an explanation, or a completed delivery.

## Start from the selected contributors

Before a lesson or a learner-facing implementation task, read the relevant
qualified contributor skills from the project's selected plugins. Use their
knowledge inventory to find prerequisites and their direction/explanation skills
to choose vocabulary and a real example. A contributor can be absent or uneven:
use only what the selected project supplies. Do not branch on language names or
maintain a Learning registry of languages, concepts or examples.

```text
Selected contributors: cpp:direction, win32:overview, msvc:toolchain
Learner records: follow the selected orientation skills to their plain learning data.
Lesson: trace one request from client call to driver boundary.
Teaching order: explain the unfamiliar Windows boundary first, then use the
existing C++ request code as the short concrete example.
Knowledge result: unchanged until the learner demonstrates understanding.
```

## Delivery mode and study mode

The default mode is guided delivery: the agent implements and validates the
authorized code while explaining the smallest useful lesson before or alongside
the relevant change. Do not repeatedly ask who writes the code. Switch to study
mode only when the learner asks to author the learning step; provide a bounded
specification, teach prerequisites first, and review their attempt.

Delivery may advance faster than study. A delivery-mode explanation is a study
lead, not proof of understanding. Only the subject owner changes its knowledge
inventory, and only after the learner supplies the evidence that owner requires.

## Learning checkpoint

Keep one repository-local `learning/checkpoint.md` when durable study context is
needed. It is not an engineering plan, delivery ledger, task tracker, or second
knowledge inventory. Record only:

- `Mode`: `guided-delivery` or `study`.
- `Active lesson`: one concrete concept or request path.
- `Learner evidence`: the learner's explanation, question, or independently
  authored attempt; use `none yet` when absent.
- `Next study action`: one bounded next learning action.

```markdown
# Learning checkpoint

- Mode: guided-delivery
- Active lesson: how the client request crosses the Windows/driver boundary
- Learner evidence: none yet
- Next study action: explain why the client cannot invoke the driver directly
```

Never put implementation status, completed tests, a delivery checklist, or a
knowledge promotion in this file. When a lesson becomes stale, replace it with
the current lesson rather than retaining a history.
