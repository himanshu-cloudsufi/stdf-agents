import { useState, useMemo, memo, type CSSProperties } from "react";
import { ChevronRight, Brain } from "lucide-react";

const DELAY_0: CSSProperties = { animationDelay: "0ms" };
const DELAY_150: CSSProperties = { animationDelay: "150ms" };
const DELAY_300: CSSProperties = { animationDelay: "300ms" };

interface ThinkingBlockProps {
  content: string;
  isActiveThinking: boolean;
}

const ThinkingBlockInner: React.FC<ThinkingBlockProps> = ({
  content,
  isActiveThinking,
}) => {
  const [isExpanded, setIsExpanded] = useState(false);

  const previewText = useMemo(() => {
    if (!content) return "";
    const lines = content.split("\n");
    const firstLine = lines[0];
    if (firstLine.length > 60) {
      return firstLine.substring(0, 60) + "\u2026";
    }
    if (lines.length > 1) {
      return firstLine + "\u2026";
    }
    return firstLine;
  }, [content]);

  return (
    <div className="group/thinking">
      <button
        type="button"
        onClick={() => setIsExpanded((prev) => !prev)}
        className="-ml-1 flex items-center gap-1.5 rounded-md px-1 py-0.5 transition-colors duration-150 hover:bg-gray-50"
      >
        <Brain className="h-3 w-3 text-gray-400" />
        <span className="text-xs font-medium text-gray-500">
          {isActiveThinking ? "Thinking" : "Thought process"}
        </span>
        {isActiveThinking && (
          <div className="flex gap-0.5">
            <div
              className="h-0.5 w-0.5 animate-bounce rounded-full bg-gray-400"
              style={DELAY_0}
            />
            <div
              className="h-0.5 w-0.5 animate-bounce rounded-full bg-gray-400"
              style={DELAY_150}
            />
            <div
              className="h-0.5 w-0.5 animate-bounce rounded-full bg-gray-400"
              style={DELAY_300}
            />
          </div>
        )}
        {!isExpanded && content && (
          <span className="max-w-48 truncate text-xs text-gray-400">
            {previewText}
          </span>
        )}
        <ChevronRight
          className={`h-3 w-3 text-gray-400 transition-transform duration-200 ${isExpanded ? "rotate-90" : ""}`}
        />
      </button>

      <div
        className={`overflow-hidden transition-[max-height,opacity] duration-200 ease-in-out ${
          isExpanded ? "mt-1.5 max-h-96 opacity-100" : "max-h-0 opacity-0"
        }`}
      >
        {content && (
          <div className="border-l border-gray-200 pl-3">
            <div className="max-h-80 overflow-y-auto whitespace-pre-wrap text-xs leading-relaxed text-gray-500">
              {content}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export const ThinkingBlock = memo(ThinkingBlockInner);
