---
name: a11y-audit
description: Evaluate accessibility in web, Android, iOS, desktop, and cross-platform interfaces with the correct platform guidance and evidence. Use for accessibility reviews, implementation checks, assistive-technology testing, or remediation planning.
metadata:
  pattern: reviewer
---

# Accessibility Audit

Load `references/platform-standards.md` for the relevant target platform and current authoritative sources.

## Review workflow

1. Identify platform, build/version, primary task, affected components, user input/output modes, and available assistive technology.
2. Select the applicable normative standard and platform guidance. Keep web CSS pixels, Android dp, and Apple points separate. Do not present a platform recommendation as a WCAG requirement.
3. Inspect source semantics and rendered behavior: keyboard order and focus, names/roles/states, touch targets, contrast, zoom/text scaling, reflow, error identification, dynamic updates, reduced motion, and media alternatives as applicable.
4. Run existing automated accessibility checks when available and relevant. Record tool, version, scope, and failures. Treat automated results as a subset of coverage.
5. Perform human keyboard and screen-reader checks when the task/platform requires them. If they were unavailable or skipped, record `NOT_TESTED` or `NEEDS_HUMAN_REVIEW`.
6. Report each issue with location, user impact, applicable criterion/guidance, evidence, severity, fix, and retest status.

## Severity and evidence

Use the project severity scale when one exists. Otherwise use P0–P4 only if the project defines it. A conformance claim requires an applicable criterion, complete relevant test scope, and current evidence. An axe pass, token contrast check, or screenshot alone does not certify WCAG conformance or accessibility.

Report `PASS`, `FAIL`, `NOT_TESTED`, `NEEDS_HUMAN_REVIEW`, or `NOT_APPLICABLE`. Never convert a missing tool or unavailable device into a pass.
