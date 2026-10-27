# Skill Trigger Cases (Design-Time Evaluation Set)

These are representative prompts and expected routes for a future skill invocation check. They are evaluation cases, not user studies, and were not run against a separate model.

| Prompt | Expected route | Baseline risk without this skill |
|---|---|---|
| “Audit this subscription screen. Compare how many steps it takes to subscribe and cancel, and check the privacy settings.” | `deceptive-design-audit`, with `a11y-audit` if accessibility is in scope | Generic visual review may miss asymmetric choices, repeated prompts, hidden cost, or blocked exit. |
| “Make the dashboard look more modern; use a dark palette.” | `uiux-master`; load the visual catalog only if useful | The audit skill should not trigger solely because the screen has a CTA or dark mode. Contrast and existing design system still matter. |
| “Our assistant can draft and send calendar invites. Evaluate whether people understand what will be sent and recover from partial failure.” | `human-ai-review` and `ai-ux-evaluation` | Static UI review may miss external receipts, approval, correction, and post-send state. |
| “The new voice assistant feels confusing. Test alternatives for people who cannot or do not want to speak.” | `ai-ux-evaluation` with its voice branch; `a11y-audit` if a standards audit is requested | A text-only flow review may miss timing, non-speech access, transcript review, and human fallback. |
| “What is a good font pairing for a portfolio?” | Use the resource catalog if helpful; no research or audit skill by default | Over-triggering a compliance or research workflow would add friction to a simple inspiration request. |
| “Did users prefer the new AI answer layout?” | `ux-research` or `ai-ux-evaluation`, depending on available evidence | A model judgment or invented persona could be mistaken for actual participant evidence. |

## Trigger quality checks

- Positive: a specialist skill should activate for the task it owns.
- Negative: an ordinary visual preference or one-off component question should not launch the whole suite.
- Ambiguous: choose a narrow master workflow, inspect available evidence, and ask only when the missing decision changes the evaluation scope or user impact.
