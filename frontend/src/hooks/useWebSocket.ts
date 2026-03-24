import { useEffect, useRef, useCallback, useState } from "react";
import { useAnalysisStore } from "../stores/useAnalysisStore";
import { WS_URL } from "../constants";
import type { AnalysisStatus } from "../types";

export interface ContextUsage {
  used: number;
  total: number;
}

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

interface BufferEntry {
  texts: string[];
  thinkings: string[];
  subTexts: Record<string, string[]>;      // parentToolId -> chunks
  subThinkings: Record<string, string[]>;  // parentToolId -> chunks
}

export function useWebSocket() {
  const wsRef = useRef<WebSocket | null>(null);
  const userId = useAnalysisStore((s) => s.userId);
  const [contextUsage, setContextUsage] = useState<ContextUsage | null>(null);

  // Step 3.1: Stream flush buffer
  const bufferRef = useRef<Map<string, BufferEntry>>(new Map());
  const flushTimerRef = useRef<ReturnType<typeof setInterval> | null>(null);

  // Step 3.2: Offline message queue
  const queueRef = useRef<string[]>([]);

  const flushBuffer = useCallback(() => {
    const store = useAnalysisStore.getState();
    const buffer = bufferRef.current;
    for (const [slug, entry] of buffer) {
      if (entry.texts.length > 0) {
        const joined = entry.texts.join("");
        store.appendChunk(slug, joined);
        entry.texts = [];
      }
      if (entry.thinkings.length > 0) {
        const joined = entry.thinkings.join("");
        store.appendThinking(slug, joined);
        entry.thinkings = [];
      }
      for (const [parentId, chunks] of Object.entries(entry.subTexts)) {
        if (chunks.length > 0) {
          store.appendSubText(slug, parentId, chunks.join(""));
        }
      }
      entry.subTexts = {};
      for (const [parentId, chunks] of Object.entries(entry.subThinkings)) {
        if (chunks.length > 0) {
          store.appendSubThinking(slug, parentId, chunks.join(""));
        }
      }
      entry.subThinkings = {};
    }
  }, []);

  useEffect(() => {
    let reconnectTimeout: ReturnType<typeof setTimeout>;
    let reconnectDelay = 2000;
    let intentionalClose = false;

    // Start the 130ms flush interval
    flushTimerRef.current = setInterval(flushBuffer, 130);

    function connect() {
      const ws = new WebSocket(`${WS_URL}/${userId}`);
      wsRef.current = ws;

      ws.onopen = () => {
        useAnalysisStore.getState().setConnected(true);
        reconnectDelay = 2000;

        // Step 3.2: Flush queued messages on reconnect
        const pending = queueRef.current.splice(0);
        for (const msg of pending) {
          ws.send(msg);
        }
      };

      ws.onmessage = (event: MessageEvent) => {
        const msg = JSON.parse(event.data);
        const store = useAnalysisStore.getState();
        const parentId = msg.parentToolId;

        switch (msg.type) {
          case "ack":
            store.addAnalysis(msg.slug, msg.query);
            break;
          case "text": {
            const slug = msg.slug as string;
            let entry = bufferRef.current.get(slug);
            if (!entry) {
              entry = { texts: [], thinkings: [], subTexts: {}, subThinkings: {} };
              bufferRef.current.set(slug, entry);
            }
            if (parentId) {
              (entry.subTexts[parentId] ??= []).push(msg.chunk as string);
            } else {
              entry.texts.push(msg.chunk as string);
            }
            break;
          }
          case "thinking": {
            const slug = msg.slug as string;
            let entry = bufferRef.current.get(slug);
            if (!entry) {
              entry = { texts: [], thinkings: [], subTexts: {}, subThinkings: {} };
              bufferRef.current.set(slug, entry);
            }
            if (parentId) {
              (entry.subThinkings[parentId] ??= []).push(msg.chunk as string);
            } else {
              entry.thinkings.push(msg.chunk as string);
            }
            break;
          }
          case "tool_start":
            flushBuffer();
            if (parentId) {
              store.addSubToolCall(msg.slug, parentId, msg.toolId, msg.name);
            } else {
              store.startToolCall(msg.slug, msg.toolId, msg.name);
            }
            break;
          case "tool_input":
            flushBuffer();
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
          case "tool_result":
            flushBuffer();
            if (parentId) {
              store.setSubToolResult(
                msg.slug,
                parentId,
                msg.toolId,
                msg.result ?? "",
                Boolean(msg.truncated),
                Boolean(msg.isError),
              );
            } else {
              store.setToolResult(
                msg.slug,
                msg.toolId,
                msg.result ?? "",
                Boolean(msg.truncated),
                Boolean(msg.isError),
              );
            }
            break;
          case "tool_end":
            flushBuffer();
            if (parentId) {
              store.endSubToolCall(msg.slug, parentId, msg.toolId);
            } else {
              store.endToolCall(msg.slug, msg.toolId);
            }
            break;
          case "ask_user":
            flushBuffer();
            store.addAskUser(msg.slug, msg.questions);
            break;
          case "plan_approval":
            flushBuffer();
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
            flushBuffer();
            store.markComplete(msg.slug, msg.cost, msg.session_id, {
              duration: msg.duration_ms ?? undefined,
              inputTokens: msg.input_tokens ?? undefined,
              outputTokens: msg.output_tokens ?? undefined,
            });
            break;
          case "usage_update":
            setContextUsage({
              used: msg.contextUsed as number,
              total: msg.contextTotal as number,
            });
            break;
          case "error":
            flushBuffer();
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
      if (flushTimerRef.current) {
        clearInterval(flushTimerRef.current);
        flushTimerRef.current = null;
      }
      flushBuffer();
      wsRef.current?.close();
    };
  }, [userId, flushBuffer]);

  // Helper: send or queue a message
  const safeSend = useCallback((payload: string) => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(payload);
    } else {
      queueRef.current.push(payload);
    }
  }, []);

  const sendNewAnalysis = useCallback((query: string) => {
    safeSend(JSON.stringify({ query }));
  }, [safeSend]);

  const sendMessage = useCallback(
    (slug: string, text: string, sessionId?: string | null) => {
      const msg: Record<string, unknown> = { slug, text };
      if (sessionId) msg.sessionId = sessionId;
      safeSend(JSON.stringify(msg));
    },
    [safeSend],
  );

  const sendAnswer = useCallback(
    (slug: string, answers: Record<string, string>) => {
      useAnalysisStore.getState().markAnswered(slug);
      safeSend(JSON.stringify({ type: "answer", slug, answers }));
    },
    [safeSend],
  );

  const sendPlanApproval = useCallback(
    (slug: string, approved: boolean, feedback?: string) => {
      useAnalysisStore.getState().markAnswered(slug);
      safeSend(
        JSON.stringify({
          type: "answer",
          slug,
          answers: { approved, feedback },
        }),
      );
    },
    [safeSend],
  );

  const sendControl = useCallback(
    (msg: Record<string, unknown>) => {
      safeSend(JSON.stringify(msg));
    },
    [safeSend],
  );

  return { sendNewAnalysis, sendMessage, sendAnswer, sendPlanApproval, sendControl, contextUsage };
}
