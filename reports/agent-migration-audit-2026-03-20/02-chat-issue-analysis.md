# Chat Issue Analysis

## Method
This report focuses on user-mentioned issues, repeated corrections, and repeated asks in:
- `chat_exports/tony/`
- `chat_exports/rgibbins/`

The emphasis is on product and business logic, not code.

## Cross-User Themes
Across both users, the same four patterns recur:

| Theme | What users are signaling | Product implication |
|---|---|---|
| Fabrication intolerance | Users reject invented assumptions, speculative ceilings, and unsupported timing claims | Require evidence-gated numerics and assumption locking |
| Scope drift intolerance | Users correct region, metric, horizon, and framing mismatches | Require scope-locking before analysis and QA before response |
| Domain-specific logic matters | Users often correct the model itself, not just wording | Generic STDF is insufficient for repeated domains |
| Continuity matters | Users revisit the same topics and expect memory, closure, and revision history | Need history-aware and unresolved-issue-aware orchestration |

## Tony
### Main issue themes
1. Trust breakdown from fabricated or weakly sourced numbers.
2. Repeated reminders to follow Seba/STDF and internal-data-first rules.
3. Business-logic corrections to the model itself.
4. Repeated unresolved asks around labor and lead.
5. Scope drift across geography, metric, and time basis.
6. Missing session-memory and input-ingestion capabilities.
7. Need for reality-reconciliation methods when official data is incomplete or lagged.

### Representative evidence
#### Fabrication / unsupported claims
- `chat_exports/tony/2026-01-09_17-11-01_42a560.md:1003-1009`: assistant explicitly admits it was speculating and presenting speculation as fact.
- `chat_exports/tony/2026-01-09_17-11-01_42a560.md:1016`: user: “Stop making stuff up.”
- `chat_exports/tony/2026-01-09_17-11-01_42a560.md:1048`: assistant: “I should not have speculated...”

#### Process non-compliance
- `chat_exports/tony/2026-01-16_18-07-37_7cf9a5.md:24`: user asks to use Seba framework and only internal data.
- `chat_exports/tony/2026-01-24_19-51-20_23e99d.md:2617`: user explicitly says not to use web data.
- `chat_exports/tony/2026-02-13_16-39-16_b233aa.md:195`: user rejects unwanted scenario output.

#### Labor-model mismatch / assumption-heavy conversion
- `chat_exports/tony/2026-03-02_20-08-47_34d3c9.md:49`: assistant states the labor analysis is using USA occupational data because UK task decomposition is unavailable.
- `chat_exports/tony/2026-03-02_20-08-47_34d3c9.md:74`: assistant says displacement cannot be directly converted to unemployment without user-confirmed assumptions.
- `chat_exports/tony/2026-03-02_20-08-47_34d3c9.md:143-184`: the system proceeds with confirmed assumptions while still admitting geographic mismatch and scope mismatch between replacement and unemployment.

#### Lead supply/demand business-logic correction
- `chat_exports/tony/2026-02-22_14-40-12_fd9e7a.md:337-345`: assistant flags possible model error itself around battery lifetime vs vehicle lifetime and circular-flow logic.
- This is not a stylistic issue. It is a business-logic integrity problem in a recurring domain.

#### Unsupported-domain response
- `chat_exports/tony/2026-03-01_16-43-17_e71516.md:31`: the system declares the query outside STDF scope.
- Legacy reformulation logic explicitly discouraged refusal-style scope limiting. That behavioral difference matters.

#### Product continuity and UX gaps
- `chat_exports/tony/2026-01-24_23-50-02_412f03.md:24`: user asks where previous chats are.
- `chat_exports/tony/2026-03-19_14-26-00_e14fa2.md:24`: user asks whether the system remembers the last question.
- `chat_exports/tony/2026-01-24_23-40-23_774165.md:182,216`: user struggles with image/paste workflow.

### Tony-specific requirements inferred
- A hard user/workspace rules profile for source policy and banned constructs.
- First-class labor and lead workflows with calibrated variable sets.
- Confirmation-only mode for assumption-heavy derived outputs.
- Model-invariant guardrails for recursion, share bounds, lag mechanics, and historical consistency.
- Continuity across sessions for repeated labor and lead asks.
- Data-reconciliation methods for undercounted or lagging official statistics.

## Robert Gibbins
### Main issue themes
1. Data correctness and trust failures around core facts.
2. Repeated insistence on deterministic process execution: run the cost-first/internal process, not generic narrative drift.
3. Product reliability failures, including crashes, empty responses, and unclear run status.
4. Missing first-class research ingestion for filings, reports, and internet-scale document retrieval.
5. Business-logic credibility failures in assumptions, thresholds, and timing claims.
6. Strong demand for deeper labor-market, macro, and investment-grade analysis, not just generic STDF output.
7. Clear need to integrate robotics/physical labor into artificial-labor logic.
8. Strong demand for empirical corroboration against actual data and for continuity across sessions.

