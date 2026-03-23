import { useAnalysisStore } from "../stores/useAnalysisStore";
import type { Analysis, AnalysisStatus } from "../types";

const statusColors: Record<AnalysisStatus, string> = {
  idle: "bg-gray-400",
  streaming: "bg-amber-400 animate-pulse",
  complete: "bg-green-500",
  error: "bg-red-500",
};

const statusLabels: Record<AnalysisStatus, string> = {
  idle: "Idle",
  streaming: "Running",
  complete: "Complete",
  error: "Error",
};

function formatTime(ts: number): string {
  return new Date(ts).toLocaleTimeString([], {
    hour: "numeric",
    minute: "2-digit",
  });
}

function groupByDate(analyses: Analysis[]): { label: string; items: Analysis[] }[] {
  const now = new Date();
  const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  const yesterday = new Date(today.getTime() - 86_400_000);
  const weekAgo = new Date(today.getTime() - 7 * 86_400_000);

  const groups: { label: string; items: Analysis[] }[] = [
    { label: "Today", items: [] },
    { label: "Yesterday", items: [] },
    { label: "Previous 7 Days", items: [] },
    { label: "Older", items: [] },
  ];

  for (const a of analyses) {
    const created = new Date(a.createdAt);
    if (created >= today) groups[0].items.push(a);
    else if (created >= yesterday) groups[1].items.push(a);
    else if (created >= weekAgo) groups[2].items.push(a);
    else groups[3].items.push(a);
  }

  return groups.filter((g) => g.items.length > 0);
}

export function AnalysisTabs() {
  const analyses = useAnalysisStore((s) => s.analyses);
  const activeSlug = useAnalysisStore((s) => s.activeSlug);
  const setActive = useAnalysisStore((s) => s.setActive);
  const clearActive = useAnalysisStore((s) => s.clearActive);
  const removeAnalysis = useAnalysisStore((s) => s.removeAnalysis);

  const sorted = [...analyses.values()].sort(
    (a, b) => b.createdAt - a.createdAt,
  );
  const groups = groupByDate(sorted);

  return (
    <aside className="w-64 border-r border-gray-200 bg-gray-50 flex flex-col">
      <div className="p-3 border-b border-gray-200">
        <button
          onClick={clearActive}
          className="w-full flex items-center justify-center gap-2 px-3 py-2 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700 transition-colors cursor-pointer"
        >
          <svg
            className="w-4 h-4"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M12 4v16m8-8H4"
            />
          </svg>
          New Analysis
        </button>
      </div>

      <nav className="flex-1 overflow-y-auto">
        {groups.length === 0 && (
          <div className="px-4 py-8 text-center text-sm text-gray-400">
            No sessions yet.
            <br />
            Type a query below to start.
          </div>
        )}

        {groups.map((group) => (
          <div key={group.label}>
            <div className="px-4 pt-4 pb-1">
              <span className="text-xs font-semibold text-gray-400 uppercase tracking-wider">
                {group.label}
              </span>
            </div>
            <div className="px-2 space-y-0.5">
              {group.items.map((analysis) => (
                <SessionItem
                  key={analysis.slug}
                  analysis={analysis}
                  isActive={activeSlug === analysis.slug}
                  onSelect={() => setActive(analysis.slug)}
                  onDelete={() => removeAnalysis(analysis.slug)}
                />
              ))}
            </div>
          </div>
        ))}
      </nav>
    </aside>
  );
}

function SessionItem({
  analysis,
  isActive,
  onSelect,
  onDelete,
}: {
  analysis: Analysis;
  isActive: boolean;
  onSelect: () => void;
  onDelete: () => void;
}) {
  return (
    <button
      onClick={onSelect}
      className={`group w-full text-left px-3 py-2 rounded-md text-sm transition-colors cursor-pointer relative ${
        isActive
          ? "bg-blue-100 text-blue-900"
          : "text-gray-700 hover:bg-gray-100"
      }`}
    >
      <div className="flex items-start gap-2 min-w-0">
        <span
          className={`w-2 h-2 rounded-full shrink-0 mt-1.5 ${statusColors[analysis.status]}`}
          title={statusLabels[analysis.status]}
        />
        <div className="min-w-0 flex-1">
          <div className="truncate font-medium">{analysis.label}</div>
          <div className="flex items-center justify-between text-xs text-gray-400 mt-0.5">
            <span>{formatTime(analysis.createdAt)}</span>
            {analysis.cost != null && (
              <span>${analysis.cost.toFixed(2)}</span>
            )}
          </div>
        </div>
      </div>
      <button
        onClick={(e) => {
          e.stopPropagation();
          onDelete();
        }}
        className="absolute top-1.5 right-1.5 p-1 rounded opacity-0 group-hover:opacity-100 hover:bg-red-100 text-gray-400 hover:text-red-500 transition-all cursor-pointer"
        title="Delete session"
      >
        <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
    </button>
  );
}
