# Research Basis: AI Product Evaluation and Conversational Accessibility

## NIST AI Risk Management Framework

- [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- The Measure function describes evaluation, benchmarking, monitoring, documentation, feedback, and tracking risks over time. Measure 3.3 specifically calls for end-user and affected-community feedback/appeal processes to be integrated into evaluation metrics.
- The framework is voluntary guidance. NIST's current overview says AI RMF 1.0 is being revised, so check its status before using it for current policy claims.

## Generative AI profile

- [NIST AI 600-1, Generative Artificial Intelligence Profile (2024)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
- Includes actions for capturing structured user feedback about AI-generated content and using feedback to detect shifts in quality or alignment. Treat these as risk-management practices to adapt, not a ready-made UX metric set.

## Conversational and voice accessibility

- [W3C Cognitive Accessibility Research Modules: Voice Systems and Conversational Interfaces (Group Note Draft, 2026)](https://www.w3.org/TR/coga-voice/)
- The draft discusses memory, processing time, speech recognition diversity, interruptions, alternative non-speech input, simple recovery, human fallback, and reviewing dialogue. It is explicitly a work in progress, not a normative standard.
- [W3C Natural Language Interface Accessibility User Requirements](https://www.w3.org/TR/naur/)
- Covers natural-language interfaces as part of larger systems, including reviewable dialogue, adequate response time, multimodal alternatives, and confirmation before irreversible actions. Read relevant normative accessibility standards for the complete product interface.

## Measurement guardrails

- Define the task, context, measure, comparison, and stop threshold before testing.
- Preserve denominators and versions. Report when samples are exploratory or underpowered.
- Use participant and deployment evidence for user outcomes. A Jev probability, other model score, or static checklist can help triage; none substitutes for user testing or production monitoring.
