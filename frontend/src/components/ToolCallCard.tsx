import { useState, useMemo } from "react";
import type { ToolCallBlock, SubEvent } from "../types";

interface Props {
  block: ToolCallBlock;
}

function parseToolInput(name: string, raw: string): string {
  try {
    const parsed = JSON.parse(raw);
    switch (name) {
      case "Skill":
        return `Running /${parsed.skill}${parsed.args ? ` "${parsed.args}"` : ""}`;
      case "Agent":
        return parsed.description || parsed.prompt?.slice(0, 80) || "Launching agent...";
      case "Read":
        return parsed.file_path?.split("/").slice(-2).join("/") || "Reading file...";
      case "Write":
        return `Writing ${parsed.file_path?.split("/").slice(-2).join("/") || "file"}`;
      case "Edit":
        return `Editing ${parsed.file_path?.split("/").slice(-2).join("/") || "file"}`;
      case "Bash":
        return parsed.command?.slice(0, 120) || "Running command...";
      case "Glob":
        return `Pattern: ${parsed.pattern || ""}`;
      case "Grep":
        return `Pattern: ${parsed.pattern || ""}`;
      case "WebSearch":
        return `"${parsed.query || ""}"`;
      case "WebFetch":
        return parsed.url || "Fetching...";
      case "AskUserQuestion":
        return parsed.questions?.[0]?.question || "Asking a question...";
      case "ToolSearch":
        return `Looking up: ${parsed.query || ""}`;
      case "EnterPlanMode":
        return "Entering plan mode...";
      case "ExitPlanMode":
        return "Submitting plan for approval";
      case "TaskCreate":
        return parsed.subject || "Creating task...";
      case "TaskUpdate":
        return `Updating task #${parsed.taskId || ""}${parsed.status ? ` → ${parsed.status}` : ""}`;
      case "TaskList":
        return "Listing tasks";
      case "TaskGet":
        return `Getting task #${parsed.taskId || ""}`;
      case "TaskOutput":
        return `Reading output of task ${parsed.task_id || ""}`;
      case "NotebookEdit":
        return parsed.file_path?.split("/").slice(-2).join("/") || "Editing notebook";
      default:
        return formatFallback(raw);
    }
  } catch {
    // Input is still accumulating (partial JSON) - show what we can
    return formatFallback(raw);
  }
}

function formatFallback(raw: string): string {
  if (!raw || raw.length < 3) return "...";
  // Try to extract something readable from partial JSON
  const skillMatch = raw.match(/"skill"\s*:\s*"([^"]+)"/);
  if (skillMatch) return `Running /${skillMatch[1]}`;
  const pathMatch = raw.match(/"file_path"\s*:\s*"([^"]+)"/);
  if (pathMatch) return pathMatch[1].split("/").slice(-2).join("/");
  const cmdMatch = raw.match(/"command"\s*:\s*"([^"]{1,80})/);
  if (cmdMatch) return cmdMatch[1];
  return "...";
}

const toolIcons: Record<string, string> = {
  Skill: "⚡",
  Agent: "🤖",
  Read: "📄",
  Write: "✏️",
  Edit: "✏️",
  Bash: "💻",
  Glob: "🔍",
  Grep: "🔍",
  WebSearch: "🌐",
  WebFetch: "🌐",
  AskUserQuestion: "❓",
  ToolSearch: "🔧",
  EnterPlanMode: "📋",
  ExitPlanMode: "✅",
  TaskCreate: "📝",
  TaskUpdate: "📝",
  TaskList: "📝",
  TaskGet: "📝",
  TaskOutput: "📝",
  SendMessage: "💬",
  NotebookEdit: "📓",
};

function subEventDescription(se: SubEvent): string {
  try {
    const parsed = JSON.parse(se.input);
    switch (se.name) {
      case "Read": return parsed.file_path?.split("/").slice(-2).join("/") || "Reading...";
      case "Write": return `Writing ${parsed.file_path?.split("/").slice(-2).join("/") || "file"}`;
      case "Edit": return `Editing ${parsed.file_path?.split("/").slice(-2).join("/") || "file"}`;
      case "Bash": return parsed.command?.slice(0, 80) || "Running command...";
      case "Glob": return `Pattern: ${parsed.pattern || ""}`;
      case "Grep": return `Searching: ${parsed.pattern || ""}`;
      case "WebSearch": return `"${parsed.query || ""}"`;
      case "WebFetch": return parsed.url?.slice(0, 60) || "Fetching...";
      case "Agent": return parsed.description || "Launching agent...";
      default: return se.name;
    }
  } catch {
    return se.name;
  }
}

export function ToolCallCard({ block }: Props) {
  const [expanded, setExpanded] = useState(false);
  const icon = toolIcons[block.name] || "⚙️";
  const description = useMemo(
    () => parseToolInput(block.name, block.input),
    [block.name, block.input],
  );
  const isAgent = block.name === "Agent";
  const subEvents = block.subEvents || [];
  const subDone = subEvents.filter((s) => s.status === "done").length;

  return (
    <div className="border border-gray-200 rounded-lg overflow-hidden my-2">
      <div
        className="flex items-center gap-2 px-3 py-2 bg-gray-50 cursor-pointer select-none"
        onClick={() => setExpanded(!expanded)}
      >
        <span className="text-sm">{icon}</span>
        <span className="text-sm font-medium text-gray-700">{block.name}</span>
        <span className="flex-1 text-xs text-gray-500 truncate">{description}</span>
        {isAgent && subEvents.length > 0 && (
          <span className="text-[10px] text-gray-400 tabular-nums shrink-0">
            {subDone}/{subEvents.length}
          </span>
        )}
        {block.status === "running" ? (
          <span className="w-3 h-3 border-2 border-blue-500 border-t-transparent rounded-full animate-spin shrink-0" />
        ) : (
          <span className="text-green-500 text-sm shrink-0">✓</span>
        )}
      </div>

      {/* Subagent progress — always visible for Agent cards when running */}
      {isAgent && subEvents.length > 0 && (
        <div className="px-3 py-1.5 border-t border-gray-100 bg-white space-y-1 max-h-48 overflow-y-auto">
          {subEvents.map((se) => (
            <div key={se.toolId} className="flex items-center gap-1.5 text-[11px]">
              {se.status === "running" ? (
                <span className="w-2 h-2 border border-blue-400 border-t-transparent rounded-full animate-spin shrink-0" />
              ) : (
                <span className="text-emerald-500 shrink-0 text-[10px]">✓</span>
              )}
              <span className="text-gray-500 font-medium shrink-0">
                {toolIcons[se.name] || "⚙️"} {se.name}
              </span>
              <span className="text-gray-400 truncate">
                {subEventDescription(se)}
              </span>
            </div>
          ))}
        </div>
      )}

      {expanded && block.input && (
        <div className="px-3 py-2 text-xs text-gray-500 font-mono whitespace-pre-wrap max-h-48 overflow-y-auto border-t border-gray-100 bg-white">
          {tryPrettyPrint(block.input)}
        </div>
      )}
    </div>
  );
}

function tryPrettyPrint(raw: string): string {
  try {
    return JSON.stringify(JSON.parse(raw), null, 2);
  } catch {
    return raw;
  }
}
