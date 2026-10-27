# Design routing and verification

Use this reference for design direction, building, redesign, and visual critique. Apply judgment rather than rigid aesthetic bans.

## Resolve the task

- Establish the user's primary job and actual content. Separate durable product facts from a surface's visual direction; reuse existing product and design documentation when present. Do not create persistent product documents unless requested or needed for a concrete handoff.
- Inspect the current design system and platform. A focused change preserves established patterns; a redesign changes only authorized scope. Capture existing navigation, forms, content, and behavior before a redesign and verify their preservation afterward.
- For a new visual direction, form a short hypothesis connecting audience, content, hierarchy, typography, color, layout, imagery and motion. Compare a small number of directions if that helps the decision; no mandatory theme or arbitrary style blacklist. Real content and approved assets beat fabricated claims. Check asset terms.
- Use optional skill instructions only if the host exposes them. Do not require a web-oriented skill for native applications. If advice conflicts, user constraints, project design system, accessibility and platform behavior prevail.

## Focused actions

Route by need: critique hierarchy and task clarity; polish visual consistency; harden empty, loading, error, long-text and recovery states; adapt responsive or native layouts; improve typography, color, layout or motion only within scope. Keep motion purposeful and respect reduced-motion preferences. Do not infer user preferences from a model-generated persona.

## Evidence and quality

- Safety floor: verify applicable functionality, readable text and contrast, visible focus, reduced motion, and relevant screen sizes or device settings. Record each as PASS, FAIL, NOT_TESTED, NEEDS_HUMAN_REVIEW or NOT_APPLICABLE with evidence; do not claim WCAG conformance from a scan.
- Heuristics: investigate repetitive decoration, weak hierarchy, unhelpful card nesting, stock-looking patterns or decorative motion. These are prompts for judgment, not universal failures; document intentional exceptions.
- Finish: review spacing, alignment, typography, state consistency and polish after material problems. Aesthetic scores cannot override a broken task or accessibility failure.
- Inspect rendered UI where possible, exercise the main task and relevant states, compare redesign behavior with the baseline, and run proportionate checks. If no browser, device or test environment is available, report the specific gap. A static detector is not usability research.

## Source inspiration, checked 2026-10-27

- Hallmark: https://github.com/Nutlope/hallmark — job-first layouts, before/after preservation and tiered checks.
- Taste Skill: https://github.com/Leonxlnx/taste-skill — brief-driven direction and browser iteration; its web tooling and runtime are optional.
- Impeccable: https://github.com/pbakaus/impeccable — separate product context from visual system and choose focused actions. Its detectors are not included here.
- UI UX Pro Max: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill — searchable design-system candidates.
- Anthropic frontend-design: https://github.com/anthropics/skills/tree/main/skills/frontend-design — subject-specific design decisions.

These are inspiration and optional external skills, not bundled dependencies. Verify licenses, versions and permissions before copying or executing third-party materials.
