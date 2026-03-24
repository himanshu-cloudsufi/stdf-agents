import { useAnalysisStore } from "../stores/useAnalysisStore";
import { useAutoScroll } from "../hooks/useAutoScroll";
import { ChatMessage } from "./ChatMessage";

interface Props {
  onAnswer: (slug: string, answers: Record<string, string>) => void;
  onPlanApproval: (slug: string, approved: boolean, feedback?: string) => void;
}

export function ChatPanel({ onAnswer, onPlanApproval }: Props) {
  const analyses = useAnalysisStore((s) => s.analyses);
  const activeSlug = useAnalysisStore((s) => s.activeSlug);
  const analysis = activeSlug ? analyses.get(activeSlug) : null;

  const lastMsg = analysis?.messages[analysis.messages.length - 1];
  const scrollDep = lastMsg
    ? lastMsg.role === "assistant"
      ? lastMsg.blocks.reduce(
          (acc, b) =>
            acc + (b.type === "text" ? b.content.length : b.type === "tool_call" ? 1 : 0),
          0,
        )
      : lastMsg.content.length
    : 0;
  const { containerRef, handleScroll } = useAutoScroll(scrollDep);

  if (!analysis) {
    return (
      <div className="flex-1 flex items-center justify-center text-gray-400">
        Start a new analysis to begin
      </div>
    );
  }

  return (
    <div
      ref={containerRef}
      onScroll={handleScroll}
      className="flex-1 overflow-y-auto p-4 space-y-4"
    >
      {analysis.messages.map((msg) => (
        <ChatMessage
          key={msg.id}
          message={msg}
          slug={analysis.slug}
          onAnswer={onAnswer}
          onPlanApproval={onPlanApproval}
        />
      ))}
      {analysis.error && (
        <div className="px-4 py-2 rounded-lg bg-red-50 text-red-700 text-sm">
          Error: {analysis.error}
        </div>
      )}
    </div>
  );
}
