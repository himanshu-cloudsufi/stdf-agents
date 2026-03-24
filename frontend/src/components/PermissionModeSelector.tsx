import { memo, useCallback, useState, useRef, useEffect } from "react";
import { Shield, ChevronDown } from "lucide-react";

interface PermissionModeOption {
  value: string;
  label: string;
  wsValue: string;
}

const PERMISSION_MODES: PermissionModeOption[] = [
  { value: "auto", label: "Auto", wsValue: "bypassPermissions" },
  { value: "ask", label: "Ask", wsValue: "default" },
  { value: "plan", label: "Plan", wsValue: "plan" },
];

interface Props {
  sendControl: (msg: Record<string, unknown>) => void;
}

export const PermissionModeSelector = memo(function PermissionModeSelector({
  sendControl,
}: Props) {
  const [selected, setSelected] = useState<string>("auto");
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  const current = PERMISSION_MODES.find((m) => m.value === selected) ?? PERMISSION_MODES[0];

  const handleSelect = useCallback(
    (mode: PermissionModeOption) => {
      setSelected(mode.value);
      setOpen(false);
      sendControl({ type: "set_permission_mode", mode: mode.wsValue });
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
        <Shield size={14} />
        <span>{current.label}</span>
        <ChevronDown size={12} className={`transition-transform ${open ? "rotate-180" : ""}`} />
      </button>
      {open && (
        <div className="absolute bottom-full left-0 mb-1 w-32 bg-white border border-gray-200 rounded-lg shadow-lg z-50 py-1">
          {PERMISSION_MODES.map((mode) => (
            <button
              key={mode.value}
              type="button"
              onClick={() => handleSelect(mode)}
              className={`w-full text-left px-3 py-1.5 text-xs hover:bg-gray-50 cursor-pointer ${
                mode.value === selected ? "text-blue-600 font-medium" : "text-gray-700"
              }`}
            >
              {mode.label}
            </button>
          ))}
        </div>
      )}
    </div>
  );
});
