import { useEffect, useRef, useCallback } from "react";
import { useAnalysisStore } from "../stores/useAnalysisStore";
import { WS_URL } from "../constants";
import type { AnalysisStatus } from "../types";

interface SyncSessionInfo {
  status: string;
  sessionId?: string;
  query?: string;
  pendingPrompt?: {
    type: string;
    questions?: { question: string; header: string; options: { label: string; description: string; preview?: string }[]; multiSelect: boolean }[];
    plan?: string;
    allowedPrompts?: { tool: string; prompt: string }[];
  };
}

export function useWebSocket() {
  const wsRef = useRef<WebSocket | null>(null);
  const userId = useAnalysisStore((s) => s.userId);

  useEffect(() => {
    let reconnectTimeout: ReturnType<typeof setTimeout>;
    let reconnectDelay = 2000;
    let intentionalClose = false;

    function connect() {
      const ws = new WebSocket(`${WS_URL}/${userId}`);
      wsRef.current = ws;

      ws.onopen = () => {
        useAnalysisStore.getState().setConnected(true);
        reconnectDelay = 2000;
      };

      ws.onmessage = (event: MessageEvent) => {
        const msg = JSON.parse(event.data);
        const store = useAnalysisStore.getState();
        const parentId = msg.parentToolId;

        switch (msg.type) {
          case "ack":
            store.addAnalysis(msg.slug, msg.query);
            break;
          case "text":
            // Skip subagent text — it's intermediate
            if (!parentId) store.appendChunk(msg.slug, msg.chunk);
            break;
          case "thinking":
            if (!parentId) store.appendThinking(msg.slug, msg.chunk);
            break;
          case "tool_start":
            if (parentId) {
              store.addSubToolCall(msg.slug, parentId, msg.toolId, msg.name);
            } else {
              store.startToolCall(msg.slug, msg.toolId, msg.name);
            }
            break;
          case "tool_input":
            if (parentId) {
              store.updateSubToolInput(
                msg.slug,
                parentId,
                msg.toolId,
                msg.json,
              );
            } else {
              store.appendToolInput(msg.slug, msg.toolId, msg.json);
            }
            break;
          case "tool_end":
            if (parentId) {
              store.endSubToolCall(msg.slug, parentId, msg.toolId);
            } else {
              store.endToolCall(msg.slug, msg.toolId);
            }
            break;
          case "ask_user":
            store.addAskUser(msg.slug, msg.questions);
            break;
          case "plan_approval":
            store.addPlanApproval(
              msg.slug,
              msg.plan || "",
              msg.allowedPrompts,
            );
            break;
          case "todo_update":
            store.setTodos(msg.slug, msg.todos);
            break;
          case "done":
            store.markComplete(msg.slug, msg.cost, msg.session_id);
            break;
          case "error":
            store.setError(msg.slug, msg.error);
            break;
          case "sync": {
            // Server sends active session statuses on reconnect
            const sessions = msg.sessions as Record<string, SyncSessionInfo>;
            for (const [slug, info] of Object.entries(sessions)) {
              store.syncSessionMeta(
                slug,
                info.sessionId ?? null,
                (info.status as AnalysisStatus) ?? "idle",
              );
              // Re-render pending interactive prompts
              if (info.pendingPrompt?.type === "ask_user" && info.pendingPrompt.questions) {
                store.addAskUser(slug, info.pendingPrompt.questions);
              }
              if (info.pendingPrompt?.type === "plan_approval") {
                store.addPlanApproval(
                  slug,
                  info.pendingPrompt.plan || "",
                  info.pendingPrompt.allowedPrompts || [],
                );
              }
            }
            break;
          }
        }
      };

      ws.onclose = () => {
        useAnalysisStore.getState().setConnected(false);
        if (!intentionalClose) {
          reconnectTimeout = setTimeout(() => {
            reconnectDelay = Math.min(reconnectDelay * 2, 30000);
            connect();
          }, reconnectDelay);
        }
      };

      ws.onerror = () => {
        ws.close();
      };
    }

    connect();

    return () => {
      intentionalClose = true;
      clearTimeout(reconnectTimeout);
      wsRef.current?.close();
    };
  }, [userId]);

  const sendNewAnalysis = useCallback((query: string) => {
    wsRef.current?.send(JSON.stringify({ query }));
  }, []);

  const sendMessage = useCallback(
    (slug: string, text: string, sessionId?: string | null) => {
      const msg: Record<string, unknown> = { slug, text };
      if (sessionId) msg.sessionId = sessionId;
      wsRef.current?.send(JSON.stringify(msg));
    },
    [],
  );

  const sendAnswer = useCallback(
    (slug: string, answers: Record<string, string>) => {
      useAnalysisStore.getState().markAnswered(slug);
      wsRef.current?.send(JSON.stringify({ type: "answer", slug, answers }));
    },
    [],
  );

  const sendPlanApproval = useCallback(
    (slug: string, approved: boolean, feedback?: string) => {
      useAnalysisStore.getState().markAnswered(slug);
      wsRef.current?.send(
        JSON.stringify({
          type: "answer",
          slug,
          answers: { approved, feedback },
        }),
      );
    },
    [],
  );

  return { sendNewAnalysis, sendMessage, sendAnswer, sendPlanApproval };
}
