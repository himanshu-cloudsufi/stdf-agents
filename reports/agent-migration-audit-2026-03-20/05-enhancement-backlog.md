# Enhancement Backlog

## Priority 0: Restore product parity for high-value business surfaces
### 1. Add a top-level routing and governance layer
Deliverables:
- reformulation / intent parser
- clarification gate
- system-level evaluator
- method-lock execution mode
- dispute-triggered re-verification path
- degraded-mode / retry / fallback policy

Reason:
The new STDF pipeline assumes these decisions are already solved. In the old product, they were not optional.

### 2. Reintroduce first-class sector workflows
Deliverables:
- `artificial-labor` agent or equivalent calibrated sub-pipeline
- `lithium-ion-demand` plus lead/lead-acid specialization
- `energy-sector` / SWB forecasting path
- `copper-forecast` path

Reason:
These were not just labels. They encoded hard business rules and user-trusted outputs.

### 3. Reintroduce investment workflows
Deliverables:
- `stellar`-style thesis construction agent
- value-driver long/short basket agent
- company-analysis and ticker-resolution layer
- optional VCA/value-chain agent

Reason:
The chats show persistent demand for investment-grade outputs, not only disruption diagnosis.

## Priority 1: Eliminate the most common user trust failures
### 4. Implement evidence-gated numerics and assumption contracts
Deliverables:
- every assumption must be source-tagged or explicitly user-confirmed
- confirmation-only mode before displacement-to-unemployment or other high-leverage conversions
- hard failure when scope assumptions are missing and cannot be safely inferred

Reason:
This directly targets “stop making stuff up” failures.

### 5. Add scope-lock QA before final synthesis
Checks:
- region
- metric type
- horizon
- observed vs forecast
- stock vs flow
- user-requested granularity

Reason:
Many chat failures were scope-control failures rather than raw analytic failures.

### 6. Add unresolved-issue memory and revision tracking
Deliverables:
- recognize repeated asks on the same topic
- summarize what was wrong last time
- show what changed in this run
- force explicit closure or flagged open gap

Reason:
Both users revisit unresolved topics repeatedly.

## Priority 2: Restore deterministic answer paths and meta behaviors
### 7. Add report-only retrieval mode
Deliverables:
- report lookup for precomputed sector outputs
- exact-label preservation
- exact table extraction
- canonical aggregation handling

Reason:
Known recurring domains should not require re-analysis every time.

### 8. Add first-class research ingestion
Deliverables:
- bulk SEC / IR / report retrieval
- batch parsing and indexing
- citation-backed extraction from uploaded and fetched reports
- portfolio-scale evidence collection workflows

Reason:
Users explicitly expect the system to autonomously pull filings and reports rather than relying on manual, one-document-at-a-time workflows.

### 9. Add trace/history/meta request support
Deliverables:
- trace explanation path
- session-history summarization path
- correction-aware “feedback only” path
- optional meeting/standup retrieval if still required by the business

Reason:
These behaviors increase trust and continuity and were explicitly represented in the legacy stack.

## Priority 3: Fill specific analytical gaps exposed by chats
### 10. Add robotics integration into labor-disruption modeling
Deliverables:
- physical-task automation curves
- robotics cost/capability integration
- China robotics data ingestion strategy

Reason:
The corpus contains explicit demand for this migration, and the lack of it creates structural blind spots.

### 11. Add empirical corroboration mode
Deliverables:
- compare model outputs to observed data over the last N months
- separate directional confirmation from level confirmation
- classify confirmed / revised / contradicted claims

Reason:
Gibbins explicitly asked for this and used it to validate labor claims.

### 12. Add data-reality reconciliation layer
Deliverables:
- proxy-based estimation when official datasets undercount reality
- confidence grading and method transparency
- explicit “official data lag vs inferred real-world adoption” framing

Reason:
Tony explicitly raised this need in distributed-solar contexts.

## Priority 4: Clean architectural follow-through
### 13. Resolve parity drift between old and new scenario policies
Deliverables:
- one global rule for when scenarios are allowed,
- one global rule for scenario count,
- one global rule for lag handling,
- one global rule for assumption disclosure.

### 14. Add backtesting and forecast-calibration loop
Deliverables:
- holdout validation on past disruptions
- calibration notes per domain
- confidence adjustment based on historical performance

### 15. Add explicit business-surface retirement decisions
For each missing legacy surface, decide one of:
- migrate,
- replace,
- retire.

Reason:
Right now, several surfaces appear accidentally missing rather than intentionally retired.

## Suggested Sequencing
1. Routing/governance layer
2. Sector-specialized workflows
3. Investment workflows
4. Assumption governance and scope QA
5. Report-mode retrieval
6. Meta/history/trace surfaces
7. Robotics and corroboration extensions
8. Calibration and cleanup

## Definition Of Done For Parity
Migration should not be called complete until the new system can do all of the following:
- answer recurring labor, lead, energy, and copper questions without generic-model drift,
- refuse fabrication by construction,
- translate disruption into investment outputs,
- recover cleanly from user corrections and disputed claims,
- explain prior outputs and maintain session continuity,
- fall back gracefully instead of returning empty responses.
