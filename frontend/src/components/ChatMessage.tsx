import { Streamdown } from "streamdown";
import { code } from "@streamdown/code";
import "streamdown/styles.css";
import type { ChatMessage as ChatMessageType, AssistantMessage } from "../types";
import { ThinkingBlock } from "./ThinkingBlock";
import { ToolCallCard } from "./ToolCallCard";
import { AskUserQuestionCard } from "./AskUserQuestionCard";
import { PlanApprovalCard } from "./PlanApprovalCard";

const plugins = { code };

interface Props {
  message: ChatMessageType;
  slug: string;
  onAnswer: (slug: string, answers: Record<string, string>) => void;
  onPlanApproval: (slug: string, approved: boolean, feedback?: string) => void;
}

function AssistantBlocks({
  message,
  slug,
  onAnswer,
  onPlanApproval,
}: {
  message: AssistantMessage;
  slug: string;
  onAnswer: (slug: string, answers: Record<string, string>) => void;
  onPlanApproval: (slug: string, approved: boolean, feedback?: string) => void;
}) {
  return (
    <div className="flex justify-start">
      <div className="max-w-[90%] px-4 py-2 rounded-lg bg-gray-100 text-gray-900 text-sm">
        {message.blocks.map((block, i) => {
          switch (block.type) {
            case "thinking":
              return <ThinkingBlock key={i} block={block} />;
            case "tool_call":
              return <ToolCallCard key={block.toolId} block={block} />;
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
            case "text":
              return (
                <div key={i}>
                  <Streamdown
                    plugins={plugins}
                    isAnimating={block.isStreaming}
                  >
                    {block.content}
                  </Streamdown>
                </div>
              );
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

export function ChatMessage({ message, slug, onAnswer, onPlanApproval }: Props) {
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
      onAnswer={onAnswer}
      onPlanApproval={onPlanApproval}
    />
  );
}
