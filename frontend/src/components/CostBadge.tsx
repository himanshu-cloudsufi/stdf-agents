import { useAnalysisStore } from "../stores/useAnalysisStore";

export function CostBadge() {
  const analyses = useAnalysisStore((s) => s.analyses);
  const activeSlug = useAnalysisStore((s) => s.activeSlug);
  const analysis = activeSlug ? analyses.get(activeSlug) : null;

  if (!analysis?.cost) return null;

  return (
    <span className="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded">
      Cost: ${analysis.cost.toFixed(2)}
    </span>
  );
}
