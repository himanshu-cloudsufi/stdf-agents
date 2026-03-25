import { memo, useState } from "react";
import { ChevronDown, DollarSign } from "lucide-react";

interface Props {
  cost: number | null;
  duration?: number;
  inputTokens?: number;
  outputTokens?: number;
}

function formatTokens(n: number): string {
  if (n >= 1_000_000) return `${(n / 1_000_000).toFixed(1)}M`;
  if (n >= 1_000) return `${(n / 1_000).toFixed(1)}k`;
  return String(n);
}

export const MessageMetadata = memo(function MessageMetadata({
  cost,
  duration,
  inputTokens,
  outputTokens,
}: Props) {
  const [expanded, setExpanded] = useState(false);

  if (cost == null) return null;

  return (
    <div className="mt-1 ml-1">
      <button
        type="button"
        onClick={() => setExpanded((e) => !e)}
        className="flex items-center gap-1 text-xs text-gray-400 hover:text-gray-600 transition-colors cursor-pointer"
      >
        <DollarSign size={12} />
        <span>Cost: ${cost.toFixed(2)}</span>
        <ChevronDown
          size={12}
          className={`transition-transform ${expanded ? "rotate-180" : ""}`}
        />
      </button>
      {expanded && (
        <div className="mt-1 flex gap-3 text-xs text-gray-400 pl-4">
          {duration != null && <span>{(duration / 1000).toFixed(1)}s</span>}
          {inputTokens != null && (
            <span>In: {formatTokens(inputTokens)}</span>
          )}
          {outputTokens != null && (
            <span>Out: {formatTokens(outputTokens)}</span>
          )}
        </div>
      )}
    </div>
  );
});
