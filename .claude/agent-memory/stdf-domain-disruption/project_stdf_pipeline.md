---
name: STDF v2 Pipeline Architecture
description: Current state of the STDF multi-agent pipeline — agents, flow, and conventions
type: project
---

STDF v2 is a 6-agent pipeline running in Claude Code. Domain Disruption (Category 1) feeds into Cost Curve (Category 2), Capability (Category 3), Tipping Point (Category 5), Adoption S-Curve (Category 4), and Synthesizer.

**Why:** User is systematically analyzing technology disruptions across sectors using the Seba/RethinkX framework. The pipeline produces structured JSON outputs designed for agent-to-agent handoff.

**How to apply:** Always output strict DomainDisruptionResponse JSON. The handoff_context field is critical — downstream agents (cost-curve, capability, tipping-point) depend on it for data anchors. Never omit key_cost_data or s_curve_positions.

Key conventions:
- Never use banned vocabulary (transition, renewable energy, net zero, green, sustainable, Wright's Law, IEA/EIA/BNEF/OPEC, clean energy, decarbonization, hydrogen economy)
- Always use: disruption, stellar energy, cost-curve dynamics, market-driven disruption, incumbent displacement, S-curve adoption
- Output must be valid JSON conforming to DomainDisruptionResponse schema
