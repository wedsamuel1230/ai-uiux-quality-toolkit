# AI UI/UX Quality Toolkit

Evidence-led skills for building and reviewing user-facing products. The toolkit connects design intent, platform-aware implementation, accessibility, human–AI interaction and verification.

## Skills

| Skill | Purpose |
| --- | --- |
| `uiux-master` | Coordinate interface tasks and select relevant guidance. |
| `ux-research` | Plan and synthesize participant and product research. |
| `a11y-audit` | Review accessibility across web and native platforms. |
| `human-ai-review` | Examine AI uncertainty, user control, action status and recovery. |
| `ai-ux-evaluation` | Evaluate AI product behavior across tasks and contexts. |
| `deceptive-design-audit` | Review consent, subscription, cancellation and other choice flows. |

## Use

The repository contains portable `skills/<name>/SKILL.md` directories and a plugin manifest. Import the repository or individual skills using a compatible Agent Skills host. When explicit selection is supported, choose `uiux-master` as the entry point and describe your task, platform and authorized scope. Exact installation and invocation depend on the host; cross-host installation has not yet been independently verified.

Example: “Review this subscription flow for cancellation friction. Do not edit files.” The intended route is `uiux-master` followed by `deceptive-design-audit` where available. This is instruction-based routing, not a deterministic dispatcher. The host decides which skills it exposes. If a requested skill is unavailable, use the built-in guidance and report the limitation.

## Evidence and limits

A read-only Codex test of version 0.1.4 found the specialist instructions and identified cancellation issues in a synthetic source fixture. Another run selected an unnecessary AI review skill and did not read the master coordinator. Version 0.1.5 narrows that trigger and clarifies the entry point; its automatic selection is not yet independently verified. No real-user research, full accessibility certification, native-device validation or live visual comparison is claimed. See [evaluation notes](evals/live-run-2026-10-27.md).

Third-party skills and tools are optional and are not installed by this package. Check their availability, versions and licenses before use. Automated checks do not replace human accessibility or usability testing.

## Validation

Run `python3 -m unittest discover -s tests -v`. These tests check manifest agreement, skill inventory, referenced files and key routing instructions. They do not establish that an agent selected a skill or that an interface works.

## Sources and contributions

The original toolkit materials were supplied under MIT; see [LICENSE.txt](LICENSE.txt). External products, repositories, assets and standards retain their own terms. Design references and source boundaries are recorded in the skill references. See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).
