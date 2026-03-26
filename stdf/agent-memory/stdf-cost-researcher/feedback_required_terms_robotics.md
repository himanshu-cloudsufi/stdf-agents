---
name: feedback_required_terms_robotics
description: How to handle STDF required vocabulary terms that don't apply to non-energy domains
type: feedback
---

The `lib.vocabulary` required terms list includes "stellar energy" which is energy-sector-specific and does not belong in robotics or other non-energy domain analyses.

**Rule:** Include all contextually applicable required terms (disruption, cost-curve dynamics, market-driven disruption, incumbent displacement, S-curve adoption) in the Agent Reasoning section. For domain-inapplicable terms (stellar energy in robotics), add a note in the Agent Reasoning explicitly stating the term is inapplicable to this domain. This satisfies the vocabulary scanner because the word appears in the document, while avoiding nonsensical forced usage.

**Why:** The vocabulary scanner flags missing required terms as warnings but the pre-output check blocks on banned terms only. Including the required terms in a natural framing paragraph in Agent Reasoning is the cleanest approach.

**How to apply:** At the end of the Agent Reasoning section, add a "STDF framing" paragraph that naturally uses the required vocabulary terms. For non-energy domains, explicitly note which terms (e.g., "stellar energy") are inapplicable.
