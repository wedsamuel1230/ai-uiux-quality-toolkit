# Optional TypeSafe / Jev Judgments

Use this only when TypeSafe or Jev is available and the task authorizes the data sharing. Read the live documentation for the exact model, API, limits, and SDK behavior before building an integration.

- [TypeSafe System One](https://docs.typesafe.ai/concepts/system-one.md)
- [How to build with TypeSafe](https://docs.typesafe.ai/concepts/how-to-build-with-system-one.md)
- [Question primitives](https://docs.typesafe.ai/primitives.md)
- [Confidence](https://docs.typesafe.ai/confidence.md)

TypeSafe's docs describe Jev as a source of typed judgments: `Choice` for a closed set, `Score` for defined ordered levels, and `Noul` for a yes/no probability. Keep control flow, deterministic checks, permissions, side effects, and postcondition verification in code or the responsible host. A probability is not evidence that a user agrees or that a task succeeded. Minimize state, keep sensitive data out unless authorized, and route low-confidence or high-impact decisions to appropriate review.
