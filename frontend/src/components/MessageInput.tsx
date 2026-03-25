import { useState, type KeyboardEvent } from "react";
import { ThinkingModeSelector } from "./ThinkingModeSelector.tsx";
import { PermissionModeSelector } from "./PermissionModeSelector.tsx";
import { ContextUsageIndicator } from "./ContextUsageIndicator.tsx";
import type { ContextUsage } from "../hooks/useWebSocket.ts";

interface Props {
  onSend: (text: string) => void;
  disabled: boolean;
  placeholder?: string;
  sendControl: (msg: Record<string, unknown>) => void;
  contextUsage: ContextUsage | null;
}

export function MessageInput({ onSend, disabled, placeholder, sendControl, contextUsage }: Props) {
  const [text, setText] = useState("");

  function handleSubmit() {
    const trimmed = text.trim();
    if (!trimmed || disabled) return;
    onSend(trimmed);
    setText("");
  }

  function handleKeyDown(e: KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  }

  return (
    <div className="border-t border-gray-200 p-4 bg-white">
      <div className="flex gap-2">
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder={placeholder ?? "Type a message..."}
          disabled={disabled}
          rows={1}
          className="flex-1 resize-none rounded-lg border border-gray-300 px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent disabled:bg-gray-50 disabled:text-gray-400"
        />
        <button
          onClick={handleSubmit}
          disabled={disabled || !text.trim()}
          className="px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-lg hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors cursor-pointer"
        >
          Send
        </button>
      </div>
      {/* Controls row */}
      <div className="flex items-center justify-between mt-2">
        <div className="flex items-center gap-1">
          <ThinkingModeSelector sendControl={sendControl} />
          <PermissionModeSelector sendControl={sendControl} />
        </div>
        <div className="flex items-center">
          {contextUsage && contextUsage.total > 0 && (
            <ContextUsageIndicator used={contextUsage.used} total={contextUsage.total} />
          )}
        </div>
      </div>
    </div>
  );
}
