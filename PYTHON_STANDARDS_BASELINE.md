# Python standards baseline

Existing violations at `463b221cc96f5f665873f718958d19b31a25f4aa` are baselined by exact authored file and rule. New files receive all enabled checks. Remove an exception when repairing its source. The tool configuration owns enforcement; this document records the rollout evidence and rationale.

## Ruff

Reason: preserve existing implementations during the standards rollout. Each row records the existing count and a representative required repair. No wildcard path or whole-rule ignores were added.

| File | Rule | Existing count | Required repair |
| --- | --- | ---: | --- |
| `.agents/sync_generated.py` | `ANN401` | 3 | Dynamically typed expressions (typing.Any) are disallowed in `load` |
| `.agents/tests/test_guide_build.py` | `PT009` | 3 | Use a regular `assert` instead of unittest-style `assertIn` |
| `.agents/tests/test_guide_build.py` | `TID251` | 1 | `unittest.TestCase` is banned: Use plain pytest functions and bare assertions. |

## Custom checker

Reason: preserve exact pre-existing custom-checker findings during the standards rollout. Each entry maps to one authored path and rule; repair the stated design issue and remove its exception. No generated or vendored path is included.

No pre-existing custom-checker findings were recorded.
