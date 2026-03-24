import { useState } from "react";
import { Streamdown } from "streamdown";
import { code } from "@streamdown/code";

interface AllowedPrompt {
  tool: string;
  prompt: string;
}

interface Props {
  plan: string;
  allowedPrompts: AllowedPrompt[];
  onApprove: () => void;
  onReject: (feedback: string) => void;
  answered: boolean;
}

export function PlanApprovalCard({
  plan,
  allowedPrompts,
  onApprove,
  onReject,
  answered,
}: Props) {
  const [rejecting, setRejecting] = useState(false);
  const [feedback, setFeedback] = useState("");
  const [expanded, setExpanded] = useState(true);

  return (
    <div className="border-2 border-emerald-200 rounded-xl bg-emerald-50/50 p-4 my-3 space-y-3">
      <div
        className="flex items-center gap-2 cursor-pointer select-none"
        onClick={() => setExpanded(!expanded)}
      >
        <span className="text-lg">📋</span>
        <span className="text-sm font-semibold text-emerald-800">
          Plan Ready for Approval
        </span>
        <span className="text-xs text-gray-400 ml-auto">
          {expanded ? "▼" : "▶"}
        </span>
      </div>

      {expanded && plan && (
        <div className="bg-white rounded-lg border border-emerald-100 p-4 max-h-96 overflow-y-auto">
          <Streamdown mode="static" plugins={{ code }}>
            {plan}
          </Streamdown>
        </div>
      )}

      {expanded && allowedPrompts.length > 0 && (
        <div className="space-y-1">
          <p className="text-xs font-medium text-gray-600 uppercase tracking-wider">
            Permissions requested:
          </p>
          <div className="space-y-1">
            {allowedPrompts.map((p, i) => (
              <div
                key={i}
                className="flex items-center gap-2 px-3 py-1.5 bg-white rounded border border-gray-200 text-xs"
              >
                <span className="text-gray-400 font-mono">{p.tool}</span>
                <span className="text-gray-700">{p.prompt}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {!answered && !rejecting && (
        <div className="flex gap-2">
          <button
            onClick={onApprove}
            className="flex-1 px-4 py-2 text-sm font-medium text-white bg-emerald-600 rounded-lg hover:bg-emerald-700 transition-colors cursor-pointer"
          >
            Approve & Execute
          </button>
          <button
            onClick={() => setRejecting(true)}
            className="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-200 rounded-lg hover:bg-gray-300 transition-colors cursor-pointer"
          >
            Reject
          </button>
        </div>
      )}

      {!answered && rejecting && (
        <div className="space-y-2">
          <textarea
            value={feedback}
            onChange={(e) => setFeedback(e.target.value)}
            placeholder="What should be changed?"
            className="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg resize-none"
            rows={2}
          />
          <div className="flex gap-2">
            <button
              onClick={() => onReject(feedback)}
              className="px-4 py-2 text-sm font-medium text-white bg-red-600 rounded-lg hover:bg-red-700 transition-colors cursor-pointer"
            >
              Send Feedback
            </button>
            <button
              onClick={() => setRejecting(false)}
              className="px-4 py-2 text-sm font-medium text-gray-600 hover:text-gray-800 transition-colors cursor-pointer"
            >
              Cancel
            </button>
          </div>
        </div>
      )}

      {answered && (
        <div className="text-xs text-emerald-600 font-medium flex items-center gap-1">
          <span>✓</span> Plan approved — executing...
        </div>
      )}
    </div>
  );
}
