import { useAnalysisStore } from "../stores/useAnalysisStore";
import type { TodoItem } from "../types";

const statusConfig: Record<
  TodoItem["status"],
  { icon: string; bg: string; text: string; border: string }
> = {
  pending: { icon: "○", bg: "bg-gray-50", text: "text-gray-500", border: "border-gray-200" },
  in_progress: {
    icon: "◉",
    bg: "bg-blue-50",
    text: "text-blue-700",
    border: "border-blue-300",
  },
  completed: {
    icon: "✓",
    bg: "bg-emerald-50",
    text: "text-emerald-700",
    border: "border-emerald-300",
  },
};

export function TodoPanel() {
  const analyses = useAnalysisStore((s) => s.analyses);
  const activeSlug = useAnalysisStore((s) => s.activeSlug);
  const analysis = activeSlug ? analyses.get(activeSlug) : null;
  const todos = analysis?.todos ?? [];

  if (todos.length === 0) return null;

  const done = todos.filter((t) => t.status === "completed").length;
  const pct = Math.round((done / todos.length) * 100);

  return (
    <aside className="w-72 border-l border-gray-200 bg-gray-50/50 flex flex-col overflow-hidden shrink-0">
      <div className="px-4 py-3 border-b border-gray-200">
        <h2 className="text-sm font-semibold text-gray-800">Pipeline Progress</h2>
        <div className="mt-2 flex items-center gap-2">
          <div className="flex-1 h-1.5 bg-gray-200 rounded-full overflow-hidden">
            <div
              className="h-full bg-emerald-500 rounded-full transition-all duration-500"
              style={{ width: `${pct}%` }}
            />
          </div>
          <span className="text-xs text-gray-500 tabular-nums">
            {done}/{todos.length}
          </span>
        </div>
      </div>
      <div className="flex-1 overflow-y-auto px-3 py-2 space-y-1.5">
        {todos.map((todo, i) => {
          const cfg = statusConfig[todo.status];
          return (
            <div
              key={i}
              className={`flex items-start gap-2 px-3 py-2 rounded-lg border ${cfg.bg} ${cfg.border}`}
            >
              <span
                className={`text-sm shrink-0 mt-0.5 ${cfg.text} ${
                  todo.status === "in_progress" ? "animate-pulse" : ""
                }`}
              >
                {cfg.icon}
              </span>
              <div className="min-w-0">
                <p className={`text-xs font-medium ${cfg.text} leading-snug`}>
                  {todo.content}
                </p>
                {todo.status === "in_progress" && todo.activeForm && (
                  <p className="text-[10px] text-blue-500 mt-0.5 truncate">
                    {todo.activeForm}
                  </p>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </aside>
  );
}
