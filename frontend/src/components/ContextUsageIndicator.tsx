import { memo, useMemo } from "react";

interface Props {
  used: number;
  total: number;
}

function formatTokens(n: number): string {
  if (n >= 1_000_000) return `${(n / 1_000_000).toFixed(0)}M`;
  if (n >= 1_000) return `${(n / 1_000).toFixed(0)}k`;
  return String(n);
}

export const ContextUsageIndicator = memo(function ContextUsageIndicator({
  used,
  total,
}: Props) {
  const pct = total > 0 ? Math.min((used / total) * 100, 100) : 0;

  const color = useMemo(() => {
    if (pct > 95) return "#ef4444"; // red
    if (pct > 75) return "#f59e0b"; // amber
    return "#9ca3af"; // gray
  }, [pct]);

  // SVG circular progress ring
  const size = 28;
  const strokeWidth = 2.5;
  const radius = (size - strokeWidth) / 2;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference - (pct / 100) * circumference;

  const tooltip = `${formatTokens(used)} / ${formatTokens(total)} tokens`;

  return (
    <div className="relative inline-flex items-center justify-center" title={tooltip}>
      <svg width={size} height={size} className="-rotate-90">
        {/* Background circle */}
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          fill="none"
          stroke="#e5e7eb"
          strokeWidth={strokeWidth}
        />
        {/* Progress arc */}
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          fill="none"
          stroke={color}
          strokeWidth={strokeWidth}
          strokeDasharray={circumference}
          strokeDashoffset={offset}
          strokeLinecap="round"
          className="transition-all duration-300"
        />
      </svg>
      {/* Center percentage text */}
      <span
        className="absolute text-[8px] font-medium tabular-nums"
        style={{ color }}
      >
        {Math.round(pct)}%
      </span>
    </div>
  );
});
