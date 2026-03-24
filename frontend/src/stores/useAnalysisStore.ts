import { create } from "zustand";
import { persist, createJSONStorage } from "zustand/middleware";
import type {
  Analysis,
  AllowedPrompt,
  AnalysisStatus,
  AssistantMessage,
  ChatMessage,
  ContentBlock,
  Question,
  TodoItem,
} from "../types";

interface AnalysisStore {
  userId: string;
  analyses: Map<string, Analysis>;
  activeSlug: string | null;
  isConnected: boolean;

  setUserId: (userId: string) => void;
  setConnected: (connected: boolean) => void;
  setActive: (slug: string) => void;
  clearActive: () => void;

  addAnalysis: (slug: string, query: string) => void;
  removeAnalysis: (slug: string) => void;
  syncSessionMeta: (
    slug: string,
    sessionId: string | null,
    status: AnalysisStatus,
  ) => void;
  appendChunk: (slug: string, chunk: string) => void;
  appendThinking: (slug: string, chunk: string) => void;
  startToolCall: (slug: string, toolId: string, name: string) => void;
  appendToolInput: (slug: string, toolId: string, json: string) => void;
  setToolResult: (
    slug: string,
    toolId: string,
    result: string,
    truncated?: boolean,
    isError?: boolean,
  ) => void;
  endToolCall: (slug: string, toolId: string) => void;
  addAskUser: (slug: string, questions: Question[]) => void;
  addPlanApproval: (
    slug: string,
    plan: string,
    allowedPrompts: AllowedPrompt[],
  ) => void;
  markAnswered: (slug: string) => void;
  markComplete: (
    slug: string,
    cost: number,
    sessionId: string,
    extra?: { duration?: number; inputTokens?: number; outputTokens?: number },
  ) => void;
  addUserMessage: (slug: string, content: string) => void;
  setError: (slug: string, error: string) => void;
  setTodos: (slug: string, todos: TodoItem[]) => void;
  addSubToolCall: (
    slug: string,
    parentToolId: string,
    toolId: string,
    name: string,
  ) => void;
  updateSubToolInput: (
    slug: string,
    parentToolId: string,
    toolId: string,
    json: string,
  ) => void;
  setSubToolResult: (
    slug: string,
    parentToolId: string,
    toolId: string,
    result: string,
    truncated?: boolean,
    isError?: boolean,
  ) => void;
  endSubToolCall: (
    slug: string,
    parentToolId: string,
    toolId: string,
  ) => void;
  appendSubText: (slug: string, parentToolId: string, chunk: string) => void;
  appendSubThinking: (slug: string, parentToolId: string, chunk: string) => void;
}

function getOrCreateAssistantMsg(messages: ChatMessage[]): {
  messages: ChatMessage[];
  assistant: AssistantMessage;
} {
  const last = messages[messages.length - 1];
  if (last && last.role === "assistant") {
    return { messages: [...messages], assistant: last };
  }
  const newMsg: AssistantMessage = {
    id: crypto.randomUUID(),
    role: "assistant",
    blocks: [],
    timestamp: Date.now(),
  };
  return { messages: [...messages, newMsg], assistant: newMsg };
}

function updateLastAssistant(
  messages: ChatMessage[],
  updater: (msg: AssistantMessage) => AssistantMessage,
): ChatMessage[] {
  const result = [...messages];
  for (let i = result.length - 1; i >= 0; i--) {
    if (result[i].role === "assistant") {
      result[i] = updater(result[i] as AssistantMessage);
      return result;
    }
  }
  return result;
}

function updateAnalysis(
  state: { analyses: Map<string, Analysis> },
  slug: string,
  updater: (a: Analysis) => Partial<Analysis>,
): { analyses: Map<string, Analysis> } | typeof state {
  const analyses = new Map(state.analyses);
  const analysis = analyses.get(slug);
  if (!analysis) return state;
  analyses.set(slug, { ...analysis, ...updater(analysis) });
  return { analyses };
}

// ---------------------------------------------------------------------------
// Debounced localStorage wrapper — writes at most once per DEBOUNCE_MS,
// plus a synchronous flush on beforeunload so reloads never lose data.
// ---------------------------------------------------------------------------
const DEBOUNCE_MS = 2000;

interface DebouncedState {
  timer: ReturnType<typeof setTimeout> | null;
  pendingKey: string | null;
  pendingValue: string | null;
}

const _db: DebouncedState = { timer: null, pendingKey: null, pendingValue: null };

function flushStorage(): void {
  if (_db.pendingKey != null && _db.pendingValue != null) {
    localStorage.setItem(_db.pendingKey, _db.pendingValue);
  }
  _db.pendingKey = null;
  _db.pendingValue = null;
  if (_db.timer) {
    clearTimeout(_db.timer);
    _db.timer = null;
  }
}