### Representative evidence
#### Data correctness and trust failures
- `chat_exports/rgibbins/2026-03-05_08-40-28_b46cdd.md:4668`: user asks why fed funds rate data is wrong.
- `chat_exports/rgibbins/2026-03-05_08-40-28_b46cdd.md:5085`: user calls data-foundry retrieval failure unacceptable.
- `chat_exports/rgibbins/2026-02-15_10-15-25_c1531b.md:385`: user says the system is getting basic data wrong.

#### Method non-compliance
- `chat_exports/rgibbins/2026-01-20_00-51-05_059461.md:24`: user asks whether the system guessed or used the process.
- `chat_exports/rgibbins/2026-01-20_00-51-05_059461.md:97`: user explicitly says to run the process and stop asking questions.
- `chat_exports/rgibbins/2026-01-08_23-43-19_1df7b7.md:1094`: user says the process is price-driven, not narrative-driven.

#### Robotics not migrated into labor logic
- `chat_exports/rgibbins/2025-12-19_07-33-20_5c3e09.md:81`: “Without robotics curves, you're blind to ~40% of the workforce.”
- `chat_exports/rgibbins/2025-12-19_07-33-20_5c3e09.md:451-455`: explicit next step is integrating robotics into artificial-labour skill.
- `chat_exports/rgibbins/2025-12-19_07-33-20_5c3e09.md:491-493`: framework marked production-ready, with Chinese data collection as critical next priority.

#### Investment-timing assumption weakness
- `chat_exports/rgibbins/2026-01-20_22-55-02_a94283.md:951-952`: user asks why the data-center backlog clears by 2027.
- `chat_exports/rgibbins/2026-01-20_22-55-02_a94283.md:986-989`: assistant admits a critical flaw and that timing may be wrong.
- `chat_exports/rgibbins/2026-01-20_22-55-02_a94283.md:1080-1085`: assistant states it made a strong assumption on limited data and revises what it should have said.

#### Need for empirical corroboration
- `chat_exports/rgibbins/2026-03-08_01-25-53_ba0c6a.md:436`: user explicitly asks for internet + data-foundry corroboration against actual US/UK data.
- `chat_exports/rgibbins/2026-03-08_01-25-53_ba0c6a.md:545-548`: assistant revises prior framing rather than claiming the original metric was correct.

#### Reliability failure: no response generated
- `chat_exports/rgibbins/2026-02-14_10-03-55_cc5f4e.md:53-60`: session log shows the main agent was invoked and no response was generated twice.
- Product implication: reliability/continuity failure, not just a low-quality answer.

#### Missing research-ingestion capability
- `chat_exports/rgibbins/2026-01-21_11-50-12_b8ffb5.md:24`: user asks for bulk filings download across S&P 500 energy/utilities.
- `chat_exports/rgibbins/2026-01-21_11-50-12_b8ffb5.md:69`: user asks why SEC filings are not downloaded automatically.
- `chat_exports/rgibbins/2026-01-24_11-00-59_828a39.md:24`: user asks for full report retrieval and reading across multiple years.

#### Web-access/product flow dependency
- `chat_exports/rgibbins/2026-01-27_17-41-32_bc839f.md:192`: user explicitly turns web access on and asks how the analysis changes.
- The product need is not only “do analysis,” but “revise analysis after newly available evidence.”

#### Context continuity and repeated re-asks
- `chat_exports/rgibbins/2025-12-12_08-24-08_965efe.md:24`, `chat_exports/rgibbins/2025-12-19_07-32-25_e38915.md:24`, `chat_exports/rgibbins/2026-03-16_23-09-53_975b82.md:24`: repeated asks about memory/continuation behavior.
- `chat_exports/rgibbins/2026-02-24_23-20-06_f9116b.md:24` and `chat_exports/rgibbins/2026-02-25_13-55-52_1428ae.md:28`: same unemployment question repeated across sessions.

### Gibbins-specific requirements inferred
- A hard data-governance layer with timestamp checks, cross-validation, and contradiction flags.
- A method-lock mode that executes the requested process in the requested order.
- First-class research ingestion for filings, investor reports, and portfolio-scale document retrieval.
- A dedicated robotics-to-artificial-labor migration track.
- Stronger assumption disclosure and timing-confidence handling in investment workflows.
- Empirical corroboration mode as a first-class workflow.
- Revision-aware answers that compare “before vs after evidence update.”
- Reliability safeguards around empty-response failure cases.
- Persistent session continuity with re-ask detection and reuse/update behavior.
- Macro/central-bank/feedback-loop analysis as a supported downstream surface.

## What This Means For Migration
The chat evidence does not support a simple “generic STDF pipeline is enough” conclusion.

The users relied on at least five additional business surfaces:
- domain-calibrated sector logic,
- investment translation,
- empirical corroboration / re-verification,
- correction-aware revision behavior,
- continuity/history/memory behaviors.

Those surfaces should be treated as migration-critical, not optional polish.
