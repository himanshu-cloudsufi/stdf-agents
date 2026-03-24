import { memo, useMemo, useState } from "react";
import { Bot, Brain, ChevronDown, ChevronRight } from "lucide-react";
import { Streamdown } from "streamdown";
import { code } from "@streamdown/code";
import type { ToolComponentProps } from "./ToolCard";
import type { SubEvent } from "../../types";
import { ToolCard } from "./ToolCard";
import { safeParseJson } from "../../utils/safeParseJson";
import { getToolMetadata } from "../../utils/toolMetadata";

const plugins = { code };

interface AgentInput {
  description?: string;
  prompt?: string;
  subagent_type?: string;
}

function subEventLabel(se: SubEvent): string {
  try {
    const parsed = JSON.parse(se.input) as Record<string, unknown>;
    switch (se.name) {
      case "Read":
        return (parsed.file_path as string)?.split("/").slice(-2).join("/") ?? "Reading...";
      case "Write":
        return `Writing ${(parsed.file_path as string)?.split("/").slice(-2).join("/") ?? "file"}`;
      case "Edit":
        return `Editing ${(parsed.file_path as string)?.split("/").slice(-2).join("/") ?? "file"}`;
      case "Bash":
        return ((parsed.command as string) ?? "").slice(0, 60) || "Running command...";
      case "Grep":
        return `Search: ${(parsed.pattern as string) ?? ""}`;
      case "Glob":
        return `Pattern: ${(parsed.pattern as string) ?? ""}`;
      case "WebSearch":
        return (parsed.query as string) ?? "Searching...";
      case "WebFetch":
        return ((parsed.url as string) ?? "").slice(0, 60) || "Fetching...";
      case "Agent":
        return (parsed.description as string) ?? "Launching agent...";
      default:
        return se.name;
    }
  } catch {
    return se.name;
  }
}

const AgentToolInner: React.FC<ToolComponentProps> = ({ block }) => {
  const [promptExpanded, setPromptExpanded] = useState(false);
  const [thinkingExpanded, setThinkingExpanded] = useState(false);

  const input = useMemo(
    () => safeParseJson<AgentInput>(block.input, {}),
    [block.input],
  );

  const subagentType = input.subagent_type ?? "general";
  const description = input.description;
  const prompt = input.prompt;
  const subEvents = block.subEvents ?? [];
  const subDone = subEvents.filter((s) => s.status === "done").length;
  const subText = block.subText ?? "";
  const subThinking = block.subThinking ?? "";
  const isRunning = block.status === "running";

  const hasDetails = Boolean(prompt) || subEvents.length > 0 || Boolean(subText) || Boolean(subThinking);

  return (
    <ToolCard
      icon={<Bot className="h-3.5 w-3.5" />}
      status={block.status}
      title={(status) => {
        const label = description ?? `Agent (${subagentType})`;
        switch (status) {
          case "done":
            return `Completed: ${label}`;
          case "running":
            return `Running: ${label}`;
          default:
            return label;
        }
      }}
      expandable={hasDetails}
      statusDetail={
        subEvents.length > 0 ? (
          <span className="text-[10px] text-gray-400 tabular-nums">
            {subDone}/{subEvents.length} tools
          </span>
        ) : undefined
      }
    >
      {hasDetails && (
        <div className="space-y-2">
          {/* Sub-agent thinking */}
          {subThinking && (
            <div>
              <button
                type="button"
                onClick={() => setThinkingExpanded((prev) => !prev)}
                className="flex items-center gap-1 text-[11px] text-gray-500 hover:text-gray-700"
              >
                {thinkingExpanded ? (
                  <ChevronDown className="h-3 w-3" />
                ) : (
                  <ChevronRight className="h-3 w-3" />
                )}
                <Brain className="h-3 w-3" />
                <span>Thinking</span>
                {isRunning && !thinkingExpanded && (
                  <span className="flex gap-0.5 ml-1">
                    <span className="w-1 h-1 rounded-full bg-gray-400 animate-bounce [animation-delay:0ms]" />
                    <span className="w-1 h-1 rounded-full bg-gray-400 animate-bounce [animation-delay:150ms]" />
                    <span className="w-1 h-1 rounded-full bg-gray-400 animate-bounce [animation-delay:300ms]" />
                  </span>
                )}
              </button>
              {thinkingExpanded && (
                <div className="mt-1 whitespace-pre-wrap break-words rounded bg-gray-50 p-2 text-[11px] text-gray-500 max-h-64 overflow-y-auto">
                  {subThinking}
                </div>
              )}
            </div>
          )}

          {/* Sub-events list */}
          {subEvents.length > 0 && (
            <div className="space-y-1">
              {subEvents.map((se) => {
                const meta = getToolMetadata(se.name);
                return (
                  <div
                    key={se.toolId}
                    className="flex items-center gap-1.5 text-[11px]"
                  >
                    {se.status === "running" ? (
                      <span className="w-2 h-2 border border-blue-400 border-t-transparent rounded-full animate-spin shrink-0" />
                    ) : (
                      <span className="text-green-500 shrink-0 text-[10px]">
                        {"\u2713"}
                      </span>
                    )}
                    <span className="text-gray-500 font-medium shrink-0">
                      {meta.icon} {se.name}
                    </span>
                    <span className="text-gray-400 truncate">
                      {subEventLabel(se)}
                    </span>
                  </div>
                );
              })}
            </div>
          )}

          {/* Sub-agent text output */}
          {subText && (
            <div className="border-t border-gray-100 pt-2">
              <div className="text-[11px] text-gray-400 mb-1">Agent output</div>
              <div className="text-xs prose prose-sm max-w-none prose-p:my-1 prose-headings:my-1">
                <Streamdown plugins={plugins} isAnimating={isRunning}>
                  {subText}
                </Streamdown>
              </div>
            </div>
          )}

          {/* Prompt section */}
          {prompt && (
            <div>
              <button
                type="button"
                onClick={() => setPromptExpanded((prev) => !prev)}
                className="flex items-center gap-1 text-[11px] text-gray-500 hover:text-gray-700"
              >
                {promptExpanded ? (
                  <ChevronDown className="h-3 w-3" />
                ) : (
                  <ChevronRight className="h-3 w-3" />
                )}
                Prompt
              </button>
              {promptExpanded && (
                <div className="mt-1 whitespace-pre-wrap break-words rounded bg-gray-50 p-2 font-mono text-[11px] text-gray-500 max-h-48 overflow-y-auto">
                  {prompt}
                </div>
              )}
            </div>
          )}
        </div>
      )}
    </ToolCard>
  );
};

export const AgentTool = memo(AgentToolInner);