if (typeof window !== "undefined") {
  window.addEventListener("beforeunload", flushStorage);
}

const debouncedStorage = {
  getItem(key: string): string | null {
    // Return pending (unflushed) value for read consistency
    if (_db.pendingKey === key && _db.pendingValue != null) return _db.pendingValue;
    return localStorage.getItem(key);
  },
  setItem(key: string, value: string): void {
    _db.pendingKey = key;
    _db.pendingValue = value;
    if (!_db.timer) {
      _db.timer = setTimeout(flushStorage, DEBOUNCE_MS);
    }
  },
  removeItem(key: string): void {
    if (_db.pendingKey === key) {
      _db.pendingKey = null;
      _db.pendingValue = null;
    }
    if (_db.timer) {
      clearTimeout(_db.timer);
      _db.timer = null;
    }
    localStorage.removeItem(key);
  },
};

// Custom storage that handles Map<string, Analysis> serialization
const mapStorage = createJSONStorage<AnalysisStore>(() => debouncedStorage, {
  reviver: (_key: string, value: unknown) => {
    // Convert serialized [key, value][] back to Map
    if (
      _key === "analyses" &&
      Array.isArray(value) &&
      value.length > 0 &&
      Array.isArray(value[0])
    ) {
      const map = new Map<string, Analysis>(value);
      // Reset stale streaming sessions to idle on rehydrate
      for (const [, a] of map) {
        if (a.status === "streaming") {
          a.status = "idle";
        }
      }
      return map;
    }
    return value;
  },
  replacer: (_key: string, value: unknown) => {
    if (_key === "analyses" && value instanceof Map) {
      return Array.from((value as Map<string, Analysis>).entries());
    }
    return value;
  },
});

