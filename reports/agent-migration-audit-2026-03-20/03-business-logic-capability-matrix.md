# Business Logic Capability Matrix

## Reading Guide
Status meanings:
- `Present`: explicitly supported in the new system.
- `Partial`: some logic exists, but not at legacy parity.
- `Missing`: no clear equivalent in the new system.

## Matrix
| Capability / Rule | Legacy prompt system | New `.claude/agents/` system | Status | Audit note |
|---|---|---|---|---|
| Generic STDF disruption pipeline | Yes | Yes, more explicit | Present | New system is stronger here |
| Deterministic sector routing | Yes, mandatory via `sector_hints` + routing block | No explicit equivalent in agent set | Missing | Requires external orchestrator or new router |
| Specialized artificial-labor skill | Yes | No dedicated agent | Missing | Generic labor-capability analysis is not parity |
| Specialized lithium-ion + lead-acid + lead demand skill | Yes | Commodity chain exists, but no dedicated calibrated lead skill | Partial | Lead-specific driver map and report-mode missing |
| Specialized energy SWB forecasting skill | Yes | Generic STDF possible | Partial | Loses tuned SWB behavior and direct routing |
| Specialized copper forecasting skill | Yes | Commodity-demand chain supports copper | Partial | Commodity chain exists, but direct sector skill surface is gone |
| Precomputed sector reports + report lookup | Yes | No obvious equivalent | Missing | High value for deterministic recurring answers |
| Investment thesis workflow | Yes (`stellar`) | No direct equivalent | Missing | Critical for trade-expression asks |
| Value-driver long/short screening | Yes (`value_investment`) | No direct equivalent | Missing | Critical for company basket asks |
| Company analysis / ticker resolution / VCA | Yes | No direct equivalent | Missing | Important for public-market workflows |
| Feedback-loop / actor-reaction modeling | Yes | No direct equivalent | Missing | Needed for macro, rates, policy, system-reaction asks |
| Reformulator / anti-sycophancy intent parser | Yes | No explicit equivalent | Missing | New agents assume clean orchestration upstream |
| Clarification logic | Yes | No explicit equivalent | Missing | Important for scope control and assumption discipline |
| Evaluator / anti-pattern enforcement | Yes | No explicit equivalent | Missing | New agent compliance is local, not pipeline-wide adjudication |
| Citation builder / provenance assembly | Yes | No clear downstream equivalent | Missing | New system has traceability language but not full citation assembly surface |
| Trace explanation / history request handling | Yes | No direct equivalent | Missing | Important for user trust and transparency |
| Meeting / standup retrieval domain | Yes | No direct equivalent | Missing | Entire business surface appears removed |
| Web re-verification for disputed claims | Yes | Implicit evidence rules only | Partial | Missing explicit dispute-triggered branch |
| Identity-response matrix | Yes | No explicit equivalent | Missing | Business/brand behavior lost |
| Skill sovereignty | Yes, explicit | No direct equivalent | Missing | New system has traceability, not authoritative skill doctrine |
| Tiered derivation gating | Yes | No direct equivalent | Missing | Legacy had user-confirmation boundary |
| No fabricated scope assumptions | Yes, explicit | Partially covered by evidence rules | Partial | New system still allows assumptions sections in several agents |
| Lag exclusion by default | Yes | Not globally explicit | Partial | New agents vary by module |
| Regional minimums (China/USA/Europe) | Partial in old, explicit in some domains | Explicit across multiple agents | Present | New system stronger |
| Adoption readiness as explicit condition | No, less formal | Yes | Present | Material improvement |
| X-curve / market-trauma decomposition | Yes conceptually | Yes, explicit xcurve agent | Present | New system stronger |
| Commodity demand decomposition with anti-GDP proxy guardrails | Limited / domain-specific | Yes, explicit | Present | Strong improvement |
| Confidence aggregation across pipeline | Limited | Yes, explicit in synthesizer | Present | Strong improvement |

## Key Upgrade Areas In The New System
The new system clearly improves on the old one in:
- explicit staged decomposition,
- formal tipping-condition logic,
- adoption-readiness treatment,
- regional adoption analysis,
- x-curve and market-trauma formalization,
- commodity demand decomposition discipline,
- confidence aggregation.

## Key Regression Areas
The migration clearly regresses in:
- domain-specific calibrated workflows,
- investment workflows,
- orchestration layers,
- provenance/citation assembly,
- report-based deterministic answer paths,
- correction-aware and history-aware meta behaviors.

## Business Conclusion
The new system is not a superset of the old system.
It is a narrower but more rigorous STDF core.

That is a viable architecture decision only if the missing surfaces are intentionally retired.
The chat exports suggest they were not retired. Users were actively using them.
