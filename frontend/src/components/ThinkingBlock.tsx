import { useState } from "react";
import type { ThinkingBlock as ThinkingBlockType } from "../types";

interface Props {
  block: ThinkingBlockType;
}

export function ThinkingBlock({ block }: Props) {
  const [expanded, setExpanded] = useState(false);

  return (
    <div
      className="border border-gray-200 rounded-lg overflow-hidden my-2"
      onClick={() => setExpanded(!expanded)}
    >
      <div className="flex items-center gap-2 px-3 py-2 bg-gray-50 cursor-pointer select-none">
        <span className="text-sm">{expanded ? "▼" : "▶"}</span>
        <span className="text-gray-500 text-sm font-medium">
          {block.content.length === 0 ? (
            <span className="animate-pulse">Thinking...</span>
          ) : (
            `Thinking (${block.content.length} chars)`
          )}
        </span>
        {block.content.length === 0 && (
          <span className="flex gap-0.5 ml-1">
            <span className="w-1 h-1 rounded-full bg-gray-400 animate-bounce [animation-delay:0ms]" />
            <span className="w-1 h-1 rounded-full bg-gray-400 animate-bounce [animation-delay:150ms]" />
            <span className="w-1 h-1 rounded-full bg-gray-400 animate-bounce [animation-delay:300ms]" />
          </span>
        )}
      </div>
      {expanded && block.content && (
        <div className="px-3 py-2 text-xs text-gray-400 font-mono whitespace-pre-wrap max-h-48 overflow-y-auto border-t border-gray-100">
          {block.content}
        </div>
      )}
    </div>
  );
}
