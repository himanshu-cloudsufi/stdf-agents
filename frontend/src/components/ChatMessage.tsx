import { useMemo } from "react";
import { Streamdown } from "streamdown";
import { code } from "@streamdown/code";
import "streamdown/styles.css";
import type {
  ChatMessage as ChatMessageType,
  AssistantMessage,
  ToolCallBlock as ToolCallBlockType,
  SubEvent,
} from "../types";
import { ThinkingBlock } from "./ThinkingBlock";
import { AskUserQuestionCard } from "./AskUserQuestionCard";
import { PlanApprovalCard } from "./PlanApprovalCard";
import { PromptSuggestions } from "./PromptSuggestions";
import { MessageActions } from "./MessageActions";
import { ToolCard } from "./tools/ToolCard";
import type { ToolCardStatus } from "./tools/ToolCard";
import { getToolMetadata, toolIcons } from "../utils/toolMetadata";

const plugins = { code };

// Regex for extracting prompt suggestions from content
const PROMPT_SUGGESTIONS_RE = /<prompt_suggestions>([\s\S]*?)<\/prompt_suggestions>/;
const SUGGESTION_RE = /<suggestion>(.*?)<\/suggestion>/g;

function extractPromptSuggestions(content: string): {
  cleanContent: string;
  suggestions: string[];
} {
  const match = content.match(PROMPT_SUGGESTIONS_RE);
  if (!match) return { cleanContent: content, suggestions: [] };

  const cleanContent = content.replace(PROMPT_SUGGESTIONS_RE, "").trim();
  const suggestions: string[] = [];
  let m: RegExpExecArray | null;
  const inner = match[1];
  SUGGESTION_RE.lastIndex = 0;
  while ((m = SUGGESTION_RE.exec(inner)) !== null) {
    suggestions.push(m[1]);
  }
  return { cleanContent, suggestions };
}

// ---------------------------------------------------------------------------
// Tool input parsing (kept from original ToolCallCard)
// ---------------------------------------------------------------------------

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
        return `Updating task #${parsed.taskId || ""}${parsed.status ? ` \u2192 ${parsed.status}` : ""}`;
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
    return formatFallback(raw);
  }
}

function formatFallback(raw: string): string {
  if (!raw || raw.length < 3) return "...";
  const skillMatch = raw.match(/"skill"\s*:\s*"([^"]+)"/);
  if (skillMatch) return `Running /${skillMatch[1]}`;
  const pathMatch = raw.match(/"file_path"\s*:\s*"([^"]+)"/);
  if (pathMatch) return pathMatch[1].split("/").slice(-2).join("/");
  const cmdMatch = raw.match(/"command"\s*:\s*"([^"]{1,80})/);
  if (cmdMatch) return cmdMatch[1];
  return "...";
}

function subEventDescription(se: SubEvent): string {
  try {
    const parsed = JSON.parse(se.input);
    switch (se.name) {
      case "Read":
        return parsed.file_path?.split("/").slice(-2).join("/") || "Reading...";
      case "Write":
        return `Writing ${parsed.file_path?.split("/").slice(-2).join("/") || "file"}`;
      case "Edit":
        return `Editing ${parsed.file_path?.split("/").slice(-2).join("/") || "file"}`;
      case "Bash":
        return parsed.command?.slice(0, 80) || "Running command...";
      case "Glob":
        return `Pattern: ${parsed.pattern || ""}`;
      case "Grep":
        return `Searching: ${parsed.pattern || ""}`;
      case "WebSearch":
        return `"${parsed.query || ""}"`;
      case "WebFetch":
        return parsed.url?.slice(0, 60) || "Fetching...";
      case "Agent":
        return parsed.description || "Launching agent...";
      default:
        return se.name;
    }
  } catch {
    return se.name;
  }
}

function tryPrettyPrint(raw: string): string {
  try {
    return JSON.stringify(JSON.parse(raw), null, 2);
  } catch {
    return raw;
  }
}

// ---------------------------------------------------------------------------
// ToolCallCard using the new universal ToolCard
// ---------------------------------------------------------------------------

function ToolCallCardWrapper({ block }: { block: ToolCallBlockType }) {
  const meta = getToolMetadata(block.name);
  const description = useMemo(
    () => parseToolInput(block.name, block.input),
    [block.name, block.input],
  );

  const status: ToolCardStatus = block.status === "done" ? "done" : "running";
  const isAgent = block.name === "Agent";
  const subEvents = block.subEvents || [];
  const subDone = subEvents.filter((s) => s.status === "done").length;

  return (
    <ToolCard
      icon={<span className="text-sm">{meta.icon}</span>}
      status={status}
      title={`${block.name} \u2014 ${description}`}
      expandable
      defaultExpanded={false}
      loadingContent={
        isAgent && subEvents.length > 0
          ? `${subDone}/${subEvents.length} sub-tasks done`
          : undefined
      }
    >
      {/* Sub-events for Agent cards */}
      {isAgent && subEvents.length > 0 && (
        <div className="space-y-1 max-h-48 overflow-y-auto">
          {subEvents.map((se) => (
            <div key={se.toolId} className="flex items-center gap-1.5 text-[11px]">
              {se.status === "running" ? (
                <span className="w-2 h-2 border border-blue-400 border-t-transparent rounded-full animate-spin shrink-0" />
              ) : (
                <span className="text-emerald-500 shrink-0 text-[10px]">{"\u2713"}</span>
              )}
              <span className="text-gray-500 font-medium shrink-0">
                {toolIcons[se.name] || "\u2699\uFE0F"} {se.name}
              </span>
              <span className="text-gray-400 truncate">
                {subEventDescription(se)}
              </span>
            </div>
          ))}
        </div>
      )}

      {/* Raw JSON input */}
      {block.input && (
        <div className="text-xs text-gray-500 font-mono whitespace-pre-wrap max-h-48 overflow-y-auto mt-1">
          {tryPrettyPrint(block.input)}
        </div>
      )}
    </ToolCard>
  );
}

