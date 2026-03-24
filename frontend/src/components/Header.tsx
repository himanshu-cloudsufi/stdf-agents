import { useAnalysisStore } from "../stores/useAnalysisStore";

export function Header() {
  const userId = useAnalysisStore((s) => s.userId);
  const isConnected = useAnalysisStore((s) => s.isConnected);

  return (
    <header className="flex items-center justify-between px-6 py-3 border-b border-gray-200 bg-white">
      <h1 className="text-lg font-semibold text-gray-900">
        STDF Analysis Platform
      </h1>
      <div className="flex items-center gap-3">
        {!isConnected && (
          <span className="text-xs text-amber-600 bg-amber-50 px-2 py-1 rounded">
            Reconnecting...
          </span>
        )}
        <span className="text-sm text-gray-500">{userId}</span>
      </div>
    </header>
  );
}
