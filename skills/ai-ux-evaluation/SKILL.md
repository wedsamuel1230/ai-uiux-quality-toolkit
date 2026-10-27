---
name: ai-ux-evaluation
description: Design or interpret evaluations of AI product behavior across representative tasks, users, interface states, and releases. Use when measuring an assistant, agent, recommender, AI feature, or conversational interface beyond a one-off visual review.
metadata:
  pattern: pipeline
---

# AI Product UX Evaluation

Load `references/evaluation-basis.md` when designing lifecycle, production, appeal, or conversational-accessibility measures. Check the live source version when a result will be used for a current policy or standards claim.

## Workflow

1. **Define context and decision.** Name the AI capability, users, tasks, deployment setting, expected human oversight, and what product decision the evaluation can change.
2. **Separate evaluation layers.** Track model/content quality, interface comprehension and control, operational reliability, and user outcomes separately. A technically correct response can still be inaccessible, misleading, late, or hard to correct.
3. **Set representative scenarios.** Include normal tasks, ambiguity, unsupported requests, stale or missing data, refusal, correction, timeout, service outage, partial completion, and recovery. Add modality-specific cases for voice, image, or mixed input/output.
4. **Choose measures before testing.** Select a small primary measure plus safety and user-control guardrails. Depending on the task, consider task completion (with numerator/denominator), critical error rate, correction/edit burden, time to recover, abandonment, successful appeal/override, understanding of AI limits, trust calibration, latency, and disparities across relevant user groups.
5. **Plan participants and data.** Recruit people who reflect the deployment context and affected users. Provide accommodations, consent, minimal data collection, and retention/deletion rules. Do not treat synthetic users or model judgments as participant results.
6. **Run and record.** Capture actual build/model version, task, environment, observed steps, outcome, and failures. Distinguish participant behavior, model/system logs, and researcher interpretation.
7. **Analyze tradeoffs and uncertainty.** Report sample and measurement limits. Do not infer population-wide performance from small exploratory samples or treat a high satisfaction score as evidence of task success or safety.
8. **Plan ongoing evaluation.** For deployed or changing systems, monitor for quality/risk shifts, establish user feedback and appeal routes, retest after meaningful updates, and define owners and thresholds for investigation.
9. **Report.** State what changed, what passed/failed/not tested, and which human or operational decisions remain open.

## Voice and multimodal branch

For speech or conversational systems, test a non-speech alternative where feasible, enough response time, pause/repeat/review options, visible conversation history where useful, simple repair, interruption/correction, and a real path to human help. Test users with diverse speech patterns and access needs. Check privacy boundaries for voice, transcripts, retention, and human review. Do not assume that a voice interface alone makes the entire task accessible; inspect outputs and downstream controls too.

## Output structure

Use a concise table with `measure`, `definition`, `sample/context`, `observed result`, `evidence`, `threshold or comparison`, and `status`. Separate model, UI, operational, and human-study evidence. Include limitations and the next evaluation step.
