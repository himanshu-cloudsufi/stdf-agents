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
        <div className="flex items-center gap-1.5">
          <span
            className={`inline-block h-2 w-2 rounded-full ${
              isConnected ? "bg-green-500" : "bg-red-500"
            }`}
          />
          <span
            className={`text-xs ${isConnected ? "text-green-700" : "text-red-600"}`}
          >
            {isConnected ? "Connected" : "Disconnected"}
          </span>
        </div>
        <span className="text-sm text-gray-500">{userId}</span>
      </div>
    </header>
  );
}
