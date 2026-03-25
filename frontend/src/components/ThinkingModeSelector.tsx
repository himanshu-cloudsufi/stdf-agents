import { memo, useCallback, useState, useRef, useEffect } from "react";
import { Brain, ChevronDown } from "lucide-react";

interface ThinkingModeOption {
  value: string;
  label: string;
  tokens: string;
}

const THINKING_MODES: ThinkingModeOption[] = [
  { value: "off", label: "Off", tokens: "0" },
  { value: "low", label: "Low", tokens: "4k" },
  { value: "medium", label: "Medium", tokens: "10k" },
  { value: "high", label: "High", tokens: "15k" },
  { value: "ultra", label: "Ultra", tokens: "32k" },
];

interface Props {
  sendControl: (msg: Record<string, unknown>) => void;
}

export const ThinkingModeSelector = memo(function ThinkingModeSelector({
  sendControl,
}: Props) {
  const [selected, setSelected] = useState<string>("off");
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  const current = THINKING_MODES.find((m) => m.value === selected) ?? THINKING_MODES[0];

  const handleSelect = useCallback(
    (mode: ThinkingModeOption) => {
      setSelected(mode.value);
      setOpen(false);
      sendControl({ type: "set_thinking", mode: mode.value });
    },
    [sendControl],
  );

  // Close dropdown on outside click
  useEffect(() => {
    function handleClickOutside(e: MouseEvent) {
      if (ref.current && !ref.current.contains(e.target as Node)) {
        setOpen(false);
      }
    }
    if (open) {
      document.addEventListener("mousedown", handleClickOutside);
      return () => document.removeEventListener("mousedown", handleClickOutside);
    }
  }, [open]);

  return (
    <div ref={ref} className="relative inline-block">
      <button
        type="button"
        onClick={() => setOpen((o) => !o)}
        className="flex items-center gap-1 px-2 py-1 text-xs text-gray-500 hover:text-gray-700 hover:bg-gray-100 rounded transition-colors cursor-pointer"
      >
        <Brain size={14} />
        <span>{current.label}</span>
        <ChevronDown size={12} className={`transition-transform ${open ? "rotate-180" : ""}`} />
      </button>
      {open && (
        <div className="absolute bottom-full left-0 mb-1 w-36 bg-white border border-gray-200 rounded-lg shadow-lg z-50 py-1">
          {THINKING_MODES.map((mode) => (
            <button
              key={mode.value}
              type="button"
              onClick={() => handleSelect(mode)}
              className={`w-full flex items-center justify-between px-3 py-1.5 text-xs hover:bg-gray-50 cursor-pointer ${
                mode.value === selected ? "text-blue-600 font-medium" : "text-gray-700"
              }`}
            >
              <span>{mode.label}</span>
              <span className="text-gray-400 tabular-nums">{mode.tokens}</span>
            </button>
          ))}
        </div>
      )}
    </div>
  );
});
