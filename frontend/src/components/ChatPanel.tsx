import { useState, useCallback, useRef, useEffect } from "react";
import { useAnalysisStore } from "../stores/useAnalysisStore";
import { useAutoScroll } from "../hooks/useAutoScroll";
import { ChatMessage } from "./ChatMessage";
import { MessageMetadata } from "./MessageMetadata";
import { ScrollButton } from "./ScrollButton";

interface Props {
  onAnswer: (slug: string, answers: Record<string, string>) => void;
  onPlanApproval: (slug: string, approved: boolean, feedback?: string) => void;
  onPromptSelect?: (text: string) => void;
}

export function ChatPanel({ onAnswer, onPlanApproval, onPromptSelect }: Props) {
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
  const { containerRef, handleScroll: autoScrollHandler } = useAutoScroll(scrollDep);

  // Track whether the user is at the bottom of the scroll container
  const [isAtBottom, setIsAtBottom] = useState(true);
  const sentinelRef = useRef<HTMLDivElement>(null);

  // Use IntersectionObserver to detect when sentinel at the bottom is visible
  useEffect(() => {
    const sentinel = sentinelRef.current;
    const container = containerRef.current;
    if (!sentinel || !container) return;

    const observer = new IntersectionObserver(
      ([entry]) => {
        setIsAtBottom(entry.isIntersecting);
      },
      {
        root: container,
        threshold: 0.1,
      },
    );

    observer.observe(sentinel);
    return () => observer.disconnect();
  }, [containerRef]);

  const handleScroll = useCallback(() => {
    autoScrollHandler();
  }, [autoScrollHandler]);

  const scrollToBottom = useCallback(() => {
    containerRef.current?.scrollTo({
      top: containerRef.current.scrollHeight,
      behavior: "smooth",
    });
  }, [containerRef]);

  const isStreaming = analysis?.status === "streaming";

  if (!analysis) {
    return (
      <div className="flex-1 flex items-center justify-center text-gray-400">
        Start a new analysis to begin
      </div>
    );
  }

  return (
    <div className="flex-1 flex flex-col overflow-hidden relative">
      <div
        ref={containerRef}
        onScroll={handleScroll}
        className="flex-1 overflow-y-auto p-4 space-y-4"
      >
        {analysis.messages.map((msg, idx) => (
          <div key={msg.id}>
            <ChatMessage
              message={msg}
              slug={analysis.slug}
              isStreaming={!!isStreaming}
              onAnswer={onAnswer}
              onPlanApproval={onPlanApproval}
              onPromptSelect={onPromptSelect}
            />
            {/* Show metadata after the last assistant message when complete */}
            {msg.role === "assistant" &&
              idx === analysis.messages.length - 1 &&
              analysis.status === "complete" && (
                <MessageMetadata
                  cost={analysis.cost}
                  duration={analysis.duration}
                  inputTokens={analysis.inputTokens}
                  outputTokens={analysis.outputTokens}
                />
              )}
          </div>
        ))}
        {analysis.error && (
          <div className="px-4 py-2 rounded-lg bg-red-50 text-red-700 text-sm">
            Error: {analysis.error}
          </div>
        )}
        {/* Typing indicator when streaming */}
        {isStreaming && analysis.messages.length > 0 && (
          <div className="flex items-center gap-2 px-2 py-1 text-xs text-gray-400">
            <span className="w-1.5 h-1.5 rounded-full bg-blue-400 animate-pulse" />
            <span>Working...</span>
          </div>
        )}
        {/* Sentinel element for IntersectionObserver */}
        <div ref={sentinelRef} className="h-1" />
      </div>
      {/* Scroll-to-bottom button */}
      {!isAtBottom && (
        <div className="relative">
          <ScrollButton onClick={scrollToBottom} />
        </div>
      )}
    </div>
  );
}
