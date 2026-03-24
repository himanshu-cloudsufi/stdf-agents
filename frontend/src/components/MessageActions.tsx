import { useState, useCallback } from "react";
import { Copy, Check } from "lucide-react";

interface Props {
  content: string;
}

export function MessageActions({ content }: Props) {
  const [copied, setCopied] = useState(false);

  const handleCopy = useCallback(() => {
    navigator.clipboard.writeText(content).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 1500);
    });
  }, [content]);

  return (
    <div className="absolute top-1 right-1 opacity-0 group-hover:opacity-100 transition-opacity">
      <button
        type="button"
        onClick={handleCopy}
        className="flex items-center gap-1 px-1.5 py-0.5 text-[10px] text-gray-500 bg-white border border-gray-200 rounded shadow-sm hover:bg-gray-50 transition-colors cursor-pointer"
        title="Copy message"
      >
        {copied ? (
          <>
            <Check className="h-3 w-3 text-green-500" />
            <span className="text-green-600">Copied!</span>
          </>
        ) : (
          <>
            <Copy className="h-3 w-3" />
            <span>Copy</span>
          </>
        )}
      </button>
    </div>
  );
}
