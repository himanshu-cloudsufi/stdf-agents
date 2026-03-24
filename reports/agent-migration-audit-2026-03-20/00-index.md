# Agent Migration Audit Index

Date: 2026-03-20
Scope:
- `old_prompts/`
- `chat_exports/tony/`
- `chat_exports/rgibbins/`
- `.claude/agents/`
- `.claude/shared-rules.md`

Corpus size:
- Legacy prompt/report files reviewed: 24
- New Claude agent files reviewed: 16
- Tony chat exports reviewed at corpus level: 51
- Robert Gibbins chat exports reviewed at corpus level: 171

Reports:
- `01-executive-summary.md`: management-level summary of findings and migration posture.
- `02-chat-issue-analysis.md`: user-reported failure patterns and repeated unmet needs from the chat exports.
- `03-business-logic-capability-matrix.md`: legacy-vs-new capability comparison focused on business logic, not code.
- `04-migration-gaps-and-risks.md`: missing or weakened rules, workflows, and domain coverage that matter operationally.
- `05-enhancement-backlog.md`: prioritized remediation and enhancement backlog.

Primary conclusion:
The new `.claude/agents/` system is materially stronger as a generic STDF-v2 analytical pipeline, but it is not yet capability-parity with the legacy prompt system at the product/business-logic layer. The largest gaps are not low-level technical details. They are in orchestration, domain-specific calibrated workflows, investment workflows, meta/history/trace behaviors, and anti-fabrication controls that users relied on in practice.
