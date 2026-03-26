# STDF Chat UI — Architecture Approaches

4 approaches compared, from heaviest to lightest. Analysis quality is identical across all — same 16 agents, same prompts. The difference is only the UI chrome.

**Timelines assume Claude Code does the implementation.**

---

## Approach A: Full Stack (Current Spec)

```
User → React UI → WebSocket → FastAPI Server → Claude Agent SDK
                                    ↓
                              Session Manager
                              MCP Tool Server
                              Hooks (progress, guardrails, questions)
                              Agent Loader
                              Orchestrator Prompt Builder
                                    ↓
                              Claude Session → 16 agents
```

**What you build:** 6 backend modules, React frontend with DAG sidebar, analysis tabs, streaming, AskUserQuestion renderer

| Pros | Cons |
|------|------|
| Rich UI (DAG viz, tabs, cost breakdown) | ~2-3 hours effort |
| Multi-user isolation | 6 Python modules to maintain |
| Real-time progress via hooks | MCP tool wrapping is boilerplate |
| Concurrent analyses per user | Over-engineered for POC |

---

## Approach B: Thin Chat Wrapper (Recommended)

```
User → Simple Chat UI → Single API endpoint → Claude Agent SDK Client
                                                      ↓
                                               One Claude session
                                               (system prompt has everything)
                                                      ↓
                                               Agent tool → 16 agents
                                               Reads/writes output files
                                               Talks back to user directly
```

**What you build:** 1 API endpoint, 1 Claude session config, 1 chat page

| Pros | Cons |
|------|------|
| ~30-45 min effort | No DAG visualization |
| Claude handles everything — orchestration, errors, follow-ups | No per-agent progress indicators |
| No hooks, no MCP server, no session manager | Single user (or simple isolation) |
| Identical analysis quality — same agents, same prompts | Cost/timing not shown per-agent |
| Follow-ups and re-runs are just chat messages | No concurrent analysis tabs |

```
server/
├── main.py          # FastAPI, one POST /chat endpoint
├── config.py        # Paths, model settings
frontend/
├── index.html       # Single page chat (or Streamlit)
```

---

## Approach C: Zero UI — Claude Code CLI Directly

```
User → Terminal → claude -p "Analyze energy storage using STDF"
                     ↓
               Claude Code (already exists)
               /stdf skill (already exists)
               Agent tool → 16 agents (already exist)
                     ↓
               output/<slug>/ files on disk
               User reads in terminal or opens .md files
```

**What you build:** Nothing. It already works today.

| Pros | Cons |
|------|------|
| 0 days effort | Terminal only — no web UI |
| Already working end-to-end | No shareable link |
| Full /stdf skill with all features | Single user, local only |
| All follow-ups work in same session | Not demo-able to non-technical users |

---

## Approach D: Streamlit One-File App

```
User → Streamlit Chat UI → claude-code subprocess (or Agent SDK)
              ↓                        ↓
        st.chat_message          Claude session
        st.status                Agent tool → 16 agents
        st.markdown              output/ files
```

**What you build:** 1 Python file (~150 lines)

| Pros | Cons |
|------|------|
| ~15-20 min effort | Streamlit aesthetics (not custom) |
| Built-in chat UI, streaming, markdown | Limited layout customization |
| st.status gives agent progress for free | Harder to do WebSocket-style events |
| Can wrap claude CLI via subprocess | Streamlit rerun model can be awkward |
| Shareable via streamlit run | Not production-grade |

---

## Side-by-Side Comparison

| | A: Full Stack | B: Thin Chat | C: CLI (exists) | D: Streamlit |
|---|---|---|---|---|
| **Effort** | ~2-3 hours | ~30-45 min | 0 | ~15-20 min |
| **Backend modules** | 6 | 1 | 0 | 1 file |
| **Frontend** | React + Tailwind | Minimal HTML or React | Terminal | Streamlit |
| **DAG visualization** | Yes | No | No | Partial (st.status) |
| **Multi-user** | Yes | Basic | No | Basic |
| **Concurrent analyses** | Yes | No | No | No |
| **Follow-ups** | Yes | Yes | Yes | Yes |
| **Re-runs** | Yes (with UI) | Yes (chat-based) | Yes | Yes (chat-based) |
| **Analysis quality** | Same | Same | Same | Same |
| **Demo-able** | Very | Yes | No | Yes |
| **Production-ready** | Yes | POC | N/A | POC |

---

## Recommendation

Start with **Approach B** (thin chat wrapper) or **Approach D** (Streamlit) for fastest POC. Validate that chat-only UX works for users. Then selectively add pieces from Approach A (DAG sidebar, tabs) only if users actually ask for them.
