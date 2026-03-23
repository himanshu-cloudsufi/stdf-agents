import { useCallback } from "react";
import { Header } from "./components/Header";
import { AnalysisTabs } from "./components/AnalysisTabs";
import { ChatPanel } from "./components/ChatPanel";
import { MessageInput } from "./components/MessageInput";
import { CostBadge } from "./components/CostBadge";
import { TodoPanel } from "./components/TodoPanel";
import { useWebSocket } from "./hooks/useWebSocket";
import { useAnalysisStore } from "./stores/useAnalysisStore";

export default function App() {
  const { sendNewAnalysis, sendMessage, sendAnswer, sendPlanApproval } =
    useWebSocket();
  const activeSlug = useAnalysisStore((s) => s.activeSlug);
  const analyses = useAnalysisStore((s) => s.analyses);
  const addUserMessage = useAnalysisStore((s) => s.addUserMessage);
  const isConnected = useAnalysisStore((s) => s.isConnected);

  const handleSend = useCallback(
    (text: string) => {
      if (!activeSlug) {
        sendNewAnalysis(text);
      } else {
        const analysis = analyses.get(activeSlug);
        addUserMessage(activeSlug, text);
        sendMessage(activeSlug, text, analysis?.sessionId);
      }
    },
    [activeSlug, analyses, sendNewAnalysis, sendMessage, addUserMessage],
  );

  return (
    <div className="h-screen flex flex-col bg-white">
      <Header />
      <div className="flex flex-1 overflow-hidden">
        <AnalysisTabs />
        <main className="flex-1 flex flex-col min-w-0">
          <ChatPanel onAnswer={sendAnswer} onPlanApproval={sendPlanApproval} />
          <MessageInput
            onSend={handleSend}
            disabled={!isConnected}
            placeholder={
              activeSlug
                ? "Type a follow-up..."
                : "Type an analysis query to begin..."
            }
          />
          <footer className="flex justify-end px-4 py-2 border-t border-gray-100">
            <CostBadge />
          </footer>
        </main>
        <TodoPanel />
      </div>
    </div>
  );
}
