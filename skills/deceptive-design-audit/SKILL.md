---
name: deceptive-design-audit
description: Review websites and apps for manipulative or deceptive interface patterns that undermine informed user choice. Use for consent, privacy settings, subscriptions, cancellation, pricing, upsell, notification, account deletion, or high-pressure conversion flows.
metadata:
  pattern: reviewer
---

# Deceptive Design Audit

Load `references/research-basis.md` when naming a pattern, connecting a finding to a source, or assessing legal scope. The sources are review frameworks, not an automatic legal verdict.

## Audit workflow

1. Define the product, user task, target audience, platform/region if known, and the exact flow under review. Include both the desired action and the user's reasonable alternative, such as decline, cancel, pause, or leave.
2. Observe the complete flow from entry to outcome. Capture page/state, sequence, labels, defaults, number of steps, and evidence. Do not infer the behavior from a marketing screenshot or source link.
3. Compare the user's available choices. Check whether accept and decline, subscribe and cancel, enable and disable, or continue and leave are similarly clear, reachable, and reversible.
4. Check for patterns such as repeated prompts after refusal, privacy mazes, hidden settings, confusing toggles, preselected extras, false urgency/scarcity, disguised ads, hidden prices/fees, obstructed cancellation, forced disclosure, and visually asymmetric buttons.
5. Evaluate the likely effect on informed choice, money, privacy, time, attention, or access to the primary task. Record who may carry extra burden and whether the result is supported by direct evidence.
6. Classify the finding as an observed pattern, a plausible risk, or a question needing more evidence. Do not label a design unlawful based only on a pattern match.
7. Propose a user-respecting fix: clear and comparable choices, accurate claims, understandable cost/data terms before commitment, a simple exit/cancel path, and defaults aligned with the stated user preference.
8. Retest the full flow, including decline/cancel and return paths, if a change is implemented.

## Severity

Use the project's severity scale. If none exists, use a descriptive severity with impact and reach. Do not invent P0/P1 blockers or let a composite score hide serious coercion, financial harm, privacy loss, or blocked exit.

## Finding format

- **Flow and state:** exact screen/step and platform/build.
- **Evidence:** screenshot, URL, recording, or reproducible steps actually captured.
- **Pattern/risk:** concise label and source scope.
- **Choice impact:** what the user intended, what the interface steers toward, and the likely harm.
- **Affected users:** evidence-backed groups or clearly labeled hypotheses.
- **Recommendation:** specific design change and required retest.
- **Status:** `PASS`, `FAIL`, `NOT_TESTED`, `NEEDS_HUMAN_REVIEW`, or `NOT_APPLICABLE`.

For jurisdiction-specific interpretations, route to qualified legal/privacy review. This skill does not provide legal certification.
