---
name: ux-research
description: Plan, conduct, or synthesize user research from actual participant and product evidence. Use for interviews, usability studies, field observation, diary studies, surveys, card sorts, tree tests, or research findings.
metadata:
  pattern: pipeline
---

# UX Research

## Workflow

1. State the product decision the research could change. Write no more than three neutral research questions and define the target task or behavior.
2. Choose a method that can answer those questions. Use interviews for context and motivation, usability observation for task behavior, and quantitative methods for measurable comparisons. Do not use a survey to claim observed behavior.
3. Define recruitment, inclusion criteria, setting, accessibility accommodations, sample limits, consent, data minimization, retention, and deletion. Do not infer protected traits from product telemetry unless lawful, necessary, and consented.
4. Prepare a neutral task and moderator guide. Obtain consent. Avoid teaching the interface before an unassisted task unless the study question requires instruction.
5. Record behavior separately from participant quotations and researcher interpretation. Note task completion, errors, recovery, timing, and context only when actually observed.
6. Synthesize themes with supporting evidence and counterexamples. Small exploratory samples can reveal issues; they do not establish population rates or saturation by themselves.
7. Map each finding to an evidence item, confidence/limitation, product implication, and a testable next step.

## Hard requirements

- Never invent interviews, participants, survey results, usability metrics, or representative personas.
- Label generated personas, synthetic users, and model-generated interpretations as hypotheses or analysis aids, not human evidence.
- Keep participant data private and collect only what the study needs.
- Report sampling, accessibility, setting, and method limits.

## Default output

Provide the decision and research questions, method and participants actually reached, findings with evidence, counterevidence, limits, implications, and next study or design experiment. Use the supplied `templates/UX_RESEARCH.md` as a starting point when present in the project.