// ---------------------------------------------------------------------------
// AssistantBlocks — now accepts isStreaming to pass to ThinkingBlock
// ---------------------------------------------------------------------------

function AssistantBlocks({
  message,
  slug,
  onAnswer,
  onPlanApproval,
  onPromptSelect,
  isStreaming,
}: {
  message: AssistantMessage;
  slug: string;
  onAnswer: (slug: string, answers: Record<string, string>) => void;
  onPlanApproval: (slug: string, approved: boolean, feedback?: string) => void;
  onPromptSelect?: (text: string) => void;
  isStreaming: boolean;
}) {
  // Collect all text block contents for MessageActions copy
  const allTextContent = useMemo(() => {
    return message.blocks
      .filter((b) => b.type === "text")
      .map((b) => (b as { content: string }).content)
      .join("\n");
  }, [message.blocks]);

  // Determine if the message is fully complete (not streaming)
  const isComplete = !isStreaming || message.blocks.every(
    (b) => b.type !== "text" || !b.isStreaming,
  );

  return (
    <div className="flex justify-start">
      <div className="group relative max-w-[90%] px-4 py-2 rounded-lg bg-gray-100 text-gray-900 text-sm">
        {/* Copy action on hover — only for completed messages with text content */}
        {isComplete && allTextContent.length > 0 && (
          <MessageActions content={allTextContent} />
        )}
        {message.blocks.map((block, i) => {
          const isLastBlock = i === message.blocks.length - 1;

          switch (block.type) {
            case "thinking":
              return (
                <ThinkingBlock
                  key={i}
                  content={block.content}
                  isActiveThinking={isLastBlock && isStreaming}
                />
              );
            case "tool_call":
              return <ToolCallCardWrapper key={block.toolId} block={block} />;
            case "ask_user":
              return (
                <AskUserQuestionCard
                  key={i}
                  questions={block.questions}
                  answered={block.answered}
                  onAnswer={(answers) => onAnswer(slug, answers)}
                />
              );
            case "plan_approval":
              return (
                <PlanApprovalCard
                  key={i}
                  plan={block.plan}
                  allowedPrompts={block.allowedPrompts}
                  answered={block.answered}
                  onApprove={() => onPlanApproval(slug, true)}
                  onReject={(fb) => onPlanApproval(slug, false, fb)}
                />
              );
            case "text": {
              const { cleanContent, suggestions } = extractPromptSuggestions(
                block.content,
              );
              return (
                <div key={i}>
                  <Streamdown
                    plugins={plugins}
                    isAnimating={block.isStreaming}
                  >
                    {cleanContent}
                  </Streamdown>
                  {suggestions.length > 0 && onPromptSelect && (
                    <PromptSuggestions
                      suggestions={suggestions}
                      onSelect={onPromptSelect}
                    />
                  )}
                </div>
              );
            }
            default:
              return null;
          }
        })}
        {message.blocks.length === 0 && (
          <span className="flex gap-1 py-1">
            <span className="w-1.5 h-1.5 rounded-full bg-gray-400 animate-bounce [animation-delay:0ms]" />
            <span className="w-1.5 h-1.5 rounded-full bg-gray-400 animate-bounce [animation-delay:150ms]" />
            <span className="w-1.5 h-1.5 rounded-full bg-gray-400 animate-bounce [animation-delay:300ms]" />
          </span>
        )}
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// ChatMessage — top-level
// ---------------------------------------------------------------------------

interface Props {
  message: ChatMessageType;
  slug: string;
  isStreaming: boolean;
  onAnswer: (slug: string, answers: Record<string, string>) => void;
  onPlanApproval: (slug: string, approved: boolean, feedback?: string) => void;
  onPromptSelect?: (text: string) => void;
}

export function ChatMessage({
  message,
  slug,
  isStreaming,
  onAnswer,
  onPlanApproval,
  onPromptSelect,
}: Props) {
  if (message.role === "user") {
    return (
      <div className="flex justify-end">
        <div className="max-w-[80%] px-4 py-2 rounded-lg bg-blue-600 text-white text-sm">
          {message.content}
        </div>
      </div>
    );
  }

  return (
    <AssistantBlocks
      message={message}
      slug={slug}
      isStreaming={isStreaming}
      onAnswer={onAnswer}
      onPlanApproval={onPlanApproval}
      onPromptSelect={onPromptSelect}
    />
  );
}
