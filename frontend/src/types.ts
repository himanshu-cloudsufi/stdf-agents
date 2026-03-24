// Content blocks within an assistant message
export interface TextBlock {
  type: "text";
  content: string;
  isStreaming: boolean;
}

export interface ThinkingBlock {
  type: "thinking";
  content: string;
  isExpanded: boolean;
}

export interface SubEvent {
  toolId: string;
  name: string;
  input: string;
  status: "running" | "done";
}

export interface ToolCallBlock {
  type: "tool_call";
  toolId: string;
  name: string;
  input: string;
  status: "running" | "done";
  subEvents: SubEvent[];
  subText?: string;
  subThinking?: string;
}

export interface TodoItem {
  content: string;
  status: "pending" | "in_progress" | "completed";
  activeForm?: string;
}

export interface QuestionOption {
  label: string;
  description: string;
  preview?: string;
}

export interface Question {
  question: string;
  header: string;
  options: QuestionOption[];
  multiSelect: boolean;
}

export interface AskUserBlock {
  type: "ask_user";
  questions: Question[];
  answered: boolean;
}

export interface AllowedPrompt {
  tool: string;
  prompt: string;
}

export interface PlanApprovalBlock {
  type: "plan_approval";
  plan: string;
  allowedPrompts: AllowedPrompt[];
  answered: boolean;
}

export type ContentBlock = TextBlock | ThinkingBlock | ToolCallBlock | AskUserBlock | PlanApprovalBlock;

export interface UserMessage {
  id: string;
  role: "user";
  content: string;
  timestamp: number;
}

export interface AssistantMessage {
  id: string;
  role: "assistant";
  blocks: ContentBlock[];
  timestamp: number;
}

export type ChatMessage = UserMessage | AssistantMessage;

export type AnalysisStatus = "idle" | "streaming" | "complete" | "error";

export interface Analysis {
  slug: string;
  label: string;
  messages: ChatMessage[];
  status: AnalysisStatus;
  cost: number | null;
  sessionId: string | null;
  error: string | null;
  todos: TodoItem[];
  createdAt: number;
  duration?: number;
  inputTokens?: number;
  outputTokens?: number;
}