export const useAnalysisStore = create<AnalysisStore>()(
  persist(
    (set) => ({
      userId: "user",
      analyses: new Map(),
      activeSlug: null,
      isConnected: false,

      setUserId: (userId) => set({ userId }),
      setConnected: (isConnected) => set({ isConnected }),
      setActive: (slug) => set({ activeSlug: slug }),
      clearActive: () => set({ activeSlug: null }),

      addAnalysis: (slug, query) =>
        set((state) => {
          const label =
            query.length > 40 ? query.slice(0, 40) + "..." : query;
          const analyses = new Map(state.analyses);
          const userMsg: ChatMessage = {
            id: crypto.randomUUID(),
            role: "user",
            content: query,
            timestamp: Date.now(),
          };
          analyses.set(slug, {
            slug,
            label,
            messages: [userMsg],
            status: "streaming",
            cost: null,
            sessionId: null,
            error: null,
            todos: [],
            createdAt: Date.now(),
          });
          return { analyses, activeSlug: slug };
        }),

      removeAnalysis: (slug) =>
        set((state) => {
          const analyses = new Map(state.analyses);
          analyses.delete(slug);
          const activeSlug =
            state.activeSlug === slug ? null : state.activeSlug;
          return { analyses, activeSlug };
        }),

      syncSessionMeta: (slug, sessionId, status) =>
        set((state) =>
          updateAnalysis(state, slug, (a) => ({
            sessionId: sessionId || a.sessionId,
            status:
              status === "streaming"
                ? "streaming"
                : a.status === "streaming"
                  ? "complete"
                  : a.status,
          })),
        ),

      appendChunk: (slug, chunk) =>
        set((state) =>
          updateAnalysis(state, slug, (analysis) => {
            const { messages, assistant } = getOrCreateAssistantMsg(
              analysis.messages,
            );
            const blocks = [...assistant.blocks];
            const lastBlock = blocks[blocks.length - 1];

            if (
              lastBlock &&
              lastBlock.type === "text" &&
              lastBlock.isStreaming
            ) {
              blocks[blocks.length - 1] = {
                ...lastBlock,
                content: lastBlock.content + chunk,
              };
            } else {
              blocks.push({ type: "text", content: chunk, isStreaming: true });
            }

            const idx = messages.findIndex((m) => m.id === assistant.id);
            messages[idx] = { ...assistant, blocks };
            return { messages, status: "streaming" };
          }),
        ),

      appendThinking: (slug, chunk) =>
        set((state) =>
          updateAnalysis(state, slug, (analysis) => {
            const { messages, assistant } = getOrCreateAssistantMsg(
              analysis.messages,
            );
            const blocks = [...assistant.blocks];
            const lastBlock = blocks[blocks.length - 1];

            if (lastBlock && lastBlock.type === "thinking") {
              blocks[blocks.length - 1] = {
                ...lastBlock,
                content: lastBlock.content + chunk,
              };
            } else {
              blocks.push({
                type: "thinking",
                content: chunk,
                isExpanded: false,
              });
            }

            const idx = messages.findIndex((m) => m.id === assistant.id);
            messages[idx] = { ...assistant, blocks };
            return { messages, status: "streaming" };
          }),
        ),

      startToolCall: (slug, toolId, name) =>
        set((state) =>
          updateAnalysis(state, slug, (analysis) => {
            const { messages, assistant } = getOrCreateAssistantMsg(
              analysis.messages,
            );
            const blocks: ContentBlock[] = [
              ...assistant.blocks,
              {
                type: "tool_call",
                toolId,
                name,
                input: "",
                status: "running",
                subEvents: [],
              },
            ];
            const idx = messages.findIndex((m) => m.id === assistant.id);
            messages[idx] = { ...assistant, blocks };
            return { messages, status: "streaming" };
          }),
        ),

      appendToolInput: (slug, toolId, json) =>
        set((state) =>
          updateAnalysis(state, slug, (analysis) => {
            const messages = updateLastAssistant(analysis.messages, (msg) => ({
              ...msg,
              blocks: msg.blocks.map((b) =>
                b.type === "tool_call" && b.toolId === toolId
                  ? { ...b, input: b.input + json }
                  : b,
              ),
            }));
            return { messages };
          }),
        ),

      setToolResult: (slug, toolId, result, truncated, isError) =>
        set((state) =>
          updateAnalysis(state, slug, (analysis) => {
            const messages = updateLastAssistant(analysis.messages, (msg) => ({
              ...msg,
              blocks: msg.blocks.map((b) =>
                b.type === "tool_call" && b.toolId === toolId
                  ? {
                      ...b,
                      result,
                      resultTruncated: Boolean(truncated),
                      isError: Boolean(isError),
                    }
                  : b,
              ),
            }));
            return { messages };
          }),
        ),

      endToolCall: (slug, toolId) =>
        set((state) =>
          updateAnalysis(state, slug, (analysis) => {
            const messages = updateLastAssistant(analysis.messages, (msg) => ({
              ...msg,
              blocks: msg.blocks.map((b) =>
                b.type === "tool_call" && b.toolId === toolId
                  ? { ...b, status: "done" as const }
                  : b,
              ),
            }));
            return { messages };
          }),
        ),

      addAskUser: (slug, questions) =>
        set((state) =>
          updateAnalysis(state, slug, (analysis) => {
            const { messages, assistant } = getOrCreateAssistantMsg(
              analysis.messages,
            );
            const blocks: ContentBlock[] = [
              ...assistant.blocks,
              { type: "ask_user", questions, answered: false },
            ];
            const idx = messages.findIndex((m) => m.id === assistant.id);
            messages[idx] = { ...assistant, blocks };
            return { messages, status: "streaming" };
          }),
        ),

      addPlanApproval: (slug, plan, allowedPrompts) =>
        set((state) =>
          updateAnalysis(state, slug, (analysis) => {
            const { messages, assistant } = getOrCreateAssistantMsg(
              analysis.messages,
            );
            const blocks: ContentBlock[] = [
              ...assistant.blocks,
              {
                type: "plan_approval",
                plan,
                allowedPrompts,
                answered: false,
              },
            ];
            const idx = messages.findIndex((m) => m.id === assistant.id);
            messages[idx] = { ...assistant, blocks };
            return { messages, status: "streaming" };
          }),
        ),

      markAnswered: (slug) =>
        set((state) =>
          updateAnalysis(state, slug, (analysis) => {
            const messages = updateLastAssistant(analysis.messages, (msg) => ({
              ...msg,
              blocks: msg.blocks.map((b) =>
                (b.type === "ask_user" || b.type === "plan_approval") &&
                !b.answered
                  ? { ...b, answered: true }
                  : b,
              ),
            }));
            return { messages };
          }),
        ),

      markComplete: (slug, cost, sessionId, extra) =>
        set((state) =>
          updateAnalysis(state, slug, (analysis) => {
            const messages = updateLastAssistant(analysis.messages, (msg) => ({
              ...msg,
              blocks: msg.blocks.map((b) =>
                b.type === "text" && b.isStreaming
                  ? { ...b, isStreaming: false }
                  : b,
              ),
            }));
            return {
              messages,
              status: "complete",
              cost,
              sessionId,
              duration: extra?.duration,
              inputTokens: extra?.inputTokens,
              outputTokens: extra?.outputTokens,
            };
          }),
        ),

      addUserMessage: (slug, content) =>
        set((state) =>
          updateAnalysis(state, slug, (analysis) => {
            const userMsg: ChatMessage = {
              id: crypto.randomUUID(),
              role: "user",
              content,
              timestamp: Date.now(),
            };
            const messages = updateLastAssistant(analysis.messages, (msg) => ({
              ...msg,
              blocks: msg.blocks.map((b) =>
                b.type === "text" && b.isStreaming
                  ? { ...b, isStreaming: false }
                  : b,
              ),
            }));
            return { messages: [...messages, userMsg], status: "streaming" };
          }),
        ),

      setError: (slug, error) =>
        set((state) =>
          updateAnalysis(state, slug, () => ({
            status: "error",
            error,
          })),
        ),

      setTodos: (slug, todos) =>
        set((state) => updateAnalysis(state, slug, () => ({ todos }))),

      addSubToolCall: (slug, parentToolId, toolId, name) =>
        set((state) =>
          updateAnalysis(state, slug, (analysis) => {
            const messages = updateLastAssistant(analysis.messages, (msg) => ({
              ...msg,
              blocks: msg.blocks.map((b) =>
                b.type === "tool_call" && b.toolId === parentToolId
                  ? {
                      ...b,
                      subEvents: [
                        ...b.subEvents,
                        {
                          toolId,
                          name,
                          input: "",
                          status: "running" as const,
                        },
                      ],
                    }
                  : b,
              ),
            }));
            return { messages };
          }),
        ),

      updateSubToolInput: (slug, parentToolId, toolId, json) =>
        set((state) =>
          updateAnalysis(state, slug, (analysis) => {
            const messages = updateLastAssistant(analysis.messages, (msg) => ({
              ...msg,
              blocks: msg.blocks.map((b) =>
                b.type === "tool_call" && b.toolId === parentToolId
                  ? {
                      ...b,
                      subEvents: b.subEvents.map((se) =>
                        se.toolId === toolId
                          ? { ...se, input: se.input + json }
                          : se,
                      ),
                    }
                  : b,
              ),
            }));
            return { messages };
          }),
        ),

      setSubToolResult: (
        slug,
        parentToolId,
        toolId,
        result,
        truncated,
        isError,
      ) =>
        set((state) =>
          updateAnalysis(state, slug, (analysis) => {
            const messages = updateLastAssistant(analysis.messages, (msg) => ({
              ...msg,
              blocks: msg.blocks.map((b) =>
                b.type === "tool_call" && b.toolId === parentToolId
                  ? {
                      ...b,
                      subEvents: b.subEvents.map((se) =>
                        se.toolId === toolId
                          ? {
                              ...se,
                              result,
                              resultTruncated: Boolean(truncated),
                              isError: Boolean(isError),
                            }
                          : se,
                      ),
                    }
                  : b,
              ),
            }));
            return { messages };
          }),
        ),

      endSubToolCall: (slug, parentToolId, toolId) =>
        set((state) =>
          updateAnalysis(state, slug, (analysis) => {
            const messages = updateLastAssistant(analysis.messages, (msg) => ({
              ...msg,
              blocks: msg.blocks.map((b) =>
                b.type === "tool_call" && b.toolId === parentToolId
                  ? {
                      ...b,
                      subEvents: b.subEvents.map((se) =>
                        se.toolId === toolId
                          ? { ...se, status: "done" as const }
                          : se,
                      ),
                    }
                  : b,
              ),
            }));
            return { messages };
          }),
        ),

      appendSubText: (slug, parentToolId, chunk) =>
        set((state) =>
          updateAnalysis(state, slug, (analysis) => {
            const messages = updateLastAssistant(analysis.messages, (msg) => ({
              ...msg,
              blocks: msg.blocks.map((b) =>
                b.type === "tool_call" && b.toolId === parentToolId
                  ? { ...b, subText: (b.subText ?? "") + chunk }
                  : b,
              ),
            }));
            return { messages };
          }),
        ),

      appendSubThinking: (slug, parentToolId, chunk) =>
        set((state) =>
          updateAnalysis(state, slug, (analysis) => {
            const messages = updateLastAssistant(analysis.messages, (msg) => ({
              ...msg,
              blocks: msg.blocks.map((b) =>
                b.type === "tool_call" && b.toolId === parentToolId
                  ? { ...b, subThinking: (b.subThinking ?? "") + chunk }
                  : b,
              ),
            }));
            return { messages };
          }),
        ),
    }),
    {
      name: "stdf-sessions",
      storage: mapStorage,
      partialize: (state) =>
        ({
          analyses: state.analyses,
          activeSlug: state.activeSlug,
          userId: state.userId,
        }) as unknown as AnalysisStore,
    },
  ),
);
